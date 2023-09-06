import textwrap

import customtkinter

from core import lists

class InfoWindow(customtkinter.CTk):
    def __init__(self, name):
        super().__init__()

        self.get_ghost_info(name)

        self.title("Phasma Helper: %s" % name)
        self.iconbitmap("logo.ico")

        self.text_label = customtkinter.CTkLabel(master=self, text=self.general_text)
        self.text_label.grid(row=0, column=0, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")

        # self.text = TextFrame(self)
        # self.text.grid(row=0, column=1, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")

        # self.menu = MenuFrame(self, name, self.text.set_text)
        # self.menu.grid(row=0, column=0, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")
        # self.text.set_text(self.menu.behavior_text)


    def get_ghost_info(self, name):
        self.behavior_text = lists.Ghosts_dict.gd().get(name).get("behavior")
        self.evidences_text = lists.Ghosts_dict.gd().get(name).get("evidences")
        self.advantages_text = lists.Ghosts_dict.gd().get(name).get("advantages")
        self.strategy_text = lists.Ghosts_dict.gd().get(name).get("strategy")

        self.behavior_text = textwrap.fill(self.behavior_text, width=100)
        self.advantages_text = textwrap.fill(self.advantages_text, width=100)
        self.strategy_text = textwrap.fill(self.strategy_text, width=100)

        self.general_text = ""
        self.general_text += f"=================== {name} ====================\n"
        self.general_text += self.behavior_text
        self.general_text += "\n===================   Улики   ====================\n"
        self.general_text += "; ".join(self.evidences_text)
        self.general_text += "\n=================== Слабости  ====================\n"
        self.general_text += self.advantages_text
        self.general_text += "\n=================== Стратегия ====================\n"
        self.general_text += self.strategy_text

class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, name, set_text):
        super().__init__(master)

        self.get_ghost_info(name)

        generally = customtkinter.CTkButton(
            master=self,
            width=110,
            text="Generally",
        )
        generally.grid(row=0, column=0, padx=(20, 20), pady=10, sticky="w")
        generally._command = lambda: set_text(self.general_text)

        behavior = customtkinter.CTkButton(
            master=self,
            width=110,
            text="Behavior",
        )
        behavior.grid(row=1, column=0, padx=(20, 20), pady=10, sticky="w")
        behavior._command = lambda: set_text(self.behavior_text)

        evidences = customtkinter.CTkButton(
            master=self,
            width=110,
            text="Evidences",
        )
        evidences.grid(row=2, column=0, padx=(20, 20), pady=10, sticky="w")
        evidences._command = lambda: set_text(self.evidences_text)

        advantages = customtkinter.CTkButton(
            master=self,
            width=110,
            text="Advantages",
        )
        advantages.grid(row=3, column=0, padx=(20, 20), pady=10, sticky="w")
        advantages._command = lambda: set_text(self.advantages_text)

        strategy = customtkinter.CTkButton(
            master=self,
            width=110,
            text="Strategy",
        )
        strategy.grid(row=4, column=0, padx=(20, 20), pady=10, sticky="w")
        strategy._command = lambda: set_text(self.strategy_text)

    
    def get_ghost_info(self, name):
        self.behavior_text = lists.Ghosts_dict.gd().get(name).get("behavior")
        self.evidences_text = lists.Ghosts_dict.gd().get(name).get("evidences")
        self.advantages_text = lists.Ghosts_dict.gd().get(name).get("advantages")
        self.strategy_text = lists.Ghosts_dict.gd().get(name).get("strategy")

        self.behavior_text = textwrap.fill(self.behavior_text, width=100)
        self.advantages_text = textwrap.fill(self.advantages_text, width=100)
        self.strategy_text = textwrap.fill(self.strategy_text, width=100)

        self.general_text = ""
        self.general_text += f"=================== {name} ====================\n"
        self.general_text += self.behavior_text
        self.general_text += "\n===================   Улики   ====================\n"
        self.general_text += "; ".join(self.evidences_text)
        self.general_text += "\n=================== Слабости  ====================\n"
        self.general_text += self.advantages_text
        self.general_text += "\n=================== Стратегия ====================\n"
        self.general_text += self.strategy_text

class TextFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.text = customtkinter.CTkLabel(master=self, text=f"sample")
        self.text.grid(row=0, column=0, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")


    def set_text(self, text):
        self.text.configure(text=text)

    