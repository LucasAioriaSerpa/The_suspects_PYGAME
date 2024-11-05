#imports external
import pygame as pyg, sys
#imports internal
import SCRIPTS.utilities as _util
import SCRIPTS.menu as _menu
import SCRIPTS.game as _game
import SCRIPTS.load_json as _json
import SCRIPTS.mouse as _mou
class Game:
    def __init__(self):
        #? json configs
        self.json_data = _json.CONFIG()
        self.json_data.create_config()
        #? game configs
        self.GAME_CONFIG = self.json_data.game_config
        self.RESOLUTION = (self.GAME_CONFIG["RESOLUTION"][0], self.GAME_CONFIG["RESOLUTION"][1])
        self.BACKGROUND_COLOR = self.GAME_CONFIG["BACKGROUND"]
        self.FPS = self.GAME_CONFIG["FPS"]
        self.game_state = self.GAME_CONFIG["GAME_STATE"]
        self.size_scale = 4
        #?inicializando pygame
        pyg.init()
        pyg.mouse.set_visible(False)
        pyg.display.set_caption("Project ttg")
        icon_game = pyg.image.load("src/IMAGES/icon_THESUS.png")
        pyg.display.set_icon(icon_game)
        self.screen = pyg.display.set_mode(self.RESOLUTION)
        self.display = pyg.Surface((self.screen.get_width()/self.size_scale, self.screen.get_height()/self.size_scale)).convert()
        self.clock = pyg.time.Clock()
        #? objects
        self.mouse_obj = _mou.MOUSE(self.display)
        self.objs_states = {
            "menu":_menu.MENU(self.display, self.game_state),
            "game":_game.GAME(self.display, self.game_state)
        }
        self.objs_util = _util.utility(self.display)
    def run(self):
        while True:
            if self.game_state['Menu']: self.objs_states["menu"].render()
            if self.game_state['Game']: self.objs_states["game"].render()
            #? check events in pygame
            for event in pyg.event.get():
                if event.type == pyg.QUIT: self.end()
            self.screen.blit(pyg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.clock.tick(self.FPS)
            pyg.display.update()
    def end(self):
        print("Main ending!")
        pyg.quit()
        sys.exit()
print("main.py loaded!")