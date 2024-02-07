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

import ctypes

import customtkinter as ctk

from config import cfg
from core import (
    frames, 
    windows
    )
from core.utils import (
    lists, 
    is_window_exists,
    themes,
    )

def configure_colors(appearance, color_theme):
    ctk.set_appearance_mode(appearance)  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme(color_theme)  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # difficulty, active_evidences
        self.difficulty = 0

        self.cursed_items_window = None
        self.ghosts_windows = []

        # Configure version and titlebar
        self.__version__ = "1.3"
        self.title(f"Phasma Helper v{self.__version__}")
        self.iconbitmap(".\core\icons\logo.ico")

        # Configure geometry
        self.geometry(f"+500+500")
        self.resizable(False, False)

        # Left menu bar
        self.left_menu_bar_frame = frames.LeftmenubarFrame(self, self.difficulty_changed)

        # Spirits Frame
        self.ghosts_frame = frames.GhostsFrame(self, self.create_ghost_window)

        # Evidences Frame
        self.evidences_frame = frames.EvidencesFrame(self, self.switch_updated)
        
        # Cursed Items Frame
        self.cursed_items_frame = frames.CursedItemsFrame(
            self, 
            width=400, 
            create_cursed_items_window=self.create_cursed_items_window
            )

        # Tools Frame
        self.tools_frame = frames.ToolsFrame(self, width=400)

        # Difficulty and version lables
        self.label_difficulty = ctk.CTkLabel(master=self, text=f"Difficulty: Amauter")
        self.label_version = ctk.CTkLabel(master=self, text=f"Version {self.__version__}")

        # Grid all widgets, frames and labels
        self.left_menu_bar_frame.grid(
            row=1, 
            column=0, 
            padx=(0, 0), 
            pady=(0, 0), 
            rowspan=3, 
            sticky="nsew",
            )
        self.ghosts_frame.grid(
            row=1, 
            column=2, 
            columnspan=2, 
            padx=(0, 20), 
            pady=(20, 0), 
            sticky="nsew"
            )
        self.evidences_frame.grid(
            row=1, 
            column=1,
            padx=(20, 20), 
            pady=(20, 0), 
            sticky="nsew"
            )
        self.cursed_items_frame.grid(
            row=2, 
            column=1, 
            columnspan=2, 
            padx=(20, 20), 
            pady=(20, 0), 
            sticky="nsew"
            )
        self.tools_frame.grid(
            row=2, 
            column=3, 
            padx=(0, 20), 
            pady=(20, 0), 
            sticky="nsew"
            )
        self.label_difficulty.grid(
            row=3, 
            column=1, 
            columnspan=1, 
            padx=(30, 30), 
            pady=10, 
            sticky="w"
            )
        self.label_version.grid(
            row=3, 
            column=3, 
            columnspan=1, 
            padx=(10, 30), 
            pady=10, 
            sticky="e"
            )

        # Get lists of buttons and switches
        self.difficulty_buttons = self.left_menu_bar_frame.get_difficulty_buttons()
        
    def switch_updated(self, evidence: str, state: int):
        """ Change state of buttons and switches according to checked evidences.

        Args:
            evidence (str): evidence name
            state (int): state of switch
        """
        self.evidences_frame.update_switches(
            evidence=evidence, 
            state=state, 
            difficulty=self.difficulty
        )
        self.ghosts_frame.update_buttons(
            possible_ghosts=self.evidences_frame.get_possible_ghosts(self.difficulty),
        )

    def difficulty_changed(self, difficulty: int):
        """ Changes difficulty setting. Also updates buttons and switches.

        Args:
            difficulty (int): diffiulty from 0 to 3, Amauter to Nightmare
        """
        
        if self.difficulty == difficulty:
            return
        
        self.left_menu_bar_frame.update_difficulty_buttons(
            old_difficulty=self.difficulty, 
            new_difficulty=difficulty
            )
        self.difficulty = difficulty
        self.label_difficulty.configure(
            text=f"Difficulty: {lists.DIFFICULTIES[self.difficulty]}"
            )
        
        self.evidences_frame.update_switches(self.difficulty)
        possible_evidences_count = 5 - difficulty
        if self.evidences_frame.activated_evidences_count > possible_evidences_count:
            self.evidences_frame.reset_switches()
            
        self.ghosts_frame.update_buttons(
            possible_ghosts=self.evidences_frame.get_possible_ghosts(self.difficulty),
        )

    def create_ghost_window(self, name: str):
        """ Creating the GhostInfoWindow

        Args:
            name (str): name of ghost
        """
        self.info = windows.GhostInfoWindow(self, name)
        self.info.attributes('-topmost', True)
        self.info.attributes('-alpha', cfg.ghosts_window_alpha)
        self.ghosts_windows.append(self.info)
        self.info.update()
        self.info.mainloop()
    
    def remove_ghost_window(self, window):
        self.ghosts_windows.remove(window)
    
    def create_cursed_items_window(self, item = "ouija_board"):
        """ Creating or focusing the CursedItemsWindow

        Args:
            name (str): name of ghost
        """
        if is_window_exists(self.cursed_items_window) == False:
            self.cursed_items_window = windows.CursedItemsWindow(item)
            self.cursed_items_window.attributes('-topmost', True)
            self.cursed_items_window.attributes('-alpha', cfg.cursed_items_window_alpha)
            self.cursed_items_window.update()
            self.cursed_items_window.mainloop()
        else:
            self.cursed_items_window.change_item(item)
    
    def is_all_childrens_destroyed(self) -> bool:
        """ Returns True if all child windows are destroyed, false otherwise

        Returns:
            bool: true if all child windows are destroyed, false otherwise
        """
        if len(self.ghosts_windows) > 0:
            return False
        if is_window_exists(self.cursed_items_window): 
            return False
        if is_window_exists(self.left_menu_bar_frame.settings_window):
            return False

        return True
    
    def destroy_childrens(self):
        """
        This function destroys all child windows of the main window.
        This includes the GhostInfoWindow, CursedItemsWindow, and the
        SettingsWindow.

        !Function is called repeatedly until all child windows are destroyed.
        """
        for window in self.ghosts_windows:
            if is_window_exists(window):
                window.destroy()

        if is_window_exists(self.cursed_items_window):
            self.cursed_items_window.destroy()
            self.cursed_items_window = None

        self.left_menu_bar_frame.destroy_settings_window()

    def destroy(self):
        cfg.save_config()

        while not self.is_all_childrens_destroyed():
            self.destroy_childrens()

        super().destroy()
    

if __name__ == "__main__":
    myappid = 'wiered.phasmahelper.ph.13' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    configure_colors(cfg.appearance, cfg.color_theme)

    app = App()
    app.mainloop()
    