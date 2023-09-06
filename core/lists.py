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

with open('core\evdsdict.json', encoding='utf-8') as json_file:
    evidences_dict = json.load(json_file)

class Ghosts_dict:
    with open('core\dict.json', encoding='utf-8') as json_file:
        ghosts_dict = json.load(json_file)

    evsd = []
        
    @staticmethod
    def reload():
        with open('core\dict.json', encoding='utf-8') as json_file:
            Ghosts_dict.ghosts_dict = json.load(json_file)

    @staticmethod
    def gd():
        return Ghosts_dict.ghosts_dict