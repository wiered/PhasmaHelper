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