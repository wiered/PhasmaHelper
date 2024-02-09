import json
import textwrap

import customtkinter as ctk

def is_window_exists(window: ctk.CTk | ctk.CTkToplevel | None) -> bool:
    """
    Checks if a window with the given name exists.

    Args:
        window (ctk.CTk | ctk.CTkToplevel): The window to check.

    Returns:
        bool: True if the window exists, False otherwise.
    """
    if window is None:
        return False

    if not window.winfo_exists():
        return False

    return True

def get_longest_line(lines):
    longest_line = 0
    for i, line in enumerate(lines):
        if len(line) > len(lines[longest_line]):
            longest_line = i
        
    return longest_line
            
def adjust_lines_lenght(lines):
    return lines
    MAX_LINE_LENGTH = 60
    
    longest_line = get_longest_line(lines)
    # lines[longest_line] = textwrap.fill(lines[longest_line], width=160)
    if len(lines[longest_line]) < MAX_LINE_LENGTH:
        lines[longest_line] += " " * (MAX_LINE_LENGTH - len(lines[longest_line]))
        
    return lines

ghosts_data = {}

def read_data(file_name):
    global ghosts_data
    
    with open(f"./core/data/ghosts/{file_name}.json", encoding='utf-8') as file:
        ghosts_data = json.load(file)

def get_ghost_data(name):
    return ghosts_data.get("Less").get(name)

def get_more(name):
    return ghosts_data.get("More").get(name)

