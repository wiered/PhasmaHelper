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
from typing import List
import customtkinter as ctk

from core.utils import themes, get_ghost_data, adjust_lines_lenght, read_data
from core.utils import lists
from config import cfg


class GhostInfoFrame(ctk.CTkFrame):
    def __init__(self, master, name, get_ghost):
        super().__init__(master)
        
        self.state = True
        self.name = name
        self.get_ghost = get_ghost
        
        self.label_name = ctk.CTkLabel(master=self, text=name, width=350)
        self.label_name.grid(row=0, column=0, columnspan=4, padx=10, pady=0, sticky="w")
        
        self.label_evidences = ctk.CTkLabel(master=self, text="EMF, Spitit Box, DOTS")
        self.label_evidences.grid(row=1, column=0, columnspan=4, padx=5, pady=0, sticky="w")
        
        self.label_behavior = ctk.CTkLabel(master=self, text="Smudge sticks stop attacks for 3 min instead of 1.5 min")
        self.label_behavior.grid(row=2, column=0, columnspan=4, padx=5, pady=0, sticky="w")
        
        self.more_button = ctk.CTkButton(
            master=self,
            width=110,
            text="More...",
        )
        self.more_button.grid(row=3, column=0, columnspan=3, padx=(0, 0), pady=0, sticky="nsew")
        
        self.cross_off_button = ctk.CTkButton(
            master=self,
            width=20,
            text="-",
        )
        self.cross_off_button.grid(row=3, column=3, columnspan=1, padx=(0, 0), pady=0, sticky="nsew")
        self.cross_off_button.configure(
            fg_color=("#ff0000", "#ff0000"),
            font=("Arial", 20)
        )
        self.cross_off_button._command = lambda: self.change_state()
        
        self.get_data()
    
    def clear(self):
        self.label_name.configure(text = "")
        self.label_evidences.configure(text = "")
        self.label_behavior.configure(text = "\n\n\n\n")
    
    def set_name(self, name):
        self.name = name
        self.get_data()
    
    def get_data(self):
        self.clear()
        
        self.label_name.configure(
            text = self.name
        )
        
        data = get_ghost_data(self.name)
        evidences = data.get("evidences")
        self.label_evidences.configure(
            text = ", ".join(evidences)
        )
        
        behavior_data = adjust_lines_lenght(data.get("behavior"))
        self.label_behavior.configure(
            text = "\n".join(behavior_data),
            justify = 'left'
        )

        self.more_button._command = lambda: self.get_ghost(self.name)
        
        if self.name == "Null":
            self.more_button.configure(
                state = "disabled"
            )
            self.cross_off_button.configure(
                state = "disabled"
            )
        else:
            self.more_button.configure(
                state = "normal"
            )
            self.cross_off_button.configure(
                state = "normal"
            )

    def change_state(self):
        if self.state:
            self.disable()
        else:
            self.enable()
            
    def enable(self):
        self.clear()
        self.state = True
        self.label_name.configure(
            font = ("Arial", 15)
            )
        self.get_data()
        self.configure(
            fg_color = themes.ghost_info_frame_activated
        )
        
    def disable(self):
        self.clear()
        self.state = False
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        article = "an" if self.name[0] in vowels else "a"
        self.label_name.configure(
            text=f"Not {article} {self.name}",
            font = ("Arial", 20)
            )
        self.label_evidences.configure(text="")
        self.label_behavior.configure(text="\n\n\n")
        self.configure(
            fg_color = themes.ghost_info_frame_deactivated
        )
    

