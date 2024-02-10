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
from core.utils import is_window_exists, read_data


class SettingWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Settings")
        self.after(250, lambda: self.iconbitmap('.\core\icons\logo.ico'))
        self.after(250, lambda: self.focus())

        self.settings_frame = ctk.CTkFrame(self)
        self.settings_frame.grid(row=0, column=0, columnspan=1, padx=(20, 20), pady=10, sticky="nsew")
        
        self.minimalistic_info_switch = ctk.CTkSwitch(
            master=self.settings_frame,
            command=lambda: self.change_is_minimalistic(),
            text="Minimalistic Info",
            )
        self.minimalistic_info_switch.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")
        self.minimalistic_info_switch.configure(
            state = "disabled"
        )
        
        self.label_ghosts_window_alpha = ctk.CTkLabel(
            master=self.settings_frame,
            text="Ghosts Window Alpha",
            )
        self.label_ghosts_window_alpha.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="nsew")
        
        self.label_cursed_items_window_alpha = ctk.CTkLabel(
            master=self.settings_frame,
            text="Cursed Items Window Alpha",
            )
        self.label_cursed_items_window_alpha.grid(row=3, column=0, padx=20, pady=(10, 0), sticky="nsew")
        
        self.ghosts_window_alpha_slider = ctk.CTkSlider(
            master = self.settings_frame,
            from_=0, 
            to=1, 
            command=self.change_ghosts_window_alpha
            )
        self.ghosts_window_alpha_slider.grid(
            row=2, 
            column=0, 
            padx=20, 
            pady=10, 
            sticky="nsew"
        )
        self.ghosts_window_alpha_slider.set(cfg.ghosts_window_alpha)
        
        self.cursed_items_window_alpha_slider = ctk.CTkSlider(
            master = self.settings_frame,
            from_=0, 
            to=1,
            command=self.change_cursed_items_window_alpha
            )
        self.cursed_items_window_alpha_slider.grid(
            row=4, 
            column=0, 
            padx=20, 
            pady=10, 
            sticky="nsew"
        )
        self.cursed_items_window_alpha_slider.set(cfg.cursed_items_window_alpha)
        
        self.language_button = ctk.CTkButton(
            master=self.settings_frame,
            text = f"Language: {cfg.language}"
        )
        self.language_button.grid(row=5, column=0, padx=20, pady=(10, 20), sticky="nsew")
        self.language_button._command = lambda: self.change_language(self.language_button)
        
        if cfg.plain_text:
            self.minimalistic_info_switch.select()
            
    def change_language(self, language_button):
        if "EN_en" in language_button.cget("text"):
            cfg.language = 'RU_ru'
        elif "RU_ru" in language_button.cget("text"):
            cfg.language = 'EN_en'
            
        read_data(cfg.language)
        language_button.configure(text = f"Language: {cfg.language}")
        self.master.master.ghosts_frame.draw_page()
    
    def change_is_minimalistic(self):
        cfg.plain_text = not cfg.plain_text
        
    def change_ghosts_window_alpha(self, value):
        cfg.ghosts_window_alpha = value
        for window in self.master.master.ghosts_windows:
            if is_window_exists(window):
                window.attributes('-alpha', cfg.ghosts_window_alpha)
        
        self.change_cursed_items_window_alpha(value)
        
    def change_cursed_items_window_alpha(self, value):
        cfg.cursed_items_window_alpha = value
        if is_window_exists(self.master.master.cursed_items_window):
            self.master.master.cursed_items_window.attributes('-alpha', cfg.cursed_items_window_alpha)
        