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

import configparser
import os
import sys

class Config:
    def __init__(self):
        self.set_config_path()
        self.read_config()
            
    @property
    def config_path(self):
        return self._config_path + '\\config.ini'

    def set_config_path(self):
        self._config_path = ".\\config"
        if "C:\Program Files" in sys.path[0]:
            self._config_path = os.getenv('APPDATA') + '\\PhasmaHelper'
        if not os.path.exists(self._config_path):
            os.makedirs(self._config_path)
    
    def read_file(self):
        with open(self.config_path, "r") as config_file:
            config = configparser.ConfigParser()
            config.read_file(config_file)
            
            self.plain_text = bool(int(config.get('Default', 'plain_text')))
            self.appearance = config.get('Default', 'appearance')
            self.color_theme = config.get('Default', 'color_theme')
            self.ghosts_window_alpha = float(config.get('Default', 'ghosts_window_alpha'))
            self.cursed_items_window_alpha = float(config.get('Default', 'cursed_items_window_alpha'))
    
    def read_config(self):
        if not os.path.exists("./config/default_config.ini"):
            raise FileNotFoundError
        if not os.path.exists(self.config_path):
            os.system(f"copy .\config\default_config.ini {self.config_path}")
        try:
            self.read_file()
        except:
            raise FileNotFoundError(f"{self.config_path}")
            # os.system("copy .\config\default_config.ini .\config\config.ini")
            # self.read_file()
    
    # write to config file
    def save_config(self):
        with open(self.config_path, "w") as config_file:
            config = configparser.RawConfigParser()
            config.add_section('Default')
            config.set('Default', 'plain_text', int(self.plain_text))
            config.set('Default', 'appearance', self.appearance)
            config.set('Default', 'color_theme', self.color_theme)
            config.set('Default', 'ghosts_window_alpha', str(round(self.ghosts_window_alpha, 2)))
            config.set('Default', 'cursed_items_window_alpha', str(round(self.cursed_items_window_alpha, 2)))
            config.write(config_file)
            
            
cfg = Config()
