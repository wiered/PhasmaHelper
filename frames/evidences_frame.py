import customtkinter as ctk

class EvidencesFrame(ctk.CTkFrame):
    def __init__(self, master, disable_spirits):
        super().__init__(master)

        self.label_evidences = ctk.CTkLabel(master=self,text="EVIDENCES")
        self.label_evidences.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

        self.emf_switch = ctk.CTkSwitch(
            master=self,
            command=lambda: disable_spirits("EMF", self.emf_switch.get()),
            text="EMF"
        )
        self.emf_switch.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")

        self.spirit_box_switch = ctk.CTkSwitch(
            master=self,
            command=lambda: disable_spirits("Spirit Box", self.spirit_box_switch.get()),
            text="Spirit Box"
        )
        self.spirit_box_switch.grid(row=4, column=0, pady=10, padx=20, sticky="nsew")

        self.fingerprints_switch = ctk.CTkSwitch(
            master=self,
            command=lambda: disable_spirits("Fingerprints", self.fingerprints_switch.get()),
            text="Fingerprints"
        )
        self.fingerprints_switch.grid(row=5, column=0, pady=10, padx=20, sticky="nsew")

        self.ghost_orb_switch = ctk.CTkSwitch(
            master=self,
            command=lambda: disable_spirits("Ghost Orb", self.ghost_orb_switch.get()),
            text="Ghost Orb")
        self.ghost_orb_switch.grid(row=6, column=0, pady=10, padx=20, sticky="nsew")

        self.ghost_writing_switch = ctk.CTkSwitch(
            master=self,
            command=lambda: disable_spirits("Ghost Writing", self.ghost_writing_switch.get()),
            text="Ghost Writing")
        self.ghost_writing_switch.grid(row=7, column=0, pady=10, padx=20, sticky="nsew")

        self.freezing_temp_switch = ctk.CTkSwitch(
            master=self,
            command=lambda: disable_spirits("Freezing Temp", self.freezing_temp_switch.get()),
            text="Freezing Temp")
        self.freezing_temp_switch.grid(row=8, column=0, pady=10, padx=20, sticky="nsew")

        self.DOTS_switch = ctk.CTkSwitch(
            master=self,
            command=lambda: disable_spirits("DOTS", self.DOTS_switch.get()),
            text="DOTS")
        self.DOTS_switch.grid(row=9, column=0, pady=10, padx=20, sticky="nsew")