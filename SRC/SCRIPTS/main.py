#imports
import pygame as _pyg, sys, time
print("IMPORTS LOADED!")

class GAME():
    def __init__(self):
        self.RESOLUTION = (1200, 750)
        self.BACKGROUND_COLOR = "#000000"
        self.FPS = 60

        self.game_state = {
            'Game': True,
            'Game_over': False,
            'Gane_won': False
        }

        self.var_game = ... # criar variaveis aqui
        ...

        _pyg.init()
        _pyg.display.set_caption("Project ttg")
        self.screen = _pyg.display.set_mode(self.RESOLUTION)
        self.display = _pyg.Surface((self.screen.get_width()/2, self.screen.get_height()/2)).convert()
        self.clock = _pyg.time.Clock()
        self.last_time = time.time()

    def run(self):
        while True:
            ...
        ...
