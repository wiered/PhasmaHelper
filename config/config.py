import configparser
import os

class Config:
    def __init__(self):
        self.read_config()


    @staticmethod
    def get_config(_key: str, selection: str = 'DEFAULT'):
        if not os.path.exists("./config/default_config.ini"):
            raise FileNotFoundError
        if not os.path.exists("./config/config.ini"):
            os.system("cp .\config\default_config.ini .\config\config.ini")
        with open("./config/config.ini", "r") as config_file:
            config = configparser.ConfigParser()
            config.read_file(config_file)
            return config.get(selection, _key)


    def read_config(self):
        if not os.path.exists("./config/default_config.ini"):
            raise FileNotFoundError
        if not os.path.exists("./config/config.ini"):
            os.system("cp .\config\default_config.ini .\config\config.ini")
        with open("./config/config.ini", "r") as config_file:
            config = configparser.ConfigParser()
            config.read_file(config_file)
            self.minimalistic_info = bool(int(config.get('DEFAULT', 'minimalistic_info')))
            self.appearance = config.get('DEFAULT', 'appearance')
            self.color_theme = config.get('DEFAULT', 'color_theme')

cfg = Config()
