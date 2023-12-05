import customtkinter as ctk
from PIL import Image

MAP_ICON = "./core/icons/map.png"

class ToolsFrame(ctk.CTkFrame):
    def __init__(self, master, width):
        super().__init__(master, width=width)
        
        self.label_tools = ctk.CTkLabel(master=self, text="Tools (WIP)")
        self.label_tools.grid(
            row=0, 
            column=0, 
            columnspan=1,
            padx=(30, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        
        map_icon = ctk.CTkImage(
            light_image=Image.open(MAP_ICON),
            dark_image=Image.open(MAP_ICON),
            size=(30, 30)
        )
        self.map_button = ctk.CTkButton(
            master=self,
            width=150,
            height=30,
            anchor="w",
            text="Maps",
            image=map_icon
        )
        self.map_button.grid(
            row=1, 
            column=0, 
            columnspan=1, 
            padx=(20, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        