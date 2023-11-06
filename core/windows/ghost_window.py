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

import textwrap

import customtkinter as ctk

from core.helpers import lists, theme
from config import cfg

BORDER_RADIUS = 0


class GhostInfoWindow(ctk.CTk):
    def __init__(self, name):
        super().__init__()

        self.get_ghost_info(name)

        self.title("Phasma Helper: %s" % name)
        self.iconbitmap(".\core\data\logo.ico")

        if cfg.is_minimalistic:
            self.text_label = ctk.CTkLabel(master=self, text=self.general_text)
            self.text_label.grid(row=0, column=0, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")
        else:
            self.ghost = ctk.CTkLabel(master=self, text=f"{name}")
            self.ghost.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=0, sticky="nsew")

            self.text = TextFrame(self)
            self.text.grid(row=2, column=0, columnspan=1, padx=(5, 5), pady=(5, 10), sticky="nsew")

            self.menu = MenuFrame(self, name, self.text.set_text)
            self.menu.grid(row=1, column=0, columnspan=1, padx=(170, 170), pady=10, sticky="nsew")


    def get_ghost_info(self, name):
        self.ghost_dict = lists.Ghosts_dict()

        self.behavior_text = self.ghost_dict.dict.get(name).get("behavior")
        self.evidences_text = self.ghost_dict.dict.get(name).get("evidences")
        self.advantages_text = self.ghost_dict.dict.get(name).get("advantages")
        self.strategy_text = self.ghost_dict.dict.get(name).get("strategy")

        self.behavior_text = textwrap.fill(self.behavior_text, width=100)
        self.evidences_text = "; ".join(self.evidences_text)
        self.advantages_text = textwrap.fill(self.advantages_text, width=100)
        self.strategy_text = textwrap.fill(self.strategy_text, width=100)

        self.general_text = ""
        self.general_text += f"=================== {name} ====================\n"
        self.general_text += self.behavior_text
        self.general_text += "\n===================   Улики   ====================\n"
        self.general_text += self.evidences_text
        self.general_text += "\n=================== Слабости  ====================\n"
        self.general_text += self.advantages_text
        self.general_text += "\n=================== Стратегия ====================\n"
        self.general_text += self.strategy_text


class MenuFrame(ctk.CTkFrame):
    def __init__(self, master, name, set_text):
        super().__init__(master)

        self.set_text = set_text
        self.tabs = [False, False, False, False]

        self.get_ghost_info(name)
        self.buttons = {}

        behavior = ctk.CTkButton(
            master=self,
            width=110,
            text="Behavior",
            corner_radius=0,
            border_width=BORDER_RADIUS,
        )
        behavior.grid(row=0, column=1, padx=(0,0), pady=0, sticky="nsew")
        behavior._command = lambda: self.change_tab(0)
        self.buttons.update({"behavior": behavior})

        evidences = ctk.CTkButton(
            master=self,
            width=110,
            text="Evidences",
            corner_radius=0,
            border_width=BORDER_RADIUS,
        )
        evidences.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
        evidences._command = lambda: self.change_tab(1)
        self.buttons.update({"evidences": evidences})

        advantages = ctk.CTkButton(
            master=self,
            width=110,
            text="Advantages",
            corner_radius=0,
            border_width=BORDER_RADIUS,
        )
        advantages.grid(row=0, column=3, padx=0, pady=0, sticky="nsew")
        advantages._command = lambda: self.change_tab(2)
        self.buttons.update({"advantages": advantages})

        strategy = ctk.CTkButton(
            master=self,
            width=110,
            text="Strategy",
            corner_radius=0,
            border_width=BORDER_RADIUS,
        )
        strategy.grid(row=0, column=4, padx=(0, 0), pady=0, sticky="nsew")
        strategy._command = lambda: self.change_tab(3)
        self.buttons.update({"strategy": strategy})

        self.change_tab(0)


    def change_tab(self, tab):
        self.tabs[tab] = not self.tabs[tab]

        temp_text = ""

        for i, tb in enumerate(lists.tabs):
            if self.tabs[i]:
                self.buttons[tb].configure(
                    fg_color=theme.button_fg_color_light,
                    bg_color=theme.button_fg_color_light,
                    border_color=theme.button_border_color_light,
                    )
                temp_text += f"\n=================== {tb} ====================\n"
                temp_text += self.texts[tb]
            else:
                self.buttons[tb].configure(
                    fg_color=theme.button_fg_color_dark,
                    bg_color=theme.button_fg_color_dark,
                    border_color=theme.button_border_color_dark,
                    )
                
        self.set_text(temp_text)
            

    def get_ghost_info(self, name):
        self.ghost_dict = lists.Ghosts_dict()

        self.texts = {}

        self.texts["behavior"] = self.ghost_dict.get(name).get("behavior")
        self.texts["evidences"] = self.ghost_dict.get(name).get("evidences")
        self.texts["advantages"] = self.ghost_dict.get(name).get("advantages")
        self.texts["strategy"] = self.ghost_dict.get(name).get("strategy")

        self.texts["behavior"] = textwrap.fill(self.texts["behavior"], width=100)
        self.texts["evidences"] = textwrap.fill("; ".join(self.texts["evidences"]), width=100)
        self.texts["advantages"] = textwrap.fill(self.texts["advantages"], width=100)
        self.texts["strategy"] = textwrap.fill(self.texts["strategy"], width=100)

        self.texts["general"] = ""
        self.texts["general"] += f"=================== {name} ====================\n"
        self.texts["general"] += self.texts["behavior"]
        self.texts["general"] += "\n===================   Улики   ====================\n"
        self.texts["general"] += self.texts["evidences"]
        self.texts["general"] += "\n=================== Слабости  ====================\n"
        self.texts["general"] += self.texts["advantages"]
        self.texts["general"] += "\n=================== Стратегия ====================\n"
        self.texts["general"] += self.texts["strategy"]


class TextFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.text = ctk.CTkLabel(master=self, text=f"sample")
        self.text.grid(row=0, column=0, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")


    def set_text(self, text):
        self.text.configure(text=text)
        
