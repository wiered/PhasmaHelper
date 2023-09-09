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
        