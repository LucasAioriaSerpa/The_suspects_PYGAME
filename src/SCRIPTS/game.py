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
        self.dialog_tutorial_text = ["Aperte [ESPACE] para continuar...",
                                "Bem vindo Espector..",
                                "seu objetivo é descobrir quem é inocente e quem é o assassino..",
                                "você pode verificar as informações do suspeito, acusar ou interrogar qualquer suspeito no caso..",
                                "no entanto, você tem um número determinado de interrogatórios, tenha cuidado Espector..",
                                "agora vá Espector, já há um caso te esperando."]
        self.tutorial_text = _util.text_fonts(self.display, "SpecialElite.ttf", 15, (10, self.half_screen[1]+45), self.string_tutorial_text, False, "#ffffff")
        self.npc_tutorial = _npc.NPC(self.display, (self.half_screen[0], self.half_screen[1]+88), "tutorial_npc", self.tutorial_text)
        #? gaming part
        self.gaming_part = {
            "day_screen": True,
            "case_introduction": False,
            "suspects_list": False,
            "interrogatory": False,
            "won":False,
            "lost": False
        }
        #* day screen
        self.day_string = self.PLAYER_obj.player_info["day"]
        self.day_text = _util.text_fonts(self.display, "N_E_B.ttf", 20, (self.half_screen[0], self.half_screen[1]), self.day_string, False, "#ffffff")
        #* case introduction
        #* suspects list
        self.background_1img = pyg.image.load("src/IMAGES/scenes/background_suspects.png").convert()
        self.background_1rect = self.util_obj.get_rect(self.background_1img, (self.half_screen[0], self.half_screen[1]+80))
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
        if self.timer[1] == 1: self.parts["loaded"] = self.case_obj.generate_case()
        self.loading_text.render(False)
        self.loading_text.update()
    def tutorial_part(self):
        self.display.blit(self.display, (0,0))
        self.display.fill("#000000")
        if len(self.dialog_tutorial_text) == self.npc_tutorial.npc_dialog["part"]:
            self.parts["tutorial"] = True
            self.parts["gaming"] = True
            return
        self.npc_tutorial.render()
        self.npc_tutorial.dialog(self.dialog_tutorial_text, self.continue_input)
        if self.continue_input: self.continue_input = False
        self.npc_tutorial.update()
        self.mouse_obj.render()
        self.mouse_obj.update(4)
    def gaming_part(self):
        if self.gaming_part["day_screen"]:
            self.display.blit(self.display, (0,0))
            self.display.fill("#000000")
            self.day_text.render(False)
            self.day_text.update()
    def render(self):
        if not self.parts["loaded"]:
            self.loading_assets()
        elif not self.parts["tutorial"]:
            self.tutorial_part()
        elif self.parts["gaming"]:
            self.gaming_part()
        for event in pyg.event.get():
            self.events(event)
    def events(self, event: pyg.event):
        if event.type == pyg.QUIT: self.end()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_SPACE:
                if self.part["tutorial"]: self.continue_input = True
        if event.type == pyg.KEYUP:
            if event.key == pyg.K_SPACE:
                if self.part["tutorial"]: self.contniue_input = False
        if event.type == pyg.MOUSEBUTTONDOWN:
            self.mouse_obj.clicked = True
        if event.type == pyg.MOUSEBUTTONUP:
            self.mouse_obj.clicked = False
    def end(self):
        print("Menu ending!")
        pyg.quit()
        sys.exit()