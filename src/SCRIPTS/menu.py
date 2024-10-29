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
    def render(self):
        self.display.blit(self.display, (0,0))
        self.display.fill("#000000")

        text_test = _util.text_fonts(self.display, "upheavtt.ttf", 25, (self.display.get_width()/2, self.display.get_height()/2), "test", False, "#000000")
        button_test = _util.button_rect(self.display, (100,100), (self.display.get_width()/2, self.display.get_height()/2), "#FFFFFF", text_test)
        text_test.font_position = button_test.b_pos
        button_test.render()
        if button_test.check_collision(self.mouse_obj):
            text_test.f_info["color"] = "#ffffff"
            button_test.collision_change(self.mouse_obj, "#000000", text_test.f_info)
            button_test.render()
            if self.mouse_obj.clicked:
                print("test!!!")

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