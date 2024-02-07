import tkinter
from typing import Any, Callable, Optional, Tuple, Union

import customtkinter as ctk
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage

from core.utils.themes import *

EVIDENCE_BUTTON_COLORS = {
        0: evidence_button_unknown,
        1: evidence_button_activated,
        2: evidence_button_deactivated,
    }

EVIDENCE_BUTTON_HOVER_COLORS = {
        0: evidence_button_unknown_hover,
        1: evidence_button_activated_hover,
        2: evidence_button_deactivated_hover,
    }

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


class EvidenceButton(ctk.CTkButton):
    def __init__(self, master, command, text):
        super().__init__(master=master, text=text)
        
        self._evidence_state = 0
        self._command = self.change_state
        self.command = command
        self._text = text
        
        self.configure(fg_color = EVIDENCE_BUTTON_COLORS[self.state])
        self.configure(hover_color = EVIDENCE_BUTTON_HOVER_COLORS[self.state])
        
    @property
    def state(self) -> int:
        return self._evidence_state
    
    @property
    def text(self):
        return self._text
    
    def reset(self):
        self._evidence_state = 0
        self.configure(fg_color = EVIDENCE_BUTTON_COLORS[self.state])
        self.configure(hover_color = EVIDENCE_BUTTON_HOVER_COLORS[self.state])

    def change_state(self):
        self._evidence_state = (self._evidence_state + 1)%3
        self.configure(fg_color = EVIDENCE_BUTTON_COLORS[self._evidence_state])
        self.configure(hover_color = EVIDENCE_BUTTON_HOVER_COLORS[self._evidence_state])
        self.command()
        
    def set_state(self, value):
        if value < 0 or value > 2:
            raise ValueError("Evidence button state must be 0, 1 or 2")
        self._evidence_state = value
        self.configure(fg_color = EVIDENCE_BUTTON_COLORS[self._evidence_state])
        self.configure(hover_color = EVIDENCE_BUTTON_HOVER_COLORS[self._evidence_state])


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
    