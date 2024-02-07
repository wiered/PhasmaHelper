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
from PIL import Image

from core.windows import PrestigeCalculatorWindow
from core.utils import is_window_exists

MAP_ICON = "./core/icons/map.png"
PRESTIGE_ICON = "./core/icons/prestige.png"


class ToolsFrame(ctk.CTkFrame):
    def __init__(self, master, width):
        super().__init__(master, width=width)
        
        self.master = master
        self.prestige_calculator_window = None
        
        self.label_tools = ctk.CTkLabel(master=self, text="Tools")
        self.label_tools.grid(
            row=0, 
            column=0, 
            columnspan=1,
            padx=(30, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        
        map_icon = ctk.CTkImage(
            light_image=Image.open(MAP_ICON),
            dark_image=Image.open(MAP_ICON),
            size=(30, 30)
        )
        self.map_button = ctk.CTkButton(
            master=self,
            width=150,
            height=30,
            anchor="w",
            text="Maps(WIP)",
            image=map_icon
        )
        self.map_button.grid(
            row=1, 
            column=0, 
            columnspan=1, 
            padx=(20, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        
        prestige_icon = ctk.CTkImage(
            light_image=Image.open(PRESTIGE_ICON),
            dark_image=Image.open(PRESTIGE_ICON),
            size=(30, 30)
        )
        self.prestige_calculator_button = ctk.CTkButton(
            master=self,
            width=150,
            height=30,
            anchor="w",
            text="Prestige Calculator",
            image=prestige_icon
        )
        self.prestige_calculator_button.grid(
            row=1, 
            column=1, 
            columnspan=1, 
            padx=(20, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        self.prestige_calculator_button.configure(command=self.create_prestige_calculator_window)
        
    def create_prestige_calculator_window(self):
        """ Creating the GhostInfoWindow

        Args:
            name (str): name of ghost
        """
        if self.prestige_calculator_window is None:
            self.prestige_calculator_window = PrestigeCalculatorWindow(self)  # create window if its None or destroyed
        elif not self.prestige_calculator_window.winfo_exists():
            self.prestige_calculator_window = PrestigeCalculatorWindow(self)

        self.prestige_calculator_window.focus()
        
    def destroy_windows(self):
        if is_window_exists(self.prestige_calculator_window):
            self.prestige_calculator_window.destroy()
            self.prestige_calculator_window = None