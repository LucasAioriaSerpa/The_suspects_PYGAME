#imports external
import pygame as pyg, sys
#imports internal
import SCRIPTS.mouse as _mou
import SCRIPTS.utilities as _util
import SCRIPTS.generate_case as _gen
import SCRIPTS.NPCs as _npc
import SCRIPTS.player as _ply
class GAME():
    def __init__(self, display:pyg.display, game_state:dict):
        self.display = display
        self.game_state = game_state
        self.mouse_obj = _mou.MOUSE(self.display)
        self.util_obj = _util.utility(self.display)
        self.case_obj = _gen.CASE()
        self.fade_obj = _util.transition_image(self.display)
        self.parts = {
            "loaded":False,
            "tutorial":False,
            "gaming":False
            }
        self.timer = [0, 0]
        self.continue_input = False
        self.half_screen = (self.display.get_width()/2, self.display.get_height()/2)
        self.PLAYER_text_obj = _util.text_fonts(self.display, "lobato.ttf", 15, (10, self.half_screen[1]+45), "", False, "#000000")
        self.PLAYER_obj = _ply.PLAYER(self.display, self.PLAYER_text_obj)
        #? loading assets
        self.string_loading_text = "Loading assets please wait . . ."
        self.loading_text = _util.text_fonts(self.display, "N_E_B.ttf", 20, (self.half_screen[0], self.half_screen[1]), self.string_loading_text, False, "#999999")
        #? tutorial part
        self.string_tutorial_text = ""
        self.dialog_tutorial_text = [
            "Aperte [ESPACE] para continuar...",
            "Bem vindo Espector..",
            "seu objetivo é descobrir quem é inocente e quem é o assassino..",
            "você pode verificar as informações do suspeito, acusar ou interrogar qualquer suspeito no caso..",
            "no entanto, você tem um número determinado de interrogatórios, tenha cuidado Espector..",
            "agora vá Espector, já há um caso te esperando."
        ]
        self.tutorial_text = _util.text_fonts(self.display, "SpecialElite.ttf", 15, (10, self.half_screen[1]+45), self.string_tutorial_text, False, "#ffffff")
        self.npc_cop = _npc.COP_NPC(self.display, (self.half_screen[0], self.half_screen[1]+88), "tutorial_npc", self.tutorial_text)
        #? gaming part
        self.game_part = {
            "day_screen": True,
            "case_introduction": False,
            "suspects_list": False,
            "won":False,
            "lost": False
        }
        #* day screen
        self.day_string = f"DAY: {self.PLAYER_obj.player_info["day"]}"
        self.day_text = _util.text_fonts(self.display, "SEASRN__.ttf", 30, (self.half_screen[0], self.half_screen[1]), self.day_string, False, "#ffffff")
        self.continue_case = _util.text_fonts(self.display, "lobato.ttf", 10, (self.half_screen[0], self.half_screen[1]+20), "aperte [SPACE] para continuar", False, "#ffffff")
        #* case introduction
        self.dialog_instructions = [""]
        #* suspects list
        self.background_1img = pyg.image.load("src/IMAGES/scenes/background_suspects.png").convert()
        self.background_1rect = self.util_obj.get_rect(self.background_1img, (self.half_screen[0], self.half_screen[1]+90))
        self.choose_suspect_text = _util.text_fonts(self.display, "N_E_B.ttf", 20, (self.half_screen[0], self.half_screen[1]+45), "Choose a Suspect!", False, "#FFFFFF")
        self.suspects_text = _util.text_fonts(self.display, "Pixel-Noir.ttf", 10, (10, self.half_screen[1]+45), "", False, "#ffffff")
        self.npc_objs = []
        self.npc_selected = 0
        self.interrogate_text = _util.text_fonts(self.display, "Pixel-Noir.ttf", 5, self.half_screen, "Interrogar", False, "#ffffff")
        self.interrogate_button = _util.button_rect(self.display, (45,10), self.half_screen, "#000000", self.interrogate_text)
        self.acusar_text = _util.text_fonts(self.display, "Pixel-Noir.ttf", 5, self.half_screen, "Acusar", False, '#ffffff')
        self.acusar_button = _util.button_rect(self.display, (45,10), self.half_screen, "#000000", self.acusar_text)
        self.acusar_interrogate_buttons_apear = False
        #? WON
        self.won_dialog = [
            "Inspector...",
            "parece que você acertou neste caso..",
            "tem mais casos amanhã."
        ]
        #! lost
        self.lost_dialog = [
                "Inspertor...",
                "parece que você cometeu um erro neste caso..",
                "tente novamente amanhã."
            ]
    def loading_assets(self):
        self.display.blit(self.display, (0,0))
        self.display.fill("#454545")
        self.timer[0] += 1
        match self.timer[0]:
            case 18: self.loading_text.f_info["text"] = self.string_loading_text
            case 28: self.loading_text.f_info["text"] = "Loading assets please wait . ."
            case 38: self.loading_text.f_info["text"] = "Loading assets please wait ."
            case 48: self.loading_text.f_info["text"] = "Loading assets please wait"
            case 58: self.loading_text.f_info["text"] = "Loading assets please wait ."
            case 68: self.loading_text.f_info["text"] = "Loading assets please wait . ."
            case 78: self.loading_text.f_info["text"] = self.string_loading_text
            case 79:
                self.timer[0] = 0
                self.timer[1] += 1
        if self.timer[1] == 1:
            self.fade_obj.fade_in(45)
            if self.fade_obj.fade_alpha >= 255:
                self.parts["loaded"] = self.case_obj.generate_case()
                n = 0
                for i in range(len(self.case_obj.NPCS)):
                    if self.case_obj.NPCS[i]["TYPE"] == "Vitima": continue
                    n+=1
                    self.npc_objs.append(_npc.SUS_NPC(self.display, ((self.half_screen[0]-145)+(n*48), self.half_screen[1]+20), self.case_obj.NPCS[i], self.suspects_text))
        self.loading_text.render(False)
        self.loading_text.update()
    def tutorial_part(self):
        self.display.blit(self.display, (0,0))
        self.display.fill("#000000")
        if len(self.dialog_tutorial_text) == self.npc_cop.npc_dialog["part"]:
            self.fade_obj.fade_in(45)
            if self.fade_obj.fade_alpha >= 255:
                self.PLAYER_obj.player_info["tutorial_done"] = True
                self.npc_cop.npc_dialog["part"] = 0
                self.parts["tutorial"] = True
                self.parts["gaming"] = True
            return
        self.npc_cop.render()
        self.npc_cop.dialog(self.dialog_tutorial_text, self.continue_input)
        if self.continue_input: self.continue_input = False
        self.npc_cop.update()
        self.mouse_obj.render()
        self.mouse_obj.update(4)
        if self.fade_obj.fade_alpha >= 0: self.fade_obj.fade_out(3)
    def gaming_part(self):
        self.display.blit(self.display, (0,0))
        self.display.fill('#000000')
        if self.game_part["day_screen"]:
            if self.day_text.apear(15):
                if self.continue_input:
                    self.fade_obj.fade_in(45)
                    if self.fade_obj.fade_alpha >= 255:
                        self.continue_input = False
                        self.game_part["day_screen"] = False
                        self.game_part["case_introduction"] = True
                        self.npc_cop.npc_dialog["part"] = 0
                        return
                self.continue_case.apear(5)
                self.continue_case.render(False)
                self.continue_case.update()
            self.day_text.render(False)
            self.day_text.update()
            if self.fade_obj.fade_alpha >= 0: self.fade_obj.fade_out(3)
        elif self.game_part["case_introduction"]:
            self.display.blit(self.background_1img, self.background_1rect)
            if len(self.dialog_instructions) == self.npc_cop.npc_dialog["part"]:
                self.fade_obj.fade_in(45)
                if self.fade_obj.fade_alpha >= 255:
                    self.continue_input = False
                    self.game_part["case_introduction"] = False
                    self.game_part["suspects_list"] = True
                    self.npc_cop.npc_dialog["part"] = 0
                return
            if self.case_obj.CASO["DEATH_CASE"] == "Envenenado":
                self.dialog_instructions = [
                    "Boa noite Espector..",
                    f"hoje o caso {self.case_obj.CASO["DEATH_DIALOG"]}..",
                    "Os suspeitos são..",
                    f"{self.case_obj.NPCS[1]["NAME"]} é {self.case_obj.NPCS[1]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[1]["DESCRIPTION"]["PERSONALIDADE"]}",
                    f"{self.case_obj.NPCS[2]["NAME"]} é {self.case_obj.NPCS[2]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[2]["DESCRIPTION"]["PERSONALIDADE"]}",
                    f"{self.case_obj.NPCS[4]["NAME"]} é {self.case_obj.NPCS[4]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[4]["DESCRIPTION"]["PERSONALIDADE"]}",
                    f"{self.case_obj.NPCS[5]["NAME"]} é {self.case_obj.NPCS[5]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[5]["DESCRIPTION"]["PERSONALIDADE"]}",
                    f"O principal suspeito é {self.case_obj.NPCS[3]["NAME"]} é {self.case_obj.NPCS[3]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[3]["DESCRIPTION"]["PERSONALIDADE"]}..",
                    "faça a escolha certa Espector."
                ]
            if self.case_obj.CASO["DEATH_CASE"] == "Esfaqueado":
                self.dialog_instructions = [
                    "Boa noite Esppector..",
                    f"hoje o caso {self.case_obj.CASO["DEATH_DIALOG"]}..",
                    "Os suspeitos são..",
                    f"{self.case_obj.NPCS[1]["NAME"]} é {self.case_obj.NPCS[1]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[1]["DESCRIPTION"]["PERSONALIDADE"]}",
                    f"{self.case_obj.NPCS[2]["NAME"]} é {self.case_obj.NPCS[2]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[2]["DESCRIPTION"]["PERSONALIDADE"]}",
                    f"{self.case_obj.NPCS[3]["NAME"]} é {self.case_obj.NPCS[3]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[3]["DESCRIPTION"]["PERSONALIDADE"]}",
                    f"{self.case_obj.NPCS[5]["NAME"]} é {self.case_obj.NPCS[5]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[5]["DESCRIPTION"]["PERSONALIDADE"]}",
                    f"O principal suspeito é {self.case_obj.NPCS[0]["NAME"]} é {self.case_obj.NPCS[0]["DESCRIPTION"]["OCUPACAO"]}, {self.case_obj.NPCS[0]["DESCRIPTION"]["PERSONALIDADE"]}..",
                    "faça a escolha certa Espector."
                ]
            self.npc_cop.render()
            self.npc_cop.dialog(self.dialog_instructions, self.continue_input)
            if self.continue_input: self.continue_input = False
            self.npc_cop.update()
            if self.fade_obj.fade_alpha >= 0: self.fade_obj.fade_out(5)
        elif self.game_part["suspects_list"]:
            self.display.blit(self.background_1img, self.background_1rect)
            for i in range(len(self.case_obj.NPCS)-1):
                if self.npc_objs[i].selected:
                    match self.npc_objs[i].npc_info["DESCRIPTION"]["GENERO"][0].upper():
                        case "F":
                            self.npc_objs[i].type_int = 2
                        case "M":
                            self.npc_objs[i].type_int = 1
                else: self.npc_objs[i].type_int = 0
                self.npc_objs[i].render()
                self.npc_objs[i].update()
            for i in range(len(self.case_obj.NPCS)-1):
                if self.npc_objs[i].check_collision(self.mouse_obj) and self.mouse_obj.clicked:
                    new_pos = (self.npc_objs[i].npc_pos[0]+30, self.npc_objs[i].npc_pos[1]-40)
                    self.npc_selected = i
                    self.interrogate_button.b_pos = new_pos
                    self.interrogate_button.b_text_obj.f_pos = new_pos
                    self.interrogate_button.b_text_obj.f_animation["frame"] = 0
                    self.acusar_button.b_pos = (new_pos[0], new_pos[1]+20)
                    self.acusar_button.b_text_obj.f_pos = (new_pos[0], new_pos[1]+20)
                    self.acusar_button.b_text_obj.f_animation["frame"] = 0
                    self.acusar_interrogate_buttons_apear = True
                else: self.npc_objs[i].selected = False
            if self.acusar_interrogate_buttons_apear:
                self.npc_objs[self.npc_selected].selected = True
                #! INTERROGAR
                if self.interrogate_button.check_collision(self.mouse_obj):
                    self.interrogate_button.outline(2, "#000000")
                    self.interrogate_button.b_color = "#ffffff"
                    self.interrogate_button.b_text_obj.f_info["color"] = "#000000"
                else:
                    self.interrogate_button.outline(2, "#ffffff")
                    self.interrogate_button.b_color = "#000000"
                    self.interrogate_button.b_text_obj.f_info["color"] = "#ffffff"
                #! ACUSAR
                if self.acusar_button.check_collision(self.mouse_obj):
                    self.acusar_button.outline(2, "#000000")
                    self.acusar_button.b_color = "#ffffff"
                    self.acusar_button.b_text_obj.f_info["color"] = "#000000"
                    if self.npc_objs[self.npc_selected].npc_info["TYPE"] == "Assassino":
                        if self.mouse_obj.clicked:
                            self.fade_obj.fade_in(150)
                            if self.fade_obj.fade_alpha >= 255:
                                self.game_part["suspects_list"] = False
                                self.game_part["won"] = True
                                self.npc_selected = 0
                                self.npc_objs.clear()
                            return
                    else:
                        if self.mouse_obj.clicked:
                            self.fade_obj.fade_in(150)
                            if self.fade_obj.fade_alpha >= 255:
                                self.game_part["suspects_list"] = False
                                self.game_part["lost"] = True
                                self.npc_selected = 0
                                self.npc_objs.clear()
                            return
                else:
                    self.acusar_button.outline(2, "#ffffff")
                    self.acusar_button.b_color = "#000000"
                    self.acusar_button.b_text_obj.f_info["color"] = "#ffffff"
                self.interrogate_button.render(False, True, 5)
                self.interrogate_button.update()
                self.interrogate_button.b_text_obj.update()
                self.acusar_button.render(False, True, 5)
                self.acusar_button.update()
                self.acusar_button.b_text_obj.update()
            self.choose_suspect_text.apear(5)
            self.choose_suspect_text.render(False)
            self.choose_suspect_text.update()
            if self.fade_obj.fade_alpha >= 0: self.fade_obj.fade_out(3)
        elif self.game_part["won"]:
            if len(self.won_dialog) == self.npc_cop.npc_dialog["part"]:
                self.fade_obj.fade_in(50)
                if self.fade_obj.fade_alpha >= 255:
                    self.PLAYER_obj.player_info["day"] += 1
                    self.day_text.f_info["text"] = f"DAY: {self.PLAYER_obj.player_info["day"]}"
                    self.day_text.f_animation["frame"] = 0
                    self.day_text.update()
                    self.continue_input = False
                    self.parts["loaded"] = False
                    self.game_part["won"] = False
                    self.game_part["day_screen"] = True
                return
            self.npc_cop.render()
            self.npc_cop.dialog(self.won_dialog, self.continue_input)
            if self.continue_input: self.continue_input = False
            if self.fade_obj.fade_alpha >= 0: self.fade_obj.fade_out(3)
        elif self.game_part["lost"]:
            if len(self.lost_dialog) == self.npc_cop.npc_dialog["part"]:
                self.fade_obj.fade_in(50)
                if self.fade_obj.fade_alpha >= 255:
                    self.PLAYER_obj.player_info["day"] += 1
                    self.day_text.f_info["text"] = f"DAY: {self.PLAYER_obj.player_info["day"]}"
                    self.day_text.f_animation["frame"] = 0
                    self.day_text.update()
                    self.continue_input = False
                    self.parts["loaded"] = False
                    self.game_part["lost"] = False
                    self.game_part["day_screen"] = True
                return
            self.npc_cop.render()
            self.npc_cop.dialog(self.lost_dialog, self.continue_input)
            if self.continue_input: self.continue_input = False
            if self.fade_obj.fade_alpha >= 0: self.fade_obj.fade_out(3)
        self.mouse_obj.render()
        self.mouse_obj.update(4)
    def render(self):
        if not self.parts["loaded"]:
            self.loading_assets()
        elif not self.parts["tutorial"] and not self.PLAYER_obj.player_info["tutorial_done"]:
            self.tutorial_part()
        elif self.parts["gaming"]:
            self.gaming_part()
        for event in pyg.event.get():
            self.events(event)
    def events(self, event: pyg.event):
        if event.type == pyg.QUIT: self.end()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_SPACE:
                if not self.parts["tutorial"] or self.parts["gaming"]: self.continue_input = True
        if event.type == pyg.KEYUP:
            if event.key == pyg.K_SPACE: self.contniue_input = False
        if event.type == pyg.MOUSEBUTTONDOWN:
            self.mouse_obj.clicked = True
        if event.type == pyg.MOUSEBUTTONUP:
            self.mouse_obj.clicked = False
    def end(self):
        print("GAME ending!")
        pyg.quit()
        sys.exit()