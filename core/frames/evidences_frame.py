"""
    PhasmaHelper
    Copyright (C) 2023 Wiered

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from copy import copy
import time

import customtkinter as ctk
from icecream import ic

from core.widgets import EvidenceSwitch, EvidenceButton
from core.utils import EvidencesManager, lists

MIMIC_EVIDENCES = ['Spirit Box', 'Ultra V.', 'Otbs', 'Freezing']

class EvidencesFrame(ctk.CTkFrame):
    def __init__(self, master, disable_spirits):
        super().__init__(master)
        
        self.evidences_manager = EvidencesManager()

        self.label_evidences = ctk.CTkLabel(master=self,text="EVIDENCES")
        self.label_evidences.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        
        self.emf_switch = EvidenceButton(
            self,
            command=lambda: disable_spirits("EMF 5", self.emf_switch.state),
            text="EMF 5"
            )
        self.emf_switch.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")

        self.spirit_box_switch = EvidenceButton(
            master=self,
            command=lambda: disable_spirits("Spirit Box", self.spirit_box_switch.state),
            text="Spirit Box",
        )
        self.spirit_box_switch.grid(row=4, column=0, pady=10, padx=20, sticky="nsew")

        self.fingerprints_switch = EvidenceButton(
            master=self,
            command=lambda: disable_spirits("Ultra V.", self.fingerprints_switch.state),
            text="Ultra V.",
        )
        self.fingerprints_switch.grid(row=5, column=0, pady=10, padx=20, sticky="nsew")
        
        self.ghost_orb_switch = EvidenceButton(
            master=self,
            command=lambda: disable_spirits("Orbs", self.ghost_orb_switch.state),
            text="Orbs",
            )
        self.ghost_orb_switch.grid(row=6, column=0, pady=10, padx=20, sticky="nsew")

        self.ghost_writing_switch = EvidenceButton(
            master=self,
            command=lambda: disable_spirits("Writing", self.ghost_writing_switch.state),
            text="Writing",
            )
        self.ghost_writing_switch.grid(row=7, column=0, pady=10, padx=20, sticky="nsew")

        self.freezing_temp_switch = EvidenceButton(
            master=self,
            command=lambda: disable_spirits("Freezing", self.freezing_temp_switch.state),
            text="Freezing",
            )
        self.freezing_temp_switch.grid(row=8, column=0, pady=10, padx=20, sticky="nsew")

        self.dots_switch = EvidenceButton(
            master=self,
            command=lambda: disable_spirits("DOTS", self.dots_switch.state),
            text="DOTS",
            )
        self.dots_switch.grid(row=9, column=0, pady=10, padx=20, sticky="nsew")
    
    @property
    def activated_evidences_count(self):
        return len(self.evidences_manager.activated_evidences)
    
    @property
    def activated_evidences(self):
        return self.evidences_manager.activated_evidences
    
    @property
    def buttons(self):
        return self.winfo_children()[1:]
    
    def get_button_by_name(self, value):
        for button in self.buttons:
            if button.text == value:
                return button
            
        raise ValueError("Wrong Button Name")
    
    def get_possible_ghosts(self, difficulty):
        return self.evidences_manager.get_possible_ghosts(difficulty)
    
    def enable_switches(self, included):
        """ Enables switch if switch index in included, otherwise disables it

        Args:
            included (List[int]): included switches
        """
        for i, button in enumerate(self.winfo_children()[1:]):
            state = "normal" if i in included else "disabled"
            if state == "disabled":
                button.reset()
                self.evidences_manager.change_evidence_state(button.text, 0)
                
            button.configure(state=state)
    
    def disable_switches(self, included):
        """ Disables switch if switch index in included, otherwise enables it

        Args:
            included (List[int]): included switches
        """
        _included = list(set(range(7)) ^ set(included))
        self.enable_switches(_included)
        
        del _included
    
    def enable_switches_by_name(self, included):
        for button in self.winfo_children()[1:]:
            state = "normal" if button.text in included else "disabled"
            if state == "disabled":
                button.reset()
                self.evidences_manager.change_evidence_state(button.text, 0)
            
            button.configure(state=state)
            
    def disable_switches_by_name(self, included):
        _included = list(set(lists.EVIDENCES) ^ set(included))
        self.enable_switches_by_name(_included)
        
        del _included
    
    def reset_switches(self):
        self.evidences_manager.reset_evidences()
        self.enable_all_switches()
        for i in range(7):
            self.winfo_children()[i+1].reset()
    
    def enable_all_switches(self):
        self.enable_switches(range(7))
            
    def disable_all_switches(self):
        self.disable_switches(range(7))   
    
    def disable_excessive_switches(self, difficulty: int):
        """ Disable excessive switches based on difficulty

        Args:
            difficulty (int)
        """
        
        # for nightmare (3) -> 2 evidences => 5 - 3(difficulty) = 2(evidences)
        # for insane    (4) -> 1 evidence  => 5 - 4(difficulty) = 1(evidence)
        possible_evidences_count = 5 - difficulty
        
        #   if number of an active evidences more than n, disable excessive evidences switches
        #   else enable all evidences switches
        if len(self.evidences_manager.activated_evidences) >= possible_evidences_count:
            self.disable_switches_by_name(
                self.evidences_manager.get_unknown_evidences()
                )
        else:
            self.enable_all_switches()

    def enable_mimic_evidences_switches(self, difficulty):
        possible_evidences_count = 5 - difficulty
        
        # If the Mimic ghost is active and there are n active evidences, 
        #   enable the Mimic evidences switches
        if len(self.evidences_manager.activated_evidences) < possible_evidences_count:
            return
        
        if not "Мимик" in self.evidences_manager.get_possible_ghosts(difficulty):
            return
        
        if not self.activated_evidences_count == 5 - difficulty:
            return
            
        if "Ghost Orb" in self.activated_evidences:
            self.enable_switches_by_name(
                MIMIC_EVIDENCES + self.evidences_manager.disactivated_evidences
                )
        else:
            self.enable_switches_by_name(
                self.activated_evidences + ["Ghost Orb"] + self.evidences_manager.disactivated_evidences
                )
    
    def update_switches(self, difficulty: int, evidence: str = None, state: int = None):
        """Update switches"""
        
        if evidence != None and state != None:
            self.evidences_manager.change_evidence_state(evidence, state)
            self.get_button_by_name(evidence).set_state(state)

        # Disabke impossible switches
        self.disable_switches(
            self.evidences_manager.get_impossible_evidences()
            )
        
        if difficulty < 3:
            return
        
        # If the difficulty is Nightmare(3) or Insane(4) it will disable excessive switches
        self.disable_excessive_switches(difficulty)
        self.enable_mimic_evidences_switches(difficulty)
        # if evidence == "Ghost Orb":
        #     self.buttons[3].set_state(state)
        #     self.evidences_manager.change_evidence_state("Ghost Orb", state)
        # self.evidences_manager.set_disactivated_evidences(tmp)
                
        