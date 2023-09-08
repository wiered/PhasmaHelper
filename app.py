import json

import customtkinter as ctk

import frames
from core import lists

bg_color = "#1a1a1a"
bg_color_frame = "#212121"
button_fg_color = "#1f6aa4"
button_fg_color_light = "#298bd6"
button_fg_color_dark = "#0D2B43"

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

def configure_colors(appearance, color_theme):
    ctk.set_appearance_mode(appearance)  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme(color_theme)  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self, version):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        super().__init__()

        # configure window
        self.__version__ = version
        self.title(f"Phasma Helper v{self.__version__}")

        width = 1060
        height = 570

        screen_width = int((0.5 * self.winfo_screenwidth() - 0.5 * width) * 1.5)
        screen_height = int((0.4 * self.winfo_screenheight() - 0.5 * height) * 1.5)

        SCREEN_WIDTH = screen_width
        SCREEN_HEIGHT = screen_height

        self.geometry(f"{width}x{height}+{screen_width}+{screen_height}")
        self.iconbitmap("logo.ico")

        self.border_width = 0
        self.active_evidences = []
        
        self.difficulty = 0
        self.difficulties = ["Amauter", "Intermediate", "Professional", "Nightmare"]

        # Left menu bar
        self.left_menu_bar_frame = frames.LeftmenubarFrame(self, self.change_difficulty_event)
        self.left_menu_bar_frame.grid(
            row=1, column=0,
            padx=(0, 0), pady=(0, 0),
            rowspan=3,
            sticky="nsew",
        )
        self.difficulty_buttons = self.left_menu_bar_frame.difficulty_buttons

        # Spirits Frame
        self.ghosts_frame = frames.GhostsFrame(self, self.show_info_window)
        self.ghosts_frame.grid(row=1, column=2, padx=(0, 20), pady=(20, 0), sticky="nsew")
        self.spirts_buttons = self.ghosts_frame._spirts_buttons

        # Evidences Frame
        self.evidenced_frame = frames.EvidencesFrame(self, self.disable_spirits)
        self.evidenced_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Tools Frame
        self.tools_frame = frames.ToolsFrame(self)
        self.tools_frame.grid(row=2, column=1, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Difficulty and version lables
        self.label_difficulty = ctk.CTkLabel(master=self, text=f"Difficulty: Amauter")
        self.label_difficulty.grid(row=3, column=1, columnspan=1, padx=(30, 30), pady=10, sticky="w")

        self.label_version = ctk.CTkLabel(master=self, text=f"Version {self.__version__}")
        self.label_version.grid(row=3, column=2, columnspan=1, padx=(10, 30), pady=10, sticky="e")
        

    def disable_spirits(self, evidence, state):
        with open('core\evdsdict.json', encoding='utf-8') as json_file:
            evidences_dict = json.load(json_file)

        if state == 1:
            self.active_evidences.append(evidence)
        else:
            self.active_evidences.remove(evidence)

        ghosts = lists.ghosts
        for evidence in self.active_evidences:
            ghosts = [ghost for ghost in ghosts if ghost in evidences_dict.get(evidence)]

        for button in self.spirts_buttons:
            if button._text in ghosts:
                button.configure(state="normal")
                button.configure(fg_color=button_fg_color)
            else:
                button.configure(state="disabled")
                button.configure(fg_color=button_fg_color_dark)


    def change_difficulty_event(self, difficulty):
        self.difficulty_buttons[self.difficulty].configure(border_width=0)
        self.difficulty = difficulty
        self.difficulty_buttons[self.difficulty].configure(border_width=1)
        self.label_difficulty.configure(text=f"Difficulty: {self.difficulties[self.difficulty]}")

    
    def show_info_window(self, name):
        self.info = frames.InfoWindow(name)
        self.info.attributes('-topmost', True)
        self.info.update()
        self.info.mainloop()

