#imports external
import random
#imports internal
import SCRIPTS.load_json as _json
class CASE():
    def __init__(self) -> None:
        json_obj = _json.CONFIG()
        json_obj.create_config()
        self.SCENE_VALUES = json_obj.load_json("scene_creation.json")
        self.NPC_VALUES = json_obj.load_json("personagens.json")
        self.EVIDENCE_VALUES = {
            "VERDADES": ...,
            "CONFLITANTES": ...,
            "FALSAS": ...
        }
        self.NPCS = []
        self.CASO = {
            "DEATH_CASE": ...,
            "DEATH_PLACE": ...,
            "DEATH_DIALOG": ...
        }
    def set_types(self, npc: int):
        match self.CASO["DEATH_CASE"]:
            case "Envenenado":
                if npc == 0:
                    self.NPCS[npc]["TYPE"] = self.SCENE_VALUES["CASO"]["NPC_TYPES"][2]
                    #?debug: npc_str = f"{f"{self.NPCS[npc]["NAME"]}":<20}||     {f"{self.NPCS[npc]["DESCRIPTION"]}":<90}||      {self.NPCS[npc]["TYPE"]}"
                    #?debug: print(f"0-Vitima:                 {npc_str}")
                elif npc == 1:
                    self.NPCS[npc]["TYPE"] = self.SCENE_VALUES["CASO"]["NPC_TYPES"][0]
                    #?debug: npc_str = f"{f"{self.NPCS[npc]["NAME"]}":<20}||     {f"{self.NPCS[npc]["DESCRIPTION"]}":<90}||      {self.NPCS[npc]["TYPE"]}"
                    #?debug: print(f"1-Assassino:              {npc_str}")
                else:
                    self.NPCS[npc]["TYPE"] = self.SCENE_VALUES["CASO"]["NPC_TYPES"][1]
                    #?debug: npc_str = f"{f"{self.NPCS[npc]["NAME"]}":<20}||     {f"{self.NPCS[npc]["DESCRIPTION"]}":<90}||      {self.NPCS[npc]["TYPE"]}"
                    #?debug: print(f"2-Testemunha:             {npc_str}")
            case "Esfaqueado":
                if npc == int:
                    ...
    def generate_case(self):
        self.CASO["DEATH_CASE"] = "Envenenado" #! random.choice(self.SCENE_VALUES["CASO"]["CAUSA_DA_MORTE"])
        self.CASO["DEATH_PLACE"] = random.choice(self.SCENE_VALUES["CASO"]["LUGAR_DA_MORTE"])
        self.CASO["DEATH_PLACE"] = self.SCENE_VALUES["CASO"][f"CASO_{self.CASO["DEATH_CASE"].upper()}"]["CAUSA_DA_MORTE"]
        #?debug: print(self.CASO)
        parts_list = ["VERDADES", "CONFLITANTES", "FALSAS"]
        for i in range(len(self.EVIDENCE_VALUES)):
            self.EVIDENCE_VALUES[parts_list[i]] = self.SCENE_VALUES["CASO"][f"CASO_{self.CASO["DEATH_CASE"].upper()}"]["EVIDENCIAS"][f"EVIDENCIAS_{parts_list[i]}"]
        #? DEFININDO O NOME E DESCRIÇÃO DE CADA NPC
        for _ in range(6):
            name = random.choice(self.NPC_VALUES["NOMES"])
            description = random.choice(self.NPC_VALUES["DESCRICOES"])
            while name["genero"] != description["genero"][0]: description = random.choice(self.NPC_VALUES["DESCRICOES"])
            self.NPCS.append({"NAME":name["nome"],"DESCRIPTION":{"OCUPACAO":description["ocupacao"],"PERSONALIDADE":description["personalidade"]}, "TYPE":...})
        #? DEFININDO OS TIPOS DE CADA NPC DEPENDENDO DO CASO
        for npc in range(len(self.NPCS)):
            self.set_types(npc)
        #? ADICIONANDO AS EVIDENCIAS NO DICIONARIO DE NPCS
        for i in range(len(parts_list)):
            for evidence in self.EVIDENCE_VALUES[parts_list[i]]:
                index_evi = self.EVIDENCE_VALUES[parts_list[i]].index(evidence)
                self.EVIDENCE_VALUES[parts_list[i]][index_evi]["DIALOG"][1] = self.EVIDENCE_VALUES[parts_list[i]][index_evi]["DIALOG"][1].replace("$", f"{self.CASO["DEATH_PLACE"]}")
                for n in range(len(self.NPCS)):
                    self.EVIDENCE_VALUES[parts_list[i]][index_evi]["DIALOG"][1] = self.EVIDENCE_VALUES[parts_list[i]][index_evi]["DIALOG"][1].replace(f"{n}", f"{self.NPCS[n]["NAME"]}")
                    self.EVIDENCE_VALUES[parts_list[i]][index_evi]["FRASE"] = self.EVIDENCE_VALUES[parts_list[i]][index_evi]["FRASE"].replace(f"{n}", f"{self.NPCS[n]["NAME"]}")
                self.NPCS[int(evidence["DIALOG"][0])]["EVIDENCIA"] = [evidence["DIALOG"][1], evidence["FRASE"], evidence["PREMISSA"]]
                #?debug: print(f"\n{parts_list[i]}: {evidence}\n")
        self.CASO["DEATH_PLACE"] = self.CASO["DEATH_PLACE"].replace("$", f"{self.CASO["DEATH_PLACE"]}")
        for n in range(len(self.NPCS)): self.CASO["DEATH_PLACE"] = self.CASO["DEATH_PLACE"].replace(f"{n}", f"{self.NPCS[n]["NAME"]}")
        return True