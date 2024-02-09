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

import textwrap
import json

import customtkinter as ctk

from core.utils import lists, get_more
from config import cfg

BORDER_WIDTH = 0


class GhostInfoWindow(ctk.CTk):
    def __init__(self, master, name):
        super().__init__()
        
        self.master = master
        

        self.title("Phasma Helper: %s" % name)
        self.iconbitmap(".\core\icons\logo.ico")
        self.geometry(f"+{int(self.winfo_screenwidth()*0.8)}+{int(self.winfo_screenheight()*0.8)}")
        
        with open('.\core\data\ghosts.json', encoding='utf-8') as json_file:
            self.ghosts_dict = json.load(json_file)
        
        if cfg.plain_text:
            general_text = self.get_ghost_info(name)
            self.text_label = ctk.CTkLabel(master=self, text=general_text)
            self.text_label.grid(row=0, column=0, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")

        else:
            self.menu = TabviewFrame(master=self, name=name)
            self.menu.grid(row=1, column=0, columnspan=1, padx=(5, 5), pady=10, sticky="nsew") 
    
    def _get_ghost_data(self, name):
            return self.ghosts_dict.get(name)
    
    def get_ghost_info(self, name):
        ghost_data = get_more(name)

        behavior_text = textwrap.fill(ghost_data.get("behavior"), width=100)
        evidences_text = "; ".join(ghost_data.get("behavior"))
        advantages_text = textwrap.fill(ghost_data.get("behavior"), width=100)
        strategy_text = textwrap.fill(ghost_data.get("behavior"), width=100)

        general_text = ""
        general_text += f"=================== {name} ====================\n"
        general_text += behavior_text
        general_text += "\n===================   Улики   ====================\n"
        general_text += evidences_text
        general_text += "\n=================== Слабости  ====================\n"
        general_text += advantages_text
        general_text += "\n=================== Стратегия ====================\n"
        general_text += strategy_text
        
        return general_text
    
    def quit(self) -> None:
        self.master.remove_ghost_window(self)
        return super().quit()
    
    def destroy(self):
        self.master.remove_ghost_window(self)
        return super().destroy()


class TabviewFrame(ctk.CTkTabview):
    def __init__(self, master, name):
        super().__init__(master, height=100)
        
        with open('.\core\data\ghosts\EN_en.json', encoding='utf-8') as json_file:
            self.ghosts_dict = json.load(json_file)
        
        name = name
        
        self.add("Behavior")
        # self.add("Advantages")
        # self.add("Strategy")
        
        ghost_data = get_more(name)
            
        evidences_text = "; ".join(ghost_data.get("evidences"))
        
        # behavior tab
        
        behavior_text = evidences_text + "\n\n" + "\n".join(ghost_data.get("behavior"))
        
        self.behavior_label = ctk.CTkLabel(master=self.tab("Behavior"), text=behavior_text)
        self.behavior_label.grid(row=0, column=0, padx=20, pady=10)
        
        # # set advantages tab
        # advantages_text = evidences_text + "\n\n" + "\n".join(ghost_data.get("behavior"))
        
        # self.advantages_label = ctk.CTkLabel(master=self.tab("Advantages"), text=advantages_text)
        # self.advantages_label.grid(row=0, column=0, padx=20, pady=10)
        
        # # set strategy tab
        # strategy_text = evidences_text + "\n\n" + "\n".join(ghost_data.get("behavior"))
        
        # self.strategy_label = ctk.CTkLabel(master=self.tab("Strategy"), text=strategy_text)
        # self.strategy_label.grid(row=0, column=0, padx=20, pady=10)
        
        del ghost_data
    
    def _get_ghost_data(self, name):
            return self.ghosts_dict.get(name)
        
        
class TextFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.text = ctk.CTkLabel(master=self, text=f"sample")
        self.text.grid(row=0, column=0, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")

    def set_text(self, text):
        self.text.configure(text=text)
        
