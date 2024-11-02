#imports external
import pygame as pyg, sys
#imports internal
import SCRIPTS.mouse as _mou
import SCRIPTS.utilities as _util
import SCRIPTS.generate_case as _gen
import SCRIPTS.NPCs as _npc
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
        self.half_screen = (self.display.get_width()/2, self.display.get_height()/2)
        #? loading assets
        self.string_loading_text = "Loading assets please wait . . ."
        self.loading_text = _util.text_fonts(self.display, "N_E_B.ttf", 20, (self.half_screen[0], self.half_screen[1]), self.string_loading_text, False, "#999999")
        #? tutorial part
        self.string_tutorial_text = ""
        self.tutorial_text = _util.text_fonts(self.display, "N_E_B.ttf", 20, (self.half_screen[0], self.half_screen[1]+65), self.string_tutorial_text, False, "#ffffff")
        self.cop_npc = ...
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
        self.loading_text.render()
        self.loading_text.update()
    def tutorial_part(self):
        self.display.blit(self.display, (0,0))
        self.display.fill("#000000")
        npc_tutorial = _npc.NPC(self.display, (self.half_screen[0], self.half_screen[1]+88), "tutorial_npc", self.tutorial_text)
        npc_tutorial.render()
        npc_tutorial.dialog(["Bem vindo Espector!","Aperte ESPACE para continuar"], False)
        npc_tutorial.update()
        self.mouse_obj.render()
        self.mouse_obj.update(4)
    def render(self):
        if self.parts["loaded"]==False:
            self.loading_assets()
        elif self.parts["tutorial"]==False:
            self.tutorial_part()
        elif self.parts["gaming"]:
            self.display.blit(self.display, (0,0))
            self.display.fill("#000000")
            self.mouse_obj.render()
            self.mouse_obj.update(4)
        for event in pyg.event.get():
            if event.type == pyg.QUIT: self.end()
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_SPACE: print("NEXT!")
            if event.type == pyg.MOUSEBUTTONDOWN:
                self.mouse_obj.clicked = True
            if event.type == pyg.MOUSEBUTTONUP:
                self.mouse_obj.clicked = False
    def end(self):
        print("Menu ending!")
        pyg.quit()
        sys.exit()