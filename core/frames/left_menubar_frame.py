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

from core.windows.setting_window import SettingWindow
from core.helpers import theme

class DifficultyButton(ctk.CTkButton):
    def __init__(
        self,
        master,
        command,
        text_color,
        width=40,
        height=30,
        text="•",
        font=("Arial", 30),
        fg_color=theme.fg_color_frame_dark,
        border_width = 0,
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            text=text,
            font=font,
            fg_color=fg_color,
            text_color=text_color,
            border_width=border_width,
            command=command
        )
        
    def get_item(self):
        return self.item


class LeftmenubarFrame(ctk.CTkFrame):
    def __init__(self, master, change_difficulty):
        super().__init__(master, corner_radius=0)

        self.change_difficulty = change_difficulty

        self.text_label = ctk.CTkLabel(master=self, text="Difficulty")
        self.text_label.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=10, sticky="nsew")

        self.settings_button = ctk.CTkButton(
            master=self,
            width=30,
            height=30,
            text="⚙️",
            anchor="w"
        )
        self.settings_button.place(relx=0.5, rely=0.93, anchor="center")
        self.settings_button.configure(command=self.open_settings)

        self._difficulty_buttons = []

        button_amauter_difficulty = DifficultyButton(
            master=self,
            fg_color=theme.fg_color_frame_dark_gray,
            text_color="#b0d8a4",
            border_width=1,
            command=lambda: self.change_difficulty(0)
        )
        button_amauter_difficulty.grid(row=1, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self._difficulty_buttons.append(button_amauter_difficulty)

        button_intermediate_difficulty = DifficultyButton(
            master=self,
            text_color="#fee191",
            command=lambda: self.change_difficulty(1)
        )
        button_intermediate_difficulty.grid(row=2, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self._difficulty_buttons.append(button_intermediate_difficulty)

        button_professional_difficulty = DifficultyButton(
            master=self,
            text_color="#fd8060",
            command=lambda: self.change_difficulty(2)
        )
        button_professional_difficulty.grid(row=3, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self._difficulty_buttons.append(button_professional_difficulty)

        button_nightmare_difficulty = DifficultyButton(
            master=self,
            text_color="#e84258",
            command=lambda: self.change_difficulty(3)
        )
        button_nightmare_difficulty.grid(row=4, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self._difficulty_buttons.append(button_nightmare_difficulty)
        
        button_insane_difficulty = DifficultyButton(
            master=self,
            text_color="#000000",
            command=lambda: self.change_difficulty(4)
        )
        button_insane_difficulty.grid(row=5, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self._difficulty_buttons.append(button_insane_difficulty)

        self.settings_window = None

    def get_difficulty_buttons(self):
        return self._difficulty_buttons
    
    def open_settings(self):
        if self.settings_window is None:
            self.settings_window = SettingWindow(self)  # create window if its None or destroyed
        elif not self.settings_window.winfo_exists():
            self.settings_window = SettingWindow(self)

        self.settings_window.focus()
        self.settings_window.attributes('-topmost', True)
        