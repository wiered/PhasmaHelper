import tkinter
from typing import Any, Callable, Optional, Tuple, Union
import customtkinter as ctk
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage

class EvidenceSwitch(ctk.CTkSwitch):
    def __init__(
        self,
        master: any, 
        width: int = 100, 
        height: int = 24, 
        switch_width: int = 36, 
        switch_height: int = 18, 
        corner_radius: int | None = None, 
        border_width: int | None = None, 
        button_length: int | None = None, 
        bg_color: str | Tuple[str, str] = "transparent", 
        fg_color: str | Tuple[str, str] | None = None, 
        border_color: str | Tuple[str, str] = "transparent", 
        progress_color: str | Tuple[str, str] | None = None, 
        button_color: str | Tuple[str, str] | None = None, 
        button_hover_color: str | Tuple[str, str] | None = None, 
        text_color: str | Tuple[str, str] | None = None, 
        text_color_disabled: str | Tuple[str, str] | None = None, 
        text: str = "CTkSwitch", 
        font: tuple | CTkFont | None = None, 
        textvariable: tkinter.Variable | None = None, 
        onvalue: int | str = 1, 
        offvalue: int | str = 0, 
        variable: tkinter.Variable | None = None,
        hover: bool = True, 
        command: Callable[..., Any] | None = None, 
        state: str = tkinter.NORMAL, 
        name: str = "",
        **kwargs
        ):
        super().__init__(
            master, 
            width, 
            height, 
            switch_width, 
            switch_height, 
            corner_radius, 
            border_width, 
            button_length, 
            bg_color, fg_color, 
            border_color, 
            progress_color, 
            button_color, 
            button_hover_color, 
            text_color, 
            text_color_disabled, 
            text, 
            font,
            textvariable, 
            onvalue, 
            offvalue, 
            variable, 
            hover, 
            command, 
            state, 
            **kwargs
            )
        
        self._name = name
        
    
    @property
    def name(self):
        return self._name
    

class CursedItemButton(ctk.CTkButton):
    def __init__(
        self, 
        master: any, 
        width: int = 140, 
        height: int = 28, 
        corner_radius: int | None = None, 
        border_width: int | None = None, 
        border_spacing: int = 2, 
        bg_color: str | Tuple[str, str] = "transparent", 
        fg_color: str | Tuple[str, str] | None = None, 
        hover_color: str | Tuple[str, str] | None = None, 
        border_color: str | Tuple[str, str] | None = None, 
        text_color: str | Tuple[str, str] | None = None, 
        text_color_disabled: str | Tuple[str, str] | None = None, 
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
        round_width_to_even_numbers: bool = True, 
        round_height_to_even_numbers: bool = True, 
        text: str = "CTkButton", 
        font: tuple | CTkFont | None = None, 
        textvariable: tkinter.Variable | None = None, 
        image: CTkImage | Any | None = None, 
        state: str = "normal", 
        hover: bool = True, 
        command: Callable[[], None] | None = None, 
        compound: str = "left", 
        anchor: str = "center", 
        item: str = "ouija_board",
        **kwargs
    ):
        super().__init__(
            master, 
            width, 
            height, 
            corner_radius, 
            border_width, 
            border_spacing, 
            bg_color, 
            fg_color, 
            hover_color, 
            border_color, 
            text_color, 
            text_color_disabled, 
            background_corner_colors, 
            round_width_to_even_numbers, 
            round_height_to_even_numbers, 
            text, 
            font, 
            textvariable, 
            image, 
            state, 
            hover, 
            command, 
            compound, 
            anchor, 
            **kwargs
        )
        
        self._item = item
        
    
    @property
    def item(self):
        return self._item