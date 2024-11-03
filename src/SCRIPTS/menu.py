#imports external
import pygame as pyg, sys
#imports internal
import SCRIPTS.mouse as _mou
import SCRIPTS.utilities as _util
class MENU():
    def __init__(self, display:pyg.display, game_state: dict    ):
        self.display = display
        self.game_state = game_state
        self.mouse_obj = _mou.MOUSE(self.display)
        self.util_obj = _util.utility(self.display)
        self.half_screen = (self.display.get_width()/2, self.display.get_height()/2)
        self.title_text = _util.text_fonts(self.display, "SEASRN__.ttf", 30, (self.half_screen[0], self.half_screen[1]-30), "The Suspects", False, "#ffffff")
        self.start_text = _util.text_fonts(self.display, "upheavtt.ttf", 20, (self.half_screen[0], self.half_screen[1]+20), "START", False, "#999999")
        self.start_button = _util.button_rect(self.display, (128,32), (self.half_screen[0], self.half_screen[1]+20), "#454545", self.start_text)
        self.exit_text = _util.text_fonts(self.display, "upheavtt.ttf", 20, (self.half_screen[0], self.half_screen[1]+60), "SAIR", False, "#999999")
        self.exit_button = _util.button_rect(self.display, (128,32), (self.half_screen[0], self.half_screen[1]+60), "#454545", self.exit_text)
    def render(self):
        self.display.blit(self.display, (0,0))
        self.display.fill("#000000")
        if self.start_button.check_collision(self.mouse_obj):
            self.start_button.b_color = "#ffffff"
            self.start_button.b_text_obj.f_info["color"] = "#000000"
            if self.mouse_obj.clicked:
                self.game_state["Menu"] = False
                self.game_state["Game"] = True
                return self.game_state
        else:
            self.start_button.b_color = "#454545"
            self.start_button.b_text_obj.f_info["color"] = "#999999"

        if self.exit_button.check_collision(self.mouse_obj):
            self.exit_button.b_color = "#ffffff"
            self.exit_button.b_text_obj.f_info["color"] = "#000000"
            if self.mouse_obj.clicked: self.end()
        else:
            self.exit_button.b_color = "#454545"
            self.exit_button.b_text_obj.f_info["color"] = "#999999"
        self.title_text.render(False)
        self.start_button.render(False)
        self.start_button.update()
        self.start_button.b_text_obj.update()
        self.exit_button.render(False)
        self.exit_button.update()
        self.exit_button.b_text_obj.update()
        self.mouse_obj.render()
        self.mouse_obj.update(4)
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