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

from config import cfg

class SettingWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Settings")
        self.after(250, lambda: self.iconbitmap('.\core\data\logo.ico'))

        self.settings_frame = SettingsFrame(self)
        self.settings_frame.grid(row=0, column=0, columnspan=1, padx=(20, 20), pady=10, sticky="nsew")


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.minimalistic_info_switch = ctk.CTkSwitch(
            master=self,
            command=lambda: self.change_is_minimalistic(),
            text="Minimalistic Info",
            )
        self.minimalistic_info_switch.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")

        if cfg.is_minimalistic:
            self.minimalistic_info_switch.select()


    def change_is_minimalistic(self):
        cfg.is_minimalistic = not cfg.is_minimalistic
        