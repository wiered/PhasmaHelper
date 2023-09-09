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

import time

import customtkinter as ctk

from config import cfg

def change_info_appearance():
    cfg.minimalistic_info = not cfg.minimalistic_info

class TimerWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Settings")
        self.after(250, lambda: self.iconbitmap('logo.ico'))

        self.time_frame = TimeFrame(self)
        self.time_frame.grid(row=0, column=0, columnspan=1, padx=(20, 20), pady=10, sticky="nsew")

        c = 0

        while True:
            self.time_frame.set_text(c)
            time.sleep(1)


class TimeFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.text_label = ctk.CTkLabel(master=self, text="0")
        self.text_label.grid(row=0, column=0, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")

    def set_text(self, text):
        self.text_label.configure(text=text)
