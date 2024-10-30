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
        self.f_info = {
            "font":font_ttf,
            "size":size,
            "text":text,
            "antialias":antialias,
            "color":color
        }
        self.f_pos = pos
        self.f_path = self.json_object.paths["PATH-FONTS"]
        self.f_obj = _pyg.font.Font(self.f_path+self.f_info["font"], self.f_info["size"])
        self.f_surface = self.f_obj.render(self.f_info["text"], self.f_info["antialias"], self.f_info["color"]).convert()
        self.f_rect = self.f_surface.get_rect(center = self.f_pos)
    def draw_rect(self, color:str, border_rad:int):
        return _pyg.draw.rect(self.display, color, self.f_rect, border_radius=border_rad)
    def render(self):
        self.display.blit(self.f_surface, self.f_rect)
    def update(self):
        self.f_obj = _pyg.font.Font(self.f_path+self.f_info["font"], self.f_info["size"])
        self.f_surface = self.f_obj.render(self.f_info["text"], self.f_info["antialias"], self.f_info["color"]).convert()
        self.f_rect = self.f_surface.get_rect(center = self.f_pos)

class button_rect():
    def __init__(self, display: _pyg.Surface, size: tuple, pos: tuple, color:str, text_obj:text_fonts):
        self.display = display
        self.b_size = size
        self.b_pos = pos
        self.b_color = color
        self.b_text_obj = text_obj
        self.b_surface = _pyg.Surface(self.b_size).convert()
        self.b_surface.fill(self.b_color)
        self.b_rect = self.b_surface.get_rect(center=self.b_pos)
        self.b_mask = _pyg.mask.from_surface(self.b_surface)
    def render(self):
        self.display.blit(self.b_surface, self.b_rect)
        self.display.blit(self.b_text_obj.f_surface, self.b_text_obj.f_rect)
    def check_collision(self, m_obj: _mous.MOUSE) -> bool:
        if self.b_mask.overlap(m_obj.mask, (m_obj.pos[0] - self.b_rect.x, m_obj.pos[1] - self.b_rect.y)):
            return True
        return False
    def update(self):
        self.b_surface = _pyg.Surface(self.b_size).convert()
        self.b_surface.fill(self.b_color)
        self.b_rect = self.b_surface.get_rect(center=self.b_pos)
        self.b_mask = _pyg.mask.from_surface(self.b_surface)
