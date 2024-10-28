#imports external
import pygame as pyg
#imports internal
import SCRIPTS.mouse as _mou
class MENU():
    def __init__(self, display:pyg.display, game_state:dict):
        self.display = display
        self.game_state = game_state
        self.mouse_obj = _mou.MOUSE(self.display)
    def render(self):
        self.display.blit(self.display, (0,0))
        self.display.fill("#000000")
        self.mouse_obj.render()
        self.mouse_obj.update(4)