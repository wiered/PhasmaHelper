import customtkinter

class ToolsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_tools = customtkinter.CTkLabel(master=self, text="TOOLS (WIP)")
        self.label_tools.grid(row=1, column=1, columnspan=1, padx=(30, 10), pady=(10, 0), sticky="w")

        self.label_tools_smudge_stick = customtkinter.CTkLabel(master=self,
                                                               text="Start smudge stick timer (60 seconds) - Ctrl+B")
        self.label_tools_smudge_stick.grid(row=2, column=1, columnspan=1, padx=(20, 0), pady=0, sticky="w")

        self.label_tools_attack = customtkinter.CTkLabel(master=self, text="Start attack timer - Ctrl+Q")
        self.label_tools_attack.grid(row=3, column=1, columnspan=1, padx=(20, 0), pady=0, sticky="w")

        self.label_tools_difficulty = customtkinter.CTkLabel(master=self, text="Change difficulty - Ctrl+P")
        self.label_tools_difficulty.grid(row=4, column=1, columnspan=1, padx=(20, 0), pady=(0, 10), sticky="w")

