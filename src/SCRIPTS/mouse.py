#imports external
import pygame as pyg
#imports internal
import SCRIPTS.load_json as _json
class MOUSE():
    def __init__(self, display:pyg.display) -> None:
        self.display = display
        self.json_object = _json.CONFIG()
        self.json_object.create_config()
        self.path_mouse = self.json_object.paths["PATH-IMAGES-mouse"]
        self.pos = pyg.mouse.get_pos()
        self.surface = pyg.image.load(self.path_mouse+"mouse.png").convert_alpha()
        self.rect = self.surface.get_rect(center=(self.pos[0], self.pos[1]))
        self.mask = pyg.mask.from_surface(self.surface)
        self.clicked = False
    def update(self, size_scale):
        self.pos = pyg.mouse.get_pos()
        self.pos = (self.pos[0]/size_scale, self.pos[1]/size_scale)
        self.rect.center = (self.pos[0], self.pos[1])
    def render(self):
        return self.display.blit(self.surface, self.rect)