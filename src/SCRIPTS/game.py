#imports external
import pygame as pyg, sys
#imports internal
import SCRIPTS.mouse as _mou
import SCRIPTS.utilities as _util
import SCRIPTS.generate_case as _gen
class GAME():
    def __init__(self, display:pyg.display, game_state:dict):
        self.display = display
        self.game_state = game_state
        self.loaded = False
        self.mouse_obj = _mou.MOUSE(self.display)
        self.util_obj = _util.utility(self.display)
        self.case_obj = _gen.CASE(self.display)
        self.half_screen = (self.display.get_width()/2, self.display.get_height()/2)
        self.timer = 0
        self.loading_text = _util.text_fonts(self.display, "N_E_B.ttf", 20, (self.half_screen[0], self.half_screen[1]), "Loading assets please wait . . .", False, "#999999")
    def loading_assets(self):
        self.display.blit(self.display, (0,0))
        self.display.fill("#454545")
        self.timer += 1
        match self.timer:
            case 18: self.loading_text.f_info["text"] = "Loading assets please wait . . ."
            case 28: self.loading_text.f_info["text"] = "Loading assets please wait . ."
            case 38: self.loading_text.f_info["text"] = "Loading assets please wait ."
            case 48: self.loading_text.f_info["text"] = "Loading assets please wait"
            case 58: self.loading_text.f_info["text"] = "Loading assets please wait ."
            case 68: self.loading_text.f_info["text"] = "Loading assets please wait . ."
            case 78: self.loading_text.f_info["text"] = "Loading assets please wait . . ."
            case 79: self.timer = 0
        self.loading_text.render()
        self.loading_text.update()
    def render(self):
        if self.loaded:
            self.display.blit(self.display, (0,0))
            self.display.fill("#000000")
            self.mouse_obj.render()
            self.mouse_obj.update(4)
        else: self.loading_assets()
        for event in pyg.event.get():
            if event.type == pyg.QUIT: self.end()
            if event.type == pyg.MOUSEBUTTONDOWN:
                self.mouse_obj.clicked = True
            if event.type == pyg.MOUSEBUTTONUP:
                self.mouse_obj.clicked = False
    def end(self):
        print("Menu ending!")
        pyg.quit()
        sys.exit()