#imports external
import pygame as pyg, random
#imports internal
import load_json as _json
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
        name = random.choice(self.NPC_VALUES["NOMES"])
        description = random.choice(self.NPC_VALUES["DESCRICOES"])
        while name["genero"] != description["genero"][0]:
            description = random.choice(self.NPC_VALUES["DESCRICOES"])
        print(name,"\n",description)
        self.NPCS.append({"NAME":name["nome"],"DESCRIPTION":{"OCUPACAO":description["ocupacao"],"PERSONALIDADE":description["personalidade"]}})
        print("true!")
CASE().generate_case()