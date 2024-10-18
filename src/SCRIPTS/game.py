#imports external
import pygame as pyg
#imports internal
...
class GAME():
    def __init__(self, display:pyg.display, game_state:dict):
        self.display = display
        self.game_state = game_state
    def render(self):
        print("rendering!")