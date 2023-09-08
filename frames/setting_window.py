import customtkinter as ctk

from config import cfg

def change_info_appearance():
    cfg.minimalistic_info = not cfg.minimalistic_info

class SettingWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Settings")
        self.after(250, lambda: self.iconbitmap('logo.ico'))

        self.settings_frame = SettingsFrame(self)
        self.settings_frame.grid(row=0, column=0, columnspan=1, padx=(20, 20), pady=10, sticky="nsew")


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.minimalistic_info_switch = ctk.CTkSwitch(
            master=self,
            command=lambda: change_info_appearance(),
            text="Minimalistic Info",
            )
        self.minimalistic_info_switch.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")

        if cfg.minimalistic_info:
            self.minimalistic_info_switch.select()

        