class GhostsFrame(ctk.CTkFrame):
    def __init__(self, master, get_ghost):
        super().__init__(master)
        read_data(cfg.language)
        self.possible_ghosts = copy(lists.GHOSTS_EN)
        
        self.page = 0
        
        self.previous_page_button = ctk.CTkButton(
            master=self,
            width=10,
            text="<",
            height=200,
        )
        self.previous_page_button.grid(row=1, column=0, rowspan=3, padx=0, pady=0, sticky="w")
        self.previous_page_button._command = lambda: self.prev_page()
        
        self.next_page_button = ctk.CTkButton(
            master=self,
            width=10,
            text=">",
            height=200,
        )
        self.next_page_button.grid(row=1, column=4, rowspan=4, padx=(0, 0), pady=0, sticky="w")
        self.next_page_button._command = lambda: self.next_page()
        
        self.ghost_1_1 = GhostInfoFrame(
            master=self,
            get_ghost=get_ghost,
            name="Spirit",
        )
        self.ghost_1_2 = GhostInfoFrame(
            master=self,
            get_ghost=get_ghost,
            name="Wraith",
        )
        self.ghost_1_3 = GhostInfoFrame(
            master=self,
            get_ghost=get_ghost,
            name="Phantom",
        )

        self.ghost_2_1 = GhostInfoFrame(
            master=self,
            get_ghost=get_ghost,
            name="Poltergeist",
        )
        self.ghost_2_2 = GhostInfoFrame(
            master=self,
            get_ghost=get_ghost,
            name="Banshee",
        )
        self.ghost_2_3 = GhostInfoFrame(
            master=self,
            get_ghost=get_ghost,
            name="Jinn",
        )

        self.ghost_3_1 = GhostInfoFrame(
            master=self,
            get_ghost=get_ghost,
            name="Mare",
        )
        self.ghost_3_2 = GhostInfoFrame(
            master=self,
            get_ghost=get_ghost,
            name="Revenant",
        )
        self.ghost_3_3 = GhostInfoFrame(
            master=self,
            get_ghost=get_ghost,
            name="Shade",
        )
    
        ###
        self.ghost_1_1.grid(row=1, column=1, padx=(20, 10), pady=10, sticky="nsew")
        self.ghost_1_2.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.ghost_1_3.grid(row=1, column=3, padx=(10, 20), pady=10, sticky="nsew")
        ###
        
        ###
        self.ghost_2_1.grid(row=2, column=1, padx=(20, 10), pady=10, sticky="nsew")
        self.ghost_2_2.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        self.ghost_2_3.grid(row=2, column=3, padx=(10, 20), pady=10, sticky="nsew")
        ###
        
        ###
        self.ghost_3_1.grid(row=3, column=1, padx=(20, 10), pady=10, sticky="nsew")
        self.ghost_3_2.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")
        self.ghost_3_3.grid(row=3, column=3, padx=(10, 20), pady=10, sticky="nsew")
        ###
        
        self.draw_page()
    
    def next_page(self):
        self.page = (self.page + 1)%3
        self.draw_page()
        
    def prev_page(self):
        self.page = (self.page - 1)%3
        self.draw_page()
            
    def draw_page(self):
        if self.page == 0:
            self.ghost_1_1.set_name("Spirit")
            self.ghost_1_2.set_name("Wraith")
            self.ghost_1_3.set_name("Phantom")
            self.ghost_2_1.set_name("Poltergeist")
            self.ghost_2_2.set_name("Banshee")
            self.ghost_2_3.set_name("Jinn")
            self.ghost_3_1.set_name("Mare")
            self.ghost_3_2.set_name("Revenant")
            self.ghost_3_3.set_name("Shade")
        elif self.page == 1:
            self.ghost_1_1.set_name("Demon")
            self.ghost_1_2.set_name("Yurei")
            self.ghost_1_3.set_name("Oni")
            self.ghost_2_1.set_name("Yokai")
            self.ghost_2_2.set_name("Hantu")
            self.ghost_2_3.set_name("Goryo")
            self.ghost_3_1.set_name("Myling")
            self.ghost_3_2.set_name("Onryo")
            self.ghost_3_3.set_name("The Twins")
        elif self.page == 2:
            self.ghost_1_1.set_name("Raiju")
            self.ghost_1_2.set_name("Obake")
            self.ghost_1_3.set_name("The Mimic")
            self.ghost_2_1.set_name("Moroi")
            self.ghost_2_2.set_name("Deogen")
            self.ghost_2_3.set_name("Thaye")
            self.ghost_3_1.set_name("Null")
            self.ghost_3_2.set_name("Null")
            self.ghost_3_3.set_name("Null")

        self.update_buttons(self.possible_ghosts)
        
    def _update_button(self, button, is_active: bool,):
        state = "normal" if is_active else "disabled"
        _theme = (themes.button_fg_color 
                  if is_active 
                  else themes.button_fg_color_dark)

        button.configure(state=state)
        button.configure(fg_color=_theme)
    
    def update_buttons(self, possible_ghosts: List):
        """ Enables all buttons for active ghosts

        Args:
            active_ghosts (List[str]): list of possible ghosts names
        """
        self.possible_ghosts = possible_ghosts
        
        for button in self.winfo_children()[2:]:
            if button.name in possible_ghosts:
                button.enable()
            else:
                button.disable()
            #self._update_button(button, button._text in possible_ghosts)

