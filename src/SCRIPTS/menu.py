#imports external
import pygame as pyg
#imports internal
import mouse as _mou
class MENU():
    def __init__(self, display:pyg.display, game_state:dict):
        self.display = display
        self.game_state = game_state
        self.mouse_obj = _mou.MOUSE(self.display)
    def render(self):
        self.mouse_obj.update(1)
        self.render()