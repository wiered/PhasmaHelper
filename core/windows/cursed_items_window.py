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
from PIL import Image

from core.utils import lists, themes

OUIJI_BOARD_ICON = "./core/icons/ouija.png"
PLAYING_CARDS_ICON = "./core/icons/cards.png"
VOODO_DOLL_ICON = "./core/icons/voodoo.png"
MUSIC_BOX_ICON = "./core/icons/musicbox.png"
SUMMONING_CIRCLE_ICON = "./core/icons/pentacle.png"
HAUNTED_MIRROR_ICON = "./core/icons/mirror.png"
MONKEY_PAW_ICON = "./core/icons/paw.png"

class ImageFrame(ctk.CTkFrame):
    def __init__(
        self, 
        master, 
        width: int = 200, 
        height: int = 200, 
        image_file="./core/images/playing_cards.png", 
        text = "Карты Таро"
        ):
        super().__init__(master, width, height)
        
        image = ctk.CTkImage(
            light_image=Image.open(image_file),
            dark_image=Image.open(image_file),
            size=(669/3, 619/3),
        )
        self.image_label = ctk.CTkLabel(
            master=self,
            width=669/3,
            height=619/3,
            anchor="w",
            text="",
            image=image,
        )
        self.image_label.grid(
            row=0, column=0,
            padx=(5, 5), pady=(5, 5),
            sticky="nsew",
        )
        
        self.image_title = ctk.CTkLabel(
            master=self,
            text=text,
        )
        self.image_title.grid(
            row=1, column=0,
            padx=(5, 5), pady=(5, 5),
            sticky="nsew",
        )
        
    def set_text(self, text):
        self.image_title.configure(text=text)
        
    def set_image(self, image_file):
        image = ctk.CTkImage(
            light_image=Image.open(image_file),
            dark_image=Image.open(image_file),
            size=(669/3, 619/3),
        )
        self.image_label.configure(image = image)


class ItemButton(ctk.CTkButton):
    def __init__(
        self,
        master,
        image,
        item,
        width: int = 40,
        height: int = 40,
        anchor: str ="w",
        text: str ="",
    ):
        super().__init__(master, width=width, height=height, anchor=anchor, text=text, image=image)
        
        self.item = item
        
    def get_item(self):
        return self.item

    
class CursedItemsLeftMenubarFrame(ctk.CTkFrame):
    def __init__(self, master, change_item):
        super().__init__(master, corner_radius=0)

        self.change_item = change_item

        #ouija board button
        ouija_board_icon = ctk.CTkImage(
            light_image=Image.open(OUIJI_BOARD_ICON),
            dark_image=Image.open(OUIJI_BOARD_ICON),
            size=(30, 30)
        )
        self.ouija_borad_button = ItemButton(
            master=self,
            image=ouija_board_icon,
            item="ouija_board",
        )
        self.ouija_borad_button.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.ouija_borad_button._command = lambda: self.change_item("ouija_board")
        
        #write cards_button
        playing_cards_icon = ctk.CTkImage(
            light_image=Image.open(PLAYING_CARDS_ICON),
            dark_image=Image.open(PLAYING_CARDS_ICON),
            size=(30, 30)
        )
        self.playing_cards_button = ItemButton(
            master=self,
            image=playing_cards_icon,
            item = "playing_cards"
        )
        self.playing_cards_button.grid(
            row=2, 
            column=0, 
            columnspan=1, 
            padx=(5, 5), 
            pady=(5, 5), 
            sticky="w"
        )
        self.playing_cards_button._command = lambda: self.change_item("playing_cards")
        
        #write voodoo_doll_button
        voodoo_doll_icon = ctk.CTkImage(
            light_image=Image.open(VOODO_DOLL_ICON),
            dark_image=Image.open(VOODO_DOLL_ICON),
            size=(30, 30)
        )
        self.voodoo_doll_button = ItemButton(
            master=self,
            item="voodoo_doll",
            image=voodoo_doll_icon
        )
        self.voodoo_doll_button.grid(
            row=3, 
            column=0, 
            columnspan=1, 
            padx=(5, 5), 
            pady=(5, 5), 
            sticky="w"
        )
        self.voodoo_doll_button._command = lambda: self.change_item("voodoo_doll")
        
        #write music_box_button
        music_box_icon = ctk.CTkImage(
            light_image=Image.open(MUSIC_BOX_ICON),
            dark_image=Image.open(MUSIC_BOX_ICON),
            size=(30, 30)
        )
        self.music_box_button = ItemButton(
            master=self,
            image=music_box_icon,
            item="music_box",
        )
        self.music_box_button.grid(
            row=4, 
            column=0, 
            columnspan=1, 
            padx=(5, 5), 
            pady=(5, 5), 
            sticky="w"
        )
        self.music_box_button._command = lambda: self.change_item("music_box")
        
        #write summoning_circle_button
        summoning_circle_icon = ctk.CTkImage(
            light_image=Image.open(SUMMONING_CIRCLE_ICON),
            dark_image=Image.open(SUMMONING_CIRCLE_ICON),
            size=(30, 30)
        )
        self.summoning_circle_button = ItemButton(
            master=self,
            item="summoning_circle",
            image=summoning_circle_icon
        )
        self.summoning_circle_button.grid(
            row=5, 
            column=0, 
            columnspan=1, 
            padx=(5, 5), 
            pady=(5, 5), 
            sticky="w"
        )
        self.summoning_circle_button._command = lambda: self.change_item("summoning_circle")
        
        #write haunted_mirror_button
        haunted_mirror_icon = ctk.CTkImage(
            light_image=Image.open(HAUNTED_MIRROR_ICON),
            dark_image=Image.open(HAUNTED_MIRROR_ICON),
            size=(30, 30)
        )
        self.haunted_mirror_button = ItemButton(
            master=self,
            item="haunted_mirror",
            image=haunted_mirror_icon
        )
        self.haunted_mirror_button.grid(
            row=6, 
            column=0, 
            columnspan=1, 
            padx=(5, 5), 
            pady=(5, 5), 
            sticky="w"
        )
        self.haunted_mirror_button._command = lambda: self.change_item("haunted_mirror")
        
        #write monkey_paw_button
        monkey_paw_icon = ctk.CTkImage(
            light_image=Image.open(MONKEY_PAW_ICON),
            dark_image=Image.open(MONKEY_PAW_ICON),
            size=(30, 30)
        )
        self.monkey_paw_button = ItemButton(
            master=self,
            image=monkey_paw_icon,
            item="monkey_paw"
        )
        self.monkey_paw_button.grid(
            row=7, 
            column=0, 
            columnspan=1, 
            padx=(5, 5), 
            pady=(5, 5), 
            sticky="w"
        )
        self.monkey_paw_button._command = lambda: self.change_item("monkey_paw")
        

