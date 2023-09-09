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

class ToolsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_tools = ctk.CTkLabel(master=self, text="TOOLS (WIP)")
        self.label_tools.grid(row=1, column=1, columnspan=1, padx=(30, 10), pady=(10, 0), sticky="w")

        self.label_tools_smudge_stick = ctk.CTkLabel(master=self,
                                                               text="Start smudge stick timer (60 seconds) - Ctrl+B")
        self.label_tools_smudge_stick.grid(row=2, column=1, columnspan=1, padx=(20, 0), pady=0, sticky="w")

        self.label_tools_attack = ctk.CTkLabel(master=self, text="Start attack timer - Ctrl+Q")
        self.label_tools_attack.grid(row=3, column=1, columnspan=1, padx=(20, 0), pady=0, sticky="w")

        self.label_tools_difficulty = ctk.CTkLabel(master=self, text="Change difficulty - Ctrl+P")
        self.label_tools_difficulty.grid(row=4, column=1, columnspan=1, padx=(20, 0), pady=(0, 10), sticky="w")

