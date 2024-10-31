#imports external
import pygame as pyg, random
#imports internal
import SCRIPTS.load_json as _json
class CASE():
    def __init__(self) -> None:
        json_obj = _json.CONFIG()
        json_obj.create_config()
        self.SCENE_VALUES = json_obj.load_json("scene_creation.json")
        self.NPC_VALUES = json_obj.load_json("personagens.json")
        self.NPCS = []
        self.CASO = {
            "DEATH_CASE": ...,
            "DEATH_PLACE": ...,
            "DIALOG_PLACE": ...,
        }
        self.EVIDENCES = {
            "TRURTHS": [...],
            "CONFLICTS": [...],
            "FALSES": [...]
        }
    def generate_case(self):
        npc_pt1 = {1:random.choice(self.NPC_VALUES["NOMES"]), 2:random.choice(self.NPC_VALUES["DESCRICOES"])}
        print(npc_pt1)
        if npc_pt1[1]["genero"]:
            ...
        self.NPCS.append(
            {"nome": ...}
        )
        print("true!")