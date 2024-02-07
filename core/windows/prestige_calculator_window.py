import json

import customtkinter as ctk

class EntyrFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.player_level_entry = ctk.CTkEntry(self, placeholder_text="Your level")
        self.player_level_entry.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.average_gain_entry = ctk.CTkEntry(self, placeholder_text="Average gain per game")
        self.average_gain_entry.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="w")

    def get(self):
        try:
            player_level = int(self.player_level_entry.get())
            average_gain = int(self.average_gain_entry.get())
        except:
            player_level = 1
            average_gain = 1000

        if player_level < 1 or player_level > 100:
            player_level = 1
        if average_gain < 0:
            average_gain = 1000
        
        return player_level, average_gain


class ResultsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
                
        msg = f"""You need _______ xp to prestige, it's ~___ games"""

        self.label = ctk.CTkLabel(self, text="CTkLabel", fg_color="transparent")
        self.label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsw")
        self.label.configure(text=msg)

    def set(self, text):
        self.label.configure(text=text)


class PrestigeCalculatorWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        

        self.title("Phasma Helper - Prestige Calculator")
        self.after(250, lambda: self.iconbitmap('.\core\icons\logo.ico'))
        self.after(250, lambda: self.focus())
        
        self.geometry(f"+{int(self.winfo_screenwidth()*0.5)}+{int(self.winfo_screenheight()*0.5)}")
        
        self.entry_frame = EntyrFrame(self)
        self.entry_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.result_frame = ResultsFrame(self)
        self.result_frame.grid(row=0, column=1, rowspan = 2, padx=10, pady=(10, 10), sticky="nsw")
        
        self.button = ctk.CTkButton(self, text="Calculate", command=self.button_callback)
        self.button.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="ew")
        
        with open('.\core\data\prestige.json', encoding='utf-8') as json_file:
            prestige_data = json.load(json_file).get("data")
            self.levels = prestige_data[::3]
            self.xp_for_level = prestige_data[1::3]
            self.total_xp = prestige_data[2::3]
            
    def button_callback(self):
        player_level, average_gain = self.entry_frame.get()
        xp_needed, games = self.calculate_xp_needed(player_level, average_gain)

        msg = f"""You need {xp_needed} xp to prestige, it's ~{games} games"""

        self.result_frame.set(msg)
            
    def calculate_xp_needed(self, player_level, average_gain):
        max_xp_needed = self.total_xp[100-1]
        xp_now = self.total_xp[player_level-1]
        
        return max_xp_needed-xp_now, int((max_xp_needed-xp_now)/average_gain)+1
            
