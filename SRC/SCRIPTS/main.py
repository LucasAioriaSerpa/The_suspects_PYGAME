#imports
import pygame as _pyg, sys
print("IMPORTS LOADED!")
class Game():
    def __init__(self):
        self.RESOLUTION = (1200, 750)
        self.BACKGROUND_COLOR = "#000000"
        self.FPS = 60
        self.game_state = {
            'Menu': False,
            'Game': True,
            'Game_over': False
        }
        #?criar variaveis aqui
        self.var_game = ...
        ...
        #?inicializando pygame
        _pyg.init()
        _pyg.display.set_caption("Project ttg")
        self.screen = _pyg.display.set_mode(self.RESOLUTION)
        self.display = _pyg.Surface((self.screen.get_width()/2, self.screen.get_height()/2)).convert()
        self.clock = _pyg.time.Clock()
    def run(self):
        while True:
            if self.game_state['Game']:
                self.display.fill(self.BACKGROUND_COLOR)
                #? render
                ...
                #? logic/conditions
                ...
            #? check events in pygame
            for event in _pyg.event.get():
                if event.type == _pyg.QUIT: self.end()
                if event.type == _pyg.KEYDOWN:
                    if event.key == _pyg.K_ESCAPE: self.end()
                    if self.game_state['Game']:
                        print("butões sendo apertados...")
            self.screen.blit(_pyg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.clock.tick(self.FPS)
            _pyg.display.update()
    def end(self):
        print("Game ending!")
        _pyg.quit()
        sys.exit()

print("main.py loaded!")