class CursedItemsWindow(ctk.CTkToplevel):
    def __init__(self, item):
        super().__init__()
        
        # setting up titlebar
        self.title(f"Phasma Helper - Cursed Items")
        self.after(250, lambda: self.iconbitmap('.\core\icons\logo.ico'))

        # setting up window geometry
        width = 1070
        height = 390
        screen_width = int((0.5 * self.winfo_screenwidth() - 0.5 * width) * 1.5)
        screen_height = int((0.4 * self.winfo_screenheight() - 0.5 * height) * 1.5)
        self.geometry(f"{width}x{height}+{screen_width}+{screen_height}")
        self.resizable(False, False)
        
        # setting up variables
        with open('core\data\cursed_items.json', encoding='utf-8') as json_file:
            self.cursed_items_dict = json.load(json_file)
        
        self.left_menu_bar_frame = CursedItemsLeftMenubarFrame(self, self.change_item)
        self.left_menu_bar_frame.grid(
            row=0, column=0,
            padx=(0, 0), pady=(0, 0),
            rowspan=2,
            sticky="nsew",
        )
        
        # Image and Title
        self.image_frame = ImageFrame(
            master=self,
            width=669/3,
            height=619/3,
            )
        self.image_frame.grid(
            row=0, column=1,
            padx=(10, 5), pady=(10, 5),
            sticky="nsew",
        ) 
        
        # Short Description of Item
        self.description_frame = ctk.CTkFrame(
            master=self,
        )
        self.description_frame.grid(
            row=1, column=1,
            padx=(10, 5), pady=(5, 10),
            sticky="nsew",
        )
        self.item_description_label = ctk.CTkLabel(
            master = self.description_frame,
            anchor="center"
        )
        self.item_description_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 5))
        
        # Description of Item
        self.main_frame = ctk.CTkFrame(
            master=self,
        )
        self.main_frame.grid(
            row=0, column=2,
            rowspan=2,
            padx=(5, 10), pady=(10, 10),
            sticky="nsew",
        )
        
        self.main_label = ctk.CTkLabel(
            master = self.main_frame,
            justify="left",
            anchor="w",
        )
        self.main_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 5))
    
        self.change_item(item)
    
    def change_item(self, item):
        self.item = item
        self.image = f"./core/images/{item}.png"
        self.item_title = self.cursed_items_dict.get(item).get("title")
        self.short_description = self.cursed_items_dict.get(item).get("short_description")
        self.description = self.cursed_items_dict.get(item).get("description")
        self.description_additional = self.cursed_items_dict.get(item).get("description_additional")
        
        self.short_description = textwrap.fill(self.short_description, width=31)
        if (self.description_additional):
            self.description += "\n\n" + self.description_additional
            
        self.image_frame.set_text(self.item_title)
        self.image_frame.set_image(self.image)
        self.item_description_label.configure(text = self.short_description)
        self.main_label.configure(text=self.description)
        
        for button in self.left_menu_bar_frame.winfo_children():
            if button.item == item:
                button.configure(fg_color=themes.button_fg_color)
            else:
                button.configure(fg_color=themes.button_fg_color_dark)
