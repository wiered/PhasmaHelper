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

import json
from typing import Any

ghosts = [
    "Дух",
    "Мираж",
    "Фантом",
    "Полтергейст",
    "Банши",
    "Джинн",
    "Мара",
    "Ревенант",
    "Тень",
    "Демон",
    "Юрэй",
    "Они",
    "Ёкай",
    "Ханту",
    "Горё",
    "Мюлинг",
    "Онрё",
    "Близнецы",
    "Райдзю",
    "Обакэ",
    "Мимик",
    "Морой",
    "Деоген",
    "Тайэ"
]

evidences = [
    "EMF",
    "Spirit Box",
    "Fingerprints",
    "Ghost Orb",
    "Ghost Writing",
    "Freezing Temp",
    "DOTS"
]

tabs = [
    "behavior",
    "evidences",
    "advantages",
    "strategy"
]

with open('core\data\evdsdict.json', encoding='utf-8') as json_file:
    ghosts_by_evidences = json.load(json_file)

class Ghosts_dict:
    def __init__(self):
        with open('core\data\dict.json', encoding='utf-8') as json_file:
            self._dict = json.load(json_file)
    

    @property
    def dict(self):
        return self._dict
    

    @dict.setter
    def dict(self, value):
        return
    

    def reload(self):
        with open('core\data\dict.json', encoding='utf-8') as json_file:
            self._dict = json.load(json_file)


    def get(self, value):
        return self._dict.get(value)