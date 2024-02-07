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

from typing import List
import customtkinter as ctk

from core.utils import themes

class GhostsFrame(ctk.CTkFrame):
    def __init__(self, master, get_ghost):
        super().__init__(master)

        self.label_spirits = ctk.CTkLabel(master=self, text="SPIRITS")
        self.label_spirits.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

        spirit = ctk.CTkButton(
            master=self,
            width=110,
            text="Дух",
        )
        spirit.grid(row=1, column=0, padx=(20, 20), pady=10, sticky="nsew")

        wraith = ctk.CTkButton(
            master=self,
            width=110,
            text="Мираж",
        )
        wraith.grid(row=1, column=1, padx=(20, 20), pady=10, sticky="nsew")

        phantom = ctk.CTkButton(
            master=self,
            width=110,
            text="Фантом",
        )
        phantom.grid(row=1, column=2, padx=(20, 20), pady=10, sticky="nsew")

        poltergeist = ctk.CTkButton(
            master=self,
            width=110,
            text="Полтергейст",
        )
        poltergeist.grid(row=1, column=3, padx=(20, 20), pady=10, sticky="nsew")

        banshee = ctk.CTkButton(
            master=self,
            width=110,
            text="Банши",
        )
        banshee.grid(row=1, column=4, padx=(20, 20), pady=10, sticky="nsew")

        jinn = ctk.CTkButton(
            master=self,
            width=110,
            text="Джинн",
        )
        jinn.grid(row=2, column=0, padx=(20, 20), pady=10, sticky="nsew")

        mare = ctk.CTkButton(
            master=self,
            width=110,
            text="Мара",
        )
        mare.grid(row=2, column=1, padx=(20, 20), pady=10, sticky="nsew")

        revenant = ctk.CTkButton(
            master=self,
            width=110,
            text="Ревенант",
        )
        revenant.grid(row=2, column=2, padx=(20, 20), pady=10, sticky="nsew")

        shade = ctk.CTkButton(
            master=self,
            width=110,
            text="Тень",
        )
        shade.grid(row=2, column=3, padx=(20, 20), pady=10, sticky="nsew")

        demon = ctk.CTkButton(
            master=self,
            width=110,
            text="Демон",
        )
        demon.grid(row=2, column=4, padx=(20, 20), pady=10, sticky="nsew")

        yurei = ctk.CTkButton(
            master=self,
            width=110,
            text="Юрэй",
        )
        yurei.grid(row=3, column=0, padx=(20, 20), pady=10, sticky="nsew")

        oni = ctk.CTkButton(
            master=self,
            width=110,
            text="Они",
        )
        oni.grid(row=3, column=1, padx=(20, 20), pady=10, sticky="nsew")

        yokai = ctk.CTkButton(
            master=self,
            width=110,
            text="Ёкай",
        )
        yokai.grid(row=3, column=2, padx=(20, 20), pady=10, sticky="nsew")

        hantu = ctk.CTkButton(
            master=self,
            width=110,
            text="Ханту",
        )
        hantu.grid(row=3, column=3, padx=(20, 20), pady=10, sticky="nsew")

        goryo = ctk.CTkButton(
            master=self,
            width=110,
            text="Горё",
        )
        goryo.grid(row=3, column=4, padx=(20, 20), pady=10, sticky="nsew")

        myling = ctk.CTkButton(
            master=self,
            width=110,
            text="Мюлинг",
        )
        myling.grid(row=4, column=0, padx=(20, 20), pady=10, sticky="nsew")

        onryo = ctk.CTkButton(
            master=self,
            width=110,
            text="Онрё",
        )
        onryo.grid(row=4, column=1, padx=(20, 20), pady=10, sticky="nsew")

        theTwins = ctk.CTkButton(
            master=self,
            width=110,
            text="Близнецы",
        )
        theTwins.grid(row=4, column=2, padx=(20, 20), pady=10, sticky="nsew")

        raiju = ctk.CTkButton(
            master=self,
            width=110,
            text="Райдзю",
        )
        raiju.grid(row=4, column=3, padx=(20, 20), pady=10, sticky="nsew")

        obake = ctk.CTkButton(
            master=self,
            width=110,
            text="Обакэ",
        )
        obake.grid(row=4, column=4, padx=(20, 20), pady=10, sticky="nsew")

        theMimic = ctk.CTkButton(
            master=self,
            width=110,
            text="Мимик",
        )
        theMimic.grid(row=5, column=1, padx=(20, 20), pady=10, sticky="nsew")

        moroi = ctk.CTkButton(
            master=self,
            width=110,
            text="Морой",
        )
        moroi.grid(row=5, column=2, padx=(20, 20), pady=10, sticky="nsew")

        deogen = ctk.CTkButton(
            master=self,
            width=110,
            text="Деоген",
        )
        deogen.grid(row=5, column=3, padx=(20, 20), pady=10, sticky="nsew")

        thaye = ctk.CTkButton(
            master=self,
            width=110,
            text="Тайэ",
        )
        thaye.grid(row=5, column=4, padx=(20, 20), pady=10, sticky="nsew")

        spirit._command = lambda: get_ghost(spirit._text)
        wraith._command = lambda: get_ghost(wraith._text)
        phantom._command = lambda: get_ghost(phantom._text)
        poltergeist._command = lambda: get_ghost(poltergeist._text)
        banshee._command = lambda: get_ghost(banshee._text)
        jinn._command = lambda: get_ghost(jinn._text)
        mare._command = lambda: get_ghost(mare._text)
        revenant._command = lambda: get_ghost(revenant._text)
        shade._command = lambda: get_ghost(shade._text)
        demon._command = lambda: get_ghost(demon._text)
        yurei._command = lambda: get_ghost(yurei._text)
        oni._command = lambda: get_ghost(oni._text)
        yokai._command = lambda: get_ghost(yokai._text)
        hantu._command = lambda: get_ghost(hantu._text)
        goryo._command = lambda: get_ghost(goryo._text)
        myling._command = lambda: get_ghost(myling._text)
        onryo._command = lambda: get_ghost(onryo._text)
        theTwins._command = lambda: get_ghost(theTwins._text)
        raiju._command = lambda: get_ghost(raiju._text)
        obake._command = lambda: get_ghost(obake._text)
        theMimic._command = lambda: get_ghost(theMimic._text)
        moroi._command = lambda: get_ghost(moroi._text)
        deogen._command = lambda: get_ghost(deogen._text)
        thaye._command = lambda: get_ghost(thaye._text)
    
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
        for button in self.winfo_children()[1:]:
            self._update_button(button, button._text in possible_ghosts)

