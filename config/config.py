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

class Config:
    def __init__(self):
        self.read_config()

    def read_config(self):
        if not os.path.exists("./config/default_config.ini"):
            raise FileNotFoundError
        if not os.path.exists("./config/config.ini"):
            os.system("copy .\config\default_config.ini .\config\config.ini")
        with open("./config/config.ini", "r") as config_file:
            config = configparser.ConfigParser()
            config.read_file(config_file)
            
            self.plain_text = bool(int(config.get('DEFAULT', 'plain_text')))
            self.appearance = config.get('DEFAULT', 'appearance')
            self.color_theme = config.get('DEFAULT', 'color_theme')

cfg = Config()
