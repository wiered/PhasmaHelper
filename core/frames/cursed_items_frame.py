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

import customtkinter as ctk
from PIL import Image

from ..widgets import CursedItemButton

OUIJI_BOARD_ICON = "./core/icons/ouija.png"
PLAYING_CARDS_ICON = "./core/icons/cards.png"
VOODO_DOLL_ICON = "./core/icons/voodoo.png"
MUSIC_BOX_ICON = "./core/icons/musicbox.png"
SUMMONING_CIRCLE_ICON = "./core/icons/pentacle.png"
HAUNTED_MIRROR_ICON = "./core/icons/mirror.png"
MONKEY_PAW_ICON = "./core/icons/paw.png"

class CursedItemsFrame(ctk.CTkFrame):
    def __init__(self, master, width, create_cursed_items_window):
        super().__init__(master, width=width)
        
        self.label_tools = ctk.CTkLabel(master=self, text="Cursed Items")
        self.label_tools.grid(
            row=0, 
            column=0, 
            columnspan=1,
            padx=(30, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        
        ouija_board_icon = ctk.CTkImage(
            light_image=Image.open(OUIJI_BOARD_ICON),
            dark_image=Image.open(OUIJI_BOARD_ICON),
            size=(30, 30)
        )
        self.ouija_borad_button = CursedItemButton(
            master=self,
            width=150,
            height=30,
            anchor="w",
            text="Ouija board",
            image=ouija_board_icon,
            item="ouija_board"
        )
        self.ouija_borad_button.grid(
            row=1, 
            column=0, 
            columnspan=1, 
            padx=(20, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        self.ouija_borad_button._command = lambda: create_cursed_items_window("ouija_board")
            
        cards_icon= ctk.CTkImage(
            light_image=Image.open(PLAYING_CARDS_ICON),
            dark_image=Image.open(PLAYING_CARDS_ICON),
            size=(30, 30)
        )
        self.cards_button = CursedItemButton(
            master=self,
            width=160,
            height=30,
            anchor="w",
            text="Playing cards",
            image=cards_icon
        )
        self.cards_button.grid(
            row=1, 
            column=1, 
            columnspan=1, 
            padx=(10, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        self.cards_button._command = lambda: create_cursed_items_window("playing_cards")
        
        voodoo_doll_icon = ctk.CTkImage(
            light_image=Image.open(VOODO_DOLL_ICON),
            dark_image=Image.open(VOODO_DOLL_ICON),
            size=(30, 30)
        )
        self.voodoo_doll_button = CursedItemButton(
            master=self,
            width=150,
            height=30,
            anchor="w",
            text="Voodoo doll",
            image=voodoo_doll_icon
        )
        self.voodoo_doll_button.grid(
            row=1, 
            column=2, 
            columnspan=1, 
            padx=(10, 20), 
            pady=(10, 0), 
            sticky="w"
        )
        self.voodoo_doll_button._command = lambda: create_cursed_items_window("voodoo_doll")
        
        music_box_icon = ctk.CTkImage(
            light_image=Image.open(MUSIC_BOX_ICON),
            dark_image=Image.open(MUSIC_BOX_ICON),
            size=(30, 30)
        )
        self.music_box_button = CursedItemButton(
            master=self,
            width=150,
            height=30,
            anchor="w",
            text="Music box",
            image=music_box_icon
        )
        self.music_box_button.grid(
            row=2, 
            column=0, 
            columnspan=1, 
            padx=(20, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        self.music_box_button._command = lambda: create_cursed_items_window("music_box")
        
        summoning_circle_icon = ctk.CTkImage(
            light_image=Image.open(SUMMONING_CIRCLE_ICON),
            dark_image=Image.open(SUMMONING_CIRCLE_ICON),
            size=(30, 30)
        )
        self.summoning_circle_button = CursedItemButton(
            master=self,
            width=160,
            height=30,
            anchor="w",
            text="Summoning circle",
            image=summoning_circle_icon
        )
        self.summoning_circle_button.grid(
            row=2, 
            column=1, 
            columnspan=1, 
            padx=(10, 10), 
            pady=(10, 0), 
            sticky="w"
        )
        self.summoning_circle_button._command = lambda: create_cursed_items_window("summoning_circle")
        
        haunted_mirror_icon = ctk.CTkImage(
            light_image=Image.open(HAUNTED_MIRROR_ICON),
            dark_image=Image.open(HAUNTED_MIRROR_ICON),
            size=(30, 30)
        )
        self.haunted_mirror_button = CursedItemButton(
            master=self,
            width=150,
            height=30,
            anchor="w",
            text="Haunted mirror",
            image=haunted_mirror_icon,
            item="haunted_mirror"
        )
        self.haunted_mirror_button.grid(
            row=2, 
            column=2, 
            columnspan=1, 
            padx=(10, 20), 
            pady=(10, 0), 
            sticky="w"
        )
        self.haunted_mirror_button._command = lambda: create_cursed_items_window("haunted_mirror")
        
        monkey_paw_icon = ctk.CTkImage(
            light_image=Image.open(MONKEY_PAW_ICON),
            dark_image=Image.open(MONKEY_PAW_ICON),
            size=(30, 30)
        )
        self.monkey_paw_button = CursedItemButton(
            master=self,
            width=160,
            height=30,
            anchor="w",
            text="Monkey paw",
            image=monkey_paw_icon,
            item="monkey_paw"
        )
        self.monkey_paw_button.grid(
            row=3, 
            column=1, 
            columnspan=1, 
            padx=(10, 10), 
            pady=(10, 10), 
            sticky="w",
        )
        self.monkey_paw_button._command = lambda: create_cursed_items_window("monkey_paw")
        