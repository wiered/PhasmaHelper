import time

import customtkinter as ctk

from config import cfg

def change_info_appearance():
    cfg.minimalistic_info = not cfg.minimalistic_info

class TimerWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Settings")
        self.after(250, lambda: self.iconbitmap('logo.ico'))

        self.time_frame = TimeFrame(self)
        self.time_frame.grid(row=0, column=0, columnspan=1, padx=(20, 20), pady=10, sticky="nsew")

        c = 0

        while True:
            self.time_frame.set_text(c)
            time.sleep(1)


class TimeFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.text_label = ctk.CTkLabel(master=self, text="0")
        self.text_label.grid(row=0, column=0, columnspan=1, padx=(30, 30), pady=10, sticky="nsew")

    def set_text(self, text):
        self.text_label.configure(text=text)
