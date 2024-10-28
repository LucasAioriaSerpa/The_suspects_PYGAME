#imports external
import pygame as _pyg
#imports internal
import SCRIPTS.load_json as _json
import SCRIPTS.mouse as _mous
class utility():
    def __init__(self, display:_pyg.Surface):
        self.json_data = _json.CONFIG()
        self.json_data.create_config()
        self.PATH = self.json_data.paths
        self.display = display
    def image_load(self, folder:str, file_name:str) -> _pyg.surface:
        return _pyg.image.load(self.PATH[folder]+file_name).convert()
    def get_rect(self, surface: _pyg.Surface, vector2: _pyg.Vector2) -> _pyg.Rect:
        return surface.get_rect(midbottom = (vector2))
    def font_rect(self, surface: _pyg.Surface, pos: float):
        return surface.get_rect(center = pos)

class transition_image():
    def __init__(self, display: _pyg.Surface) -> None:
        self.display = display
        self.fade_alpha = 0
        self.cordinates = (display.get_width(), display.get_height())
        self.fade_surface = _pyg.Surface().convert()
        self.fade_surface.fill("#000000")
        self.fade_surface.set_alpha(self.fade_alpha)
    def fade_in(self, speed):
        self.fade_alpha += speed
        self.fade_surface.set_alpha(self.fade_alpha)
        self.display.blit(self.fade_surface, (0,0))
    def fade_out(self, speed):
        self.fade_alpha -= speed
        self.fade_surface.set_alpha(self.fade_alpha)
        self.display.blit(self.fade_surface, (0,0))

class text_fonts():
    def __init__(self, display: _pyg.Surface, font_ttf: str, size: int, pos: tuple, text: str, antialias: bool, color: str):
        self.display = display
        self.json_object = _json.CONFIG()
        self.json_object.create_config()
        self.path_font = self.json_object.paths["PATH-FONTS"]
        self.font_obj = _pyg.font.Font(self.path_font+font_ttf, size)
        self.font_surface = self.font_obj.render(text, antialias, color).convert()
        self.font_pos = pos
        self.font_rect = self.font_surface.get_rect(center = self.font_pos)
    def draw_rect(self, color:str, size:int):
        return _pyg.draw.rect(self.display, color, self.font_rect, border_radius=size)

class button_rect():
    def __init__(self, display: _pyg.Surface, size: tuple, pos: tuple, color:str, text_obj:text_fonts):
        self.display = display
        self.text_obj = text_obj
        self.surface = _pyg.Surface(size).convert()
        self.color = color
        self.fill = self.surface.fill(color)
        self.rect = self.surface.get_rect(center=pos)
        self.mask = _pyg.mask.from_surface(self.surface)
    def render(self):
        self.display.blit(self.surface, self.rect)
        self.display.blit(self.text_obj.font_surface, self.text_obj.font_rect)
    def check_collision(self, m_obj: _mous.MOUSE, color: str):
        self.surface.fill(self.color)
        if self.mask.overlap(m_obj.mask, (m_obj.pos[0] - self.rect.x, m_obj.pos[1] - self.rect.y)):
            self.surface.fill(color)
            self.render()
