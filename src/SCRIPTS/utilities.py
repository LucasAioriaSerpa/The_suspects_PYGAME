#imports
import pygame as _pyg
class utility():
    def __init__(self, display:_pyg.Surface):
        self.PATH = {
            'PATH': "src/",
            'AUDIOS': "src/AUDIOS/",
            'FONTS': "src/FONTS/",
            'IMAGES': "src/IMAGES/"
        }
        self.display = display
    def image_load(self, folder:str, file_name:str) -> _pyg.surface:
        return _pyg.image.load(self.PATH[folder]+file_name).convert()
    def get_rect(self, surface: _pyg.Surface, vector2: _pyg.Vector2) -> _pyg.Rect:
        return surface.get_rect(midbottom = (vector2))
    def font_rect(self, surface: _pyg.Surface, pos: float):
        return surface.get_rect(center = pos)
class Mouse():
    def __init__(self, display: _pyg.surface):
        self.display = display
        self.pos = _pyg.mouse.get_pos()
        self.surface = utility(display).image_load('IMAGE','.png')
        self.rect = self.surface.get_rect(center=(self.pos[0], self.pos[1]))
        self.mask = _pyg.mask.from_surface(self.surface)
        self.clicked = False
    def update(self):
        self.pos = _pyg.mouse.get_pos()
        self.pos = (self.pos[0]/2, self.pos[1]/2)
        self.rect.center = (self.pos[0], self.pos[1])
    def render(self):
        return self.display.blit(self.surface, self.rect)