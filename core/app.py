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

import customtkinter as ctk

from core import frames, windows, widgets
from core.helpers import lists, theme

def configure_colors(appearance, color_theme):
    ctk.set_appearance_mode(appearance)  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme(color_theme)  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # difficulty, active_evidences
        self.difficulty = 0
        self.active_evidences = []
        self.cursed_items_window_is_open = False
        
        self.cursed_items_window = None

        # Configure version and titlebar
        self.__version__ = "1.2"
        self.title(f"Phasma Helper v{self.__version__}")
        self.iconbitmap(".\core\icons\logo.ico")
        
        # Configure geometry
        self.geometry(f"{self.winfo_screenwidth()*0.4}x{0.4 * self.winfo_screenheight()} + 300 + 300")
        self.resizable(False, False)

        # Left menu bar
        self.left_menu_bar_frame = frames.LeftmenubarFrame(self, self.change_difficulty)

        # Spirits Frame
        self.ghosts_frame = frames.GhostsFrame(self, self.showGhostWindow)
        
        # Evidences Frame
        self.evidenced_frame = frames.EvidencesFrame(self, self.change_evidence_state)

        # Cursed Items Frame
        self.cursed_items_frame = frames.CursedItemsFrame(self, width=400, show_window=self.showCursedItemsWindow)
        
        # Tools Frame
        self.tools_frame = frames.ToolsFrame(self, width=400)

        # Difficulty and version lables
        self.label_difficulty = ctk.CTkLabel(master=self, text=f"Difficulty: Amauter")
        self.label_version = ctk.CTkLabel(master=self, text=f"Version {self.__version__}")
        
        # Grid all widgets, frames and labels
        self.left_menu_bar_frame.grid(
            row=1, 
            column=0, 
            padx=(0, 0), 
            pady=(0, 0), 
            rowspan=3, 
            sticky="nsew",
            )
        self.ghosts_frame.grid(
            row=1, 
            column=2, 
            columnspan=2, 
            padx=(0, 20), 
            pady=(20, 0), 
            sticky="nsew"
            )
        self.evidenced_frame.grid(
            row=1, 
            column=1,
            padx=(20, 20), 
            pady=(20, 0), 
            sticky="nsew"
            )
        self.cursed_items_frame.grid(
            row=2, 
            column=1, 
            columnspan=2, 
            padx=(20, 20), 
            pady=(20, 0), 
            sticky="nsew"
            )
        self.tools_frame.grid(
            row=2, 
            column=3, 
            padx=(0, 20), 
            pady=(20, 0), 
            sticky="nsew"
            )
        self.label_difficulty.grid(
            row=3, 
            column=1, 
            columnspan=1, 
            padx=(30, 30), 
            pady=10, 
            sticky="w"
            )
        self.label_version.grid(
            row=3, 
            column=3, 
            columnspan=1, 
            padx=(10, 30), 
            pady=10, 
            sticky="e"
            )
        
        # Get lists of buttons and switches
        self.spirts_buttons = self.ghosts_frame.winfo_children()[1:]
        self.difficulty_buttons = self.left_menu_bar_frame.get_difficulty_buttons()
        self.evidences_switches = self.evidenced_frame.winfo_children()[1:]
        

    def _is_evidence_switch_checked(self, evidence: str | ctk.CTkSwitch | widgets.EvidenceSwitch) -> bool:
        """ Return true if evidence is checked

        Args:
            evidence (str | ctk.CTkSwitch | widgets.EvidenceSwitch): evidence name or evidence switch

        Returns:
            bool: True if checked False else
        """
        
        evidence_name = None
        if isinstance(evidence, str):
            evidence_name = evidence
        elif isinstance(evidence, ctk.CTkSwitch):
            evidence = evidence.name
        elif isinstance(evidence, widgets.EvidenceSwitch):
            evidence_name = evidence.name
            
        return evidence_name in self.active_evidences

    def _get_active_ghosts(self) -> list[str]:
        """Returns a list of all matching ghosts

        Returns:
            list[str]: list of matching ghosts
        """
        ghosts = lists.GHOSTS
        for evidence in self.active_evidences:
            ghosts = [ghost for ghost in ghosts if ghost in lists.ghosts_by_evidences.get(evidence)]
            
        return ghosts

    def _enable_all_switches(self):
        """
        Enables all evidences switches
        """
        for i in range(7):
            self.evidences_switches[i].configure(state="normal")

    def _disable_unchecked_switches(self):
        """
        This function disables all evidence switches that are not currently checked.
        It does this by checking each switch and if it is not checked, disabling it.
        """
        for i in range(7):
            if not self._is_evidence_switch_checked(self.evidences_switches[i].name):
                self.evidences_switches[i].configure(state="disabled")

    def _chage_switches_state(self, n: int):
        #   if number of an active evidences more than n, disable other evidences switches
        #   else enable other evidences switches
        if len(self.active_evidences) >= n:
            self._disable_unchecked_switches()
        else:
            self._enable_all_switches()

    def _enable_mimic_switches(self):
        """ 
        Enables all mimic evidences switches
        """
        self.evidences_switches[1].configure(state="normal")
        self.evidences_switches[2].configure(state="normal")
        self.evidences_switches[3].configure(state="normal")
        self.evidences_switches[5].configure(state="normal")
        
    def _set_mimic_only_button(self):
        """
        This function sets the button for the Mimic ghost to be the only active button.
        It does this by disabling all other buttons and enabling the Mimic button.
        """
        for button in self.spirts_buttons:
            button.configure(state="disabled")
            button.configure(fg_color=theme.button_fg_color_dark)
            
        self.spirts_buttons[20].configure(state="normal")
        self.spirts_buttons[20].configure(fg_color=theme.button_fg_color)
        return

    def _update_switches(self):
        """Update switches"""
        # Get a list of all active ghosts
        ghosts = self._get_active_ghosts()
        
        # Loop through each evidence add it to enabled switches, then if there is
        #   no ghosts with this evidences, disable the switch
        for i, evidence in enumerate(lists.EVIDENCES):
            # Takes ghost in list of active ghosts, checks if he has that evidence, 
            #   and if so, adds it to tmp list
            tmp = [ghost for ghost in ghosts if ghost in lists.ghosts_by_evidences.get(evidence)]
            if len(tmp) == 0:
                self.evidences_switches[i].configure(state="disabled")
            else:
                self.evidences_switches[i].configure(state="normal")
        
        # If the difficulty is Nightmare(3)
        if self.difficulty == 3:
            self._chage_switches_state(2)
            # If the Mimic ghost is active and there are 2 active evidences, 
            #   enable the Mimic evidences switches
            if "Мимик" in ghosts and len(self.active_evidences) == 2:
                self._enable_mimic_switches()
        
        # If the difficulty is Insane(4)
        elif self.difficulty == 4:
            self._chage_switches_state(1)
            # If the Mimic ghost is active and there is only 1 active evidences, 
            #   enable the Mimic evidences switches
            if "Мимик" in ghosts and len(self.active_evidences) == 1:
                self._enable_mimic_switches()

    def _update_buttons(self):
        """Update buttons"""
        ghosts = self._get_active_ghosts()
        
        # If the difficulty is Nightmare(3) and there are 3 active evidences
        if self.difficulty == 3 and len(self.active_evidences) == 3:
            # Disables all except Mimic button
            self._set_mimic_only_button()
            return
        
        # If the difficulty is Insane(4) and there are 2 active evidences
        if self.difficulty == 4 and len(self.active_evidences) == 2:
            # Disables all except Mimic button 
            self._set_mimic_only_button()
            return
                
        for button in self.spirts_buttons:
            if button._text in ghosts:
                button.configure(state="normal")
                button.configure(fg_color=theme.button_fg_color)
            else:
                button.configure(state="disabled")
                button.configure(fg_color=theme.button_fg_color_dark)

    def change_evidence_state(self, evidence: str, state: int):
        """ Change state of buttons and switches according to checked evidences.

        Args:
            evidence (str): evidence name
            state (int): state of switch
        """
        if bool(state):
            self.active_evidences.append(evidence)
        else:
            self.active_evidences.remove(evidence)

        self._update_switches()
        self._update_buttons()

    def change_difficulty(self, difficulty: int):
        """ Changes difficulty setting. Also updates buttons and switches.

        Args:
            difficulty (int): diffiulty from 0 to 3, Amauter to Nightmare
        """
        self.difficulty_buttons[self.difficulty].configure(
            border_width=0,
            fg_color=theme.fg_color_frame_dark
        )
        self.difficulty = difficulty
        self.difficulty_buttons[self.difficulty].configure(
            border_width=1,
            fg_color=theme.fg_color_frame_dark_gray
        )
        self.label_difficulty.configure(text=f"Difficulty: {lists.DIFFICULTIES[self.difficulty]}")
        
        self._update_switches()
        self._update_buttons()

    def showGhostWindow(self, name: str):
        """ Show GhostInfoWindow

        Args:
            name (str): name of ghost
        """
        self.info = windows.GhostInfoWindow(name)
        self.info.attributes('-topmost', True)
        self.info.update()
        self.info.mainloop()

    def showCursedItemsWindow(self, item = "ouija_board"):
        """ Show GhostInfoWindow

        Args:
            name (str): name of ghost
        """
        if self.cursed_items_window is None or not self.cursed_items_window.winfo_exists():
            self.cursed_items_window = windows.CursedItemsWindow(item)
            self.cursed_items_window.attributes('-topmost', True)
            self.cursed_items_window.update()
            self.cursed_items_window.mainloop()
        else:
            self.cursed_items_window.change_item(item)
