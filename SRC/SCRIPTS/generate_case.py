#imports external
import random
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
        }
        self.DIALOG_
    def set_types(self, npc: int):
        match self.CASO["DEATH_CASE"]:
            case "Envenenado":
                match npc:
                    case 0:
                        self.NPCS[npc]["TYPE"] = self.SCENE_VALUES["CASO"]["NPC_TYPES"][2]
                        npc_str = f"{f"{self.NPCS[npc]["NAME"]}":<20}||     {f"{self.NPCS[npc]["DESCRIPTION"]}":<90}||      {self.NPCS[npc]["TYPE"]}"
                        print(f"0-Vitima:                 {npc_str}")
                    case 1:
                        self.NPCS[npc]["TYPE"] = self.SCENE_VALUES["CASO"]["NPC_TYPES"][0]
                        npc_str = f"{f"{self.NPCS[npc]["NAME"]}":<20}||     {f"{self.NPCS[npc]["DESCRIPTION"]}":<90}||      {self.NPCS[npc]["TYPE"]}"
                        print(f"1-Assassino:              {npc_str}")
                    case 2:
                        self.NPCS[npc]["TYPE"] = self.SCENE_VALUES["CASO"]["NPC_TYPES"][1]
                        npc_str = f"{f"{self.NPCS[npc]["NAME"]}":<20}||     {f"{self.NPCS[npc]["DESCRIPTION"]}":<90}||      {self.NPCS[npc]["TYPE"]}"
                        print(f"2-Testemunha:             {npc_str}")
                    case 3:
                        self.NPCS[npc]["TYPE"] = self.SCENE_VALUES["CASO"]["NPC_TYPES"][1]
                        npc_str = f"{f"{self.NPCS[npc]["NAME"]}":<20}||     {f"{self.NPCS[npc]["DESCRIPTION"]}":<90}||      {self.NPCS[npc]["TYPE"]}"
                        print(f"3-Suspeito principal:     {npc_str}")
                    case 4:
                        self.NPCS[npc]["TYPE"] = self.SCENE_VALUES["CASO"]["NPC_TYPES"][1]
                        npc_str = f"{f"{self.NPCS[npc]["NAME"]}":<20}||     {f"{self.NPCS[npc]["DESCRIPTION"]}":<90}||      {self.NPCS[npc]["TYPE"]}"
                        print(f"4-Cúmplice/testemunha:    {npc_str}")
                    case 5:
                        self.NPCS[npc]["TYPE"] = self.SCENE_VALUES["CASO"]["NPC_TYPES"][1]
                        npc_str = f"{f"{self.NPCS[npc]["NAME"]}":<20}||     {f"{self.NPCS[npc]["DESCRIPTION"]}":<90}||      {self.NPCS[npc]["TYPE"]}"
                        print(f"5-Suspeito (amigo de 3):  {npc_str}")
            case "Esfaqueado":
                match npc:
                    case 0:
                        ...
    def generate_case(self):
        self.CASO["DEATH_CASE"] = "Envenenado" # random.choice(self.SCENE_VALUES["CASO"]["CAUSA_DA_MORTE"])
        self.CASO["DEATH_PLACE"] = random.choice(self.SCENE_VALUES["CASO"]["LUGAR_DA_MORTE"])
        print(self.CASO)
        for _ in range(6):
            name = random.choice(self.NPC_VALUES["NOMES"])
            description = random.choice(self.NPC_VALUES["DESCRICOES"])
            while name["genero"] != description["genero"][0]: description = random.choice(self.NPC_VALUES["DESCRICOES"])
            self.NPCS.append({"NAME":name["nome"],"DESCRIPTION":{"OCUPACAO":description["ocupacao"],"PERSONALIDADE":description["personalidade"]}, "TYPE":...})
        for npc in range(len(self.NPCS)):
            self.set_types(npc)
        self.EVIDENCES[""]
        return True
print(CASE().generate_case())