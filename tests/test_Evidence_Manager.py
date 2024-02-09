from copy import copy
import json
import random
import unittest
from collections import Counter

from core.utils import EvidencesManager, Ghost
from core.utils import lists

def read_ghosts():
    ghosts = []
    with open('.\core\data\evidences.json', encoding='utf-8') as json_file:
        ghosts_by_evidences = json.load(json_file)
        
    with open('.\core\data\ghosts\EN_en.json', encoding='utf-8') as json_file:
        ghosts_dict = json.load(json_file)
        
    ghosts_dict = ghosts_dict.get("More")
        
    for ghost_name in ghosts_dict:
        ghost_data = ghosts_dict.get(ghost_name)
        ghosts.append(
            Ghost(
                name=ghost_name,
                evidences=ghost_data.get("evidences"),
                behavior=ghost_data.get("behavior"),
                speed=0,
            )
        )
    
    return ghosts, ghosts_by_evidences

class TestEvidencesManager(unittest.TestCase):
    def test_changing_state(self):
        evidences_manager = EvidencesManager()
        self.assertEqual(evidences_manager.activated_evidences, [], "Activated evidences is not Empty")
        self.assertEqual(evidences_manager.disactivated_evidences, [], "Disactivated evidences is not Empty")
        self.assertEqual(evidences_manager.unknown_evidences, lists.EVIDENCES, "Disactivated evidences is not Empty")
        
        evidences_manager.change_evidence_state("EMF 5", 1)
        self.assertEqual(evidences_manager.activated_evidences, ["EMF 5"], "No EMF in activated_evidences")
        evidences_manager.change_evidence_state("DOTS", 2)
        self.assertEqual(evidences_manager.disactivated_evidences, ["DOTS"], "No DOTS in disactivated_evidences")
    
    def test_random_activating(self):
        for i in range(20):
            evidences_manager = EvidencesManager()
            evidence = random.choice(lists.EVIDENCES)
            evidences_manager.change_evidence_state(evidence, 1)
            
            self.assertEqual(evidences_manager.activated_evidences, [evidence], "Error in random activating Evidence")
                
    def test_activating_multiple(self):
        for i in range(20):
            evidences_manager = EvidencesManager()
            k = random.randint(0, 6)
            evidences = random.sample(lists.EVIDENCES, k)
            for evidence in evidences:
                evidences_manager.change_evidence_state(evidence, 1)
                
            self.assertEqual(evidences_manager.activated_evidences, evidences, "Error in multiple random activating Evidence")

    def test_disactivating(self):
        for i in range(20):
            evidences_manager = EvidencesManager()
            evidence = random.choice(lists.EVIDENCES)
            evidences_manager.change_evidence_state(evidence, 2)
            
            self.assertEqual(evidences_manager.disactivated_evidences, [evidence], "Error in random disactivating Evidence")
            
    def test_disacticvating_multiple(self):
        for i in range(20):
            evidences_manager = EvidencesManager()
            k = random.randint(0, 6)
            evidences = random.sample(lists.EVIDENCES, k)
            for evidence in evidences:
                evidences_manager.change_evidence_state(evidence, 2)
                
            self.assertEqual(evidences_manager.disactivated_evidences, evidences, "Error in multiple random disactivating Evidences")
            
    def test_random_activating_or_disactivating(self):
        for i in range(20):
            rnd_choice = random.randint(1, 2) 
            
            evidences_manager = EvidencesManager()
            evidence = random.choice(lists.EVIDENCES)
            evidences_manager.change_evidence_state(evidence, rnd_choice)
            if rnd_choice == 1:
                evindences_list = evidences_manager.activated_evidences
            else:
                evindences_list = evidences_manager.disactivated_evidences
            
            self.assertEqual(evindences_list, [evidence], "Error in randon activating or disactivating Evidences")
            
    def test_multiple_random_activating_or_disactivating(self):
        for i in range(20):
            evidences_manager = EvidencesManager()
            k = random.randint(0, 6)
            evidences = random.sample(lists.EVIDENCES, k)
            activated_evidences = []
            disactivated_evidences = []
            
            for evidence in evidences:
                random_choice = random.randint(1, 2)
                evidences_manager.change_evidence_state(evidence, random_choice)
                if random_choice == 1:
                    activated_evidences.append(evidence)
                else:
                    disactivated_evidences.append(evidence)
                
            self.assertEqual(evidences_manager.activated_evidences, activated_evidences, "Error in multiple_random_activating_or_disactivating: wrong activated_evidences")
            self.assertEqual(evidences_manager.disactivated_evidences, disactivated_evidences, "Error in multiple_random_activating_or_disactivating: wrong disactivated_evidences")
            
    def test_is_ghost_possible(self):
        ghosts, ghosts_by_evidences = read_ghosts()
        evidences_manager = EvidencesManager()
        for ghost in ghosts:
            self.assertEqual(evidences_manager.is_ghost_possible(ghost=ghost, difficulty=1), True, "Error in is_ghost_possible, with no activated evidences")
        
        evidences_manager.change_evidence_state("EMF 5", 1)
        for ghost in ghosts:
            if ghost.name in ghosts_by_evidences.get("EMF 5"):
                self.assertEqual(evidences_manager.is_ghost_possible(ghost=ghost, difficulty=1), True, "Error in is_ghost_possible, with \"EMF\" evidence")
    
    def test_is_ghost_possible_one_random_evidence(self):
        ghosts, ghosts_by_evidences = read_ghosts()
        for i in range(20):
            evidences_manager = EvidencesManager()
            evidence = random.choice(lists.EVIDENCES)
            evidences_manager.change_evidence_state(evidence, 1)
            for ghost in ghosts:
                if ghost.name in ghosts_by_evidences.get(evidence):
                    self.assertEqual(evidences_manager.is_ghost_possible(ghost=ghost, difficulty=1), True, "Error in is_ghost_possible, with one random evidence")

    def test_possible_ghosts(self):
        evidences_manager = EvidencesManager()
        possible_ghosts = evidences_manager.get_possible_ghosts()
        for ghost in lists.GHOSTS_EN:
            self.assertEqual(
                ghost in possible_ghosts,
                True,
                "Error in get_possible_ghosts with no evidences"
            )
        
        evidences_manager.change_evidence_state("EMF 5", 1)
        possible_ghosts = evidences_manager.get_possible_ghosts()
        _, ghosts_by_evidences = read_ghosts()
        for ghost in ghosts_by_evidences.get("EMF 5"):
            self.assertEqual(
                ghost in possible_ghosts,
                True,
                f"Error in get_possible_ghosts with EMF: p_g: {possible_ghosts}, t_p_g: {ghosts_by_evidences.get('EMF 5')}"
            )
    
    def test_possible_ghosts_random_evidence(self):
        _, ghosts_by_evidences = read_ghosts()
        evidences_manager = EvidencesManager()
        for _ in range(20):
            evidence = random.choice(lists.EVIDENCES)
            evidences_manager.change_evidence_state(evidence, 1)
            possible_ghosts = evidences_manager.get_possible_ghosts()
            for ghost in ghosts_by_evidences.get(evidence):
                self.assertEqual(
                    ghost in possible_ghosts,
                    True,
                    "Error in get_possible_ghosts with EMF"
                )
            evidences_manager.change_evidence_state(evidence, 0)
    
    def test_possible_ghosts_two_random_evidences(self):
        _, ghosts_by_evidences = read_ghosts()
        evidences_manager = EvidencesManager()
        for _ in range(20):
            first_evidence = random.choice(lists.EVIDENCES)
            second_evidence = random.choice(lists.EVIDENCES)
            evidences_manager.change_evidence_state(first_evidence, 1)
            evidences_manager.change_evidence_state(second_evidence, 1)
            
            first_evidence_ghost = ghosts_by_evidences.get(first_evidence)
            second_evidence_ghost = ghosts_by_evidences.get(second_evidence)
            test_possible_ghosts = list((Counter(first_evidence_ghost) & Counter(second_evidence_ghost)).elements())
            
            possible_ghosts = evidences_manager.get_possible_ghosts()
            for ghost in test_possible_ghosts:
                self.assertEqual(
                    ghost in possible_ghosts,
                    True,
                    f"""Error in get_possible_ghosts with multiple random \nf_e: {first_evidence} \ns_e: {second_evidence} \np_g: {possible_ghosts} \nt_p_g: {test_possible_ghosts}
                    f_e_gs = {first_evidence_ghost}
                    s_e_gs = {second_evidence_ghost}
                    """
                )
            evidences_manager.reset_evidences()
    
    def test_possible_ghosts_multiple_random_evidences(self):
        _, ghosts_by_evidences = read_ghosts()
        evidences_manager = EvidencesManager()
        for i in range(20):
            evidence_ghosts = copy(lists.GHOSTS_EN)
            k = random.randint(0, 6)
            evidences = random.sample(lists.EVIDENCES, k)
            for evidence in evidences:
                evidences_manager.change_evidence_state(evidence, 1)
                evidence_ghosts = list((Counter(evidence_ghosts) & Counter(ghosts_by_evidences.get(evidence))).elements())
            
            possible_ghosts = evidences_manager.get_possible_ghosts()
            for ghost in evidence_ghosts:
                self.assertEqual(
                    ghost in possible_ghosts,
                    True,
                    f"Error in get_possible_ghosts with multiple random \nevidences: {evidences} \np_g: {possible_ghosts} \nt_p_g: {evidence_ghosts}"
                )
            evidences_manager.reset_evidences()
    
    def test_forced_evidences(self):
        evidences_manager = EvidencesManager()
        
        evidences_manager.change_evidence_state("Fingerprints", 2)
        self.assertEqual(
            "Обакэ" in evidences_manager.get_possible_ghosts(4),
            False, 
            "Error in is_ghost_possible, with forced fp ghosts"
            )
        evidences_manager.change_evidence_state("Fingerprints", 0)
        
        evidences_manager.change_evidence_state("Spirit Box", 2)
        for ghost in ["Морой", "Деоген"]:
            self.assertEqual(
                ghost in evidences_manager.get_possible_ghosts(4), 
                False, 
                "Error in is_ghost_possible, with forced spirit box"
                )
        evidences_manager.change_evidence_state("Spirit Box", 0)
        
        evidences_manager.change_evidence_state("Ghost Orb", 2)
        self.assertEqual(
            "Мимик" in evidences_manager.get_possible_ghosts(4), 
            False, 
            "Error in is_ghost_possible, with forced ghost orbs"
            )
        evidences_manager.change_evidence_state("Ghost Orb", 0)
            
        evidences_manager.change_evidence_state("Freezing Temp", 2)
        self.assertEqual(
            "Ханту" in evidences_manager.get_possible_ghosts(4), 
            False, 
            "Error in is_ghost_possible, with forced freezing"
            )
        evidences_manager.change_evidence_state("Freezing Temp", 0)
    
    def test_reset_evidences(self):
        evidences_manager = EvidencesManager()
        self.assertEqual(evidences_manager.activated_evidences, [], "Activated evidences is not Empty")
        self.assertEqual(evidences_manager.disactivated_evidences, [], "Disactivated evidences is not Empty")
        self.assertEqual(evidences_manager.unknown_evidences, lists.EVIDENCES, "Disactivated evidences is not Empty")
        
        evidences_manager.change_evidence_state("EMF 5", 1)
        evidences_manager.change_evidence_state("Spirit Box", 2)
        evidences_manager.reset_evidences()
        self.assertEqual(evidences_manager.activated_evidences, [], "Activated evidences is not Empty")
        self.assertEqual(evidences_manager.disactivated_evidences, [], "Disactivated evidences is not Empty")
        self.assertEqual(evidences_manager.unknown_evidences, lists.EVIDENCES, "Disactivated evidences is not Empty")
    
    def test(self):
        ...
    