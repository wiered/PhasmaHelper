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

with open('core\evdsdict.json', encoding='utf-8') as json_file:
    evidences_dict = json.load(json_file)

class Ghosts_dict:
    def __init__(self):
        with open('core\dict.json', encoding='utf-8') as json_file:
            self._dict = json.load(json_file)
    

    @property
    def dict(self):
        return self._dict
    

    @dict.setter
    def dict(self, value):
        return
    

    def reload(self):
        with open('core\dict.json', encoding='utf-8') as json_file:
            self._dict = json.load(json_file)


    def get(self, value):
        return self._dict.get(value)