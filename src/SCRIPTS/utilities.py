#imports external
import pygame as _pyg
#imports internal
...
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
