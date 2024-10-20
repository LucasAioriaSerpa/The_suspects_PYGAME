#imports external
import pygame as pyg, sys
#imports internal
import SCRIPTS.utilities as _util
import SCRIPTS.menu as _menu
import SCRIPTS.game as _game
class Game():
    def __init__(self):
        self.RESOLUTION = (1200, 750)
        self.BACKGROUND_COLOR = "#000000"
        self.FPS = 60
        self.game_state = {
            'Menu': True,
            'Game': False,
            'Game_over': False
        }
        #?inicializando pygame
        pyg.init()
        pyg.mouse.set_visible(False)
        pyg.display.set_caption("Project ttg")
        self.screen = pyg.display.set_mode(self.RESOLUTION)
        self.display = pyg.Surface((self.screen.get_width()/2, self.screen.get_height()/2)).convert()
        self.clock = pyg.time.Clock()
        self.objs_states = {
            "menu":_menu.MENU(self.display, self.game_state),
            "game":_game.GAME(self.display, self.game_state)
        }
    def run(self):
        while True:
            if self.game_state['Menu']: self.objs_states["menu"].render()
            if self.game_state['Game']: self.objs_states["game"].render()
            #? check events in pygame
            for event in pyg.event.get():
                if event.type == pyg.QUIT: self.end()
                self.event_key(event)
            self.screen.blit(pyg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.clock.tick(self.FPS)
            pyg.display.update()
    def event_key(self, event:pyg.event):
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE: self.end()
            if self.game_state['Game']: print("butões sendo apertados")
    def end(self):
        print("Game ending!")
        pyg.quit()
        sys.exit()
print("main.py loaded!")