import itertools
import json
from copy import copy
from typing import List
from dataclasses import dataclass

from customtkinter import CTkSwitch

from core.utils import lists
from core.widgets import EvidenceSwitch
    
    
@dataclass   
class Ghost:
    name: str
    evidences: List[str]
    speed: int
    behavior: str
    
    def has_evidences(self, evidences):
        return all(evidence in self.evidences for evidence in evidences)
    
    def has_any_evidence(self, evidences):
        return any(evidence in self.evidences for evidence in evidences)
    
    def __repr__(self) -> str:
        return f"name: {self.name}  evds: {self.evidences}\n"
    
    
class EvidencesManager:
    def __init__(self):
        self._activated_evidences = []
        self._disactivated_evidences = []
        self._unknown_evidences = copy(lists.EVIDENCES)
        
        self.ghosts: List[Ghost] = []
        self.speed = 0

        self.read_ghosts()
                
    @property
    def activated_evidences(self) -> list:
        return self._activated_evidences

    @property 
    def disactivated_evidences(self) -> list:
        return self._disactivated_evidences
    
    @property
    def unknown_evidences(self) -> list:        
        return self._unknown_evidences

    def change_evidence_state(self, evidence: str, state: int):
        """ Change state of buttons and switches according to checked evidences.

        Args:
            evidence (str): evidence name
            state (int): state of switch
        """
        if evidence in self._activated_evidences:
            self._activated_evidences.remove(evidence)
        elif evidence in self._disactivated_evidences:
            self._disactivated_evidences.remove(evidence)
        elif evidence in self._unknown_evidences:
            self._unknown_evidences.remove(evidence)
        
        if state == 0:
            self._unknown_evidences.append(evidence)
        elif state == 1:
            self._activated_evidences.append(evidence)
        elif state == 2:
            self._disactivated_evidences.append(evidence)
    
    def is_ghost_possible(self, ghost, difficulty):
        # Check if has evidence
        if not ghost.has_evidences(self.activated_evidences):
            return False
        
        # Check if correct speed
        
        # For proffesional or lower
        #   if ghost has any of disactivated evidences, then return False
        if difficulty < 3:
            if ghost.has_any_evidence(self._disactivated_evidences):
                return False
        
        # For Nightmare
        # Form pairs of disactivated evidences,
        #   if ghost has both evidences of any pair
        #   then return false
        # Cause on Nightmare ghost can only "hide" one evidence
        #   we can eliminate them, cause ghost cant "hide" two evidences
        if difficulty == 3:
            for pair in itertools.combinations(self._disactivated_evidences, r=2):
                if ghost.has_evidences(pair):
                    return False
        
        # For Insane
        # Form triplets of disactivated evidences,
        #   if ghost has all evidences of any triplet
        #   then return false
        if difficulty == 4:
            for triplet in itertools.combinations(self._disactivated_evidences, r=3):
                if ghost.has_evidences(triplet):
                    return False
        
        return True   
    
    def remove_ghosts(self, possible_ghosts, evidence, ghosts):
        if not evidence in self._disactivated_evidences:
            return possible_ghosts
        
        for ghost in ghosts:
            if ghost in possible_ghosts:
                possible_ghosts.remove(ghost)
        
        return possible_ghosts
    
    def check_forced_evidences(self, difficulty, possible_ghosts):   
        if len(self.activated_evidences) > 5 - difficulty:  
            return ["The Mimic"]
        
        possible_ghosts = self.remove_ghosts(
            possible_ghosts, 
            "Orbs", 
            ["The Mimic"]
            )
        
        possible_ghosts = self.remove_ghosts(
            possible_ghosts, 
            "Spirit Box", 
            ["Moroi", "Deogen"]
            )

        possible_ghosts = self.remove_ghosts(
            possible_ghosts, 
            "Ultra V.", 
            ["Obake"]
            )
        
        possible_ghosts = self.remove_ghosts(
            possible_ghosts, 
            "Freezing", 
            ["Hantu"]
            )
        
        return possible_ghosts
    
    def get_possible_ghosts(self, difficulty = 1):
        possible_ghosts = []
        for ghost in self.ghosts:
            if self.is_ghost_possible(ghost, difficulty):
                possible_ghosts.append(ghost.name)

        possible_ghosts = self.check_forced_evidences(difficulty, possible_ghosts)
        
        return possible_ghosts
    
    def get_possible_ghosts_by_evidences(self, evidences):
        possible_ghosts = []
        for ghost in self.ghosts:
            if not ghost.has_evidences(evidences):
                continue
            
            possible_ghosts.append(ghost.name)
        
        return possible_ghosts
    
    def read_ghosts(self):
        with open('.\core\data\evidences.json', encoding='utf-8') as json_file:
            self.ghosts_by_evidences = json.load(json_file)
            
        with open('.\core\data\ghosts\EN_en.json', encoding='utf-8') as json_file:
            ghosts_dict = json.load(json_file)
            
        ghosts_dict = ghosts_dict.get("More")
            
        for ghost_name in ghosts_dict:
            ghost_data = ghosts_dict.get(ghost_name)
            self.ghosts.append(
                Ghost(
                    name=ghost_name,
                    evidences=ghost_data.get("evidences"),
                    behavior=ghost_data.get("behavior"),
                    speed=0,
                )
            )

        del ghosts_dict
        del ghost_data
    
    def reset_evidences(self):
        self._activated_evidences = []
        self._disactivated_evidences = []
        self._unknown_evidences = copy(lists.EVIDENCES)
    
    def is_evidence_active(self, evidence: str | CTkSwitch | EvidenceSwitch) -> bool:
        """ Return true if evidence is checked

        Args:
            evidence (str | ctk.CTkSwitch | widgets.EvidenceSwitch): evidence name or evidence switch

        Returns:
            bool: True if checked False else
        """
        
        evidence_name = None
        if isinstance(evidence, str):
            evidence_name = evidence
        elif isinstance(evidence, CTkSwitch):
            evidence_name = evidence.name
        elif isinstance(evidence, EvidenceSwitch):
            evidence_name = evidence.name
            
        return evidence_name in self.activated_evidences
    
    def get_unknown_evidences(self) -> list:
        return self.unknown_evidences
    
    def get_impossible_evidences(self) -> list:
        impossible_evidences = []
        
        for i, evidence in enumerate(lists.EVIDENCES):
            if evidence in self.activated_evidences or evidence in self.disactivated_evidences:
                continue
            # Takes ghost in list of active ghosts, checks if he has that evidence, 
            #   and if so, adds it to tmp list
            tmp = self.get_possible_ghosts_by_evidences(
                self.activated_evidences + [evidence]
            )
            if len(tmp) == 0:
                impossible_evidences.append(i)
        
        return impossible_evidences
            