#imports external
import pygame as pyg
#imports internal
import SCRIPTS.load_json as _json
import SCRIPTS.mouse as _mous
class utility():
    def __init__(self, display:pyg.Surface):
        self.json_data = _json.CONFIG()
        self.json_data.create_config()
        self.PATH = self.json_data.paths
        self.display = display
    def image_load(self, folder:str, file_name:str) -> pyg.surface:
        return pyg.image.load(self.PATH[folder]+file_name).convert()
    def get_rect(self, surface: pyg.Surface, vector2: pyg.Vector2) -> pyg.Rect:
        return surface.get_rect(midbottom = (vector2))
    def font_rect(self, surface: pyg.Surface, pos: float):
        return surface.get_rect(center = pos)
class transition_image():
    def __init__(self, display: pyg.Surface) -> None:
        self.display = display
        self.fade_alpha = 0
        self.cordinates = (display.get_width(), display.get_height())
        self.fade_surface = pyg.Surface(self.cordinates).convert()
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
    def __init__(self, display: pyg.Surface, font_ttf: str, size: int, pos: tuple, text: str, antialias: bool, color: str):
        self.display = display
        self.json_object = _json.CONFIG()
        self.json_object.create_config()
        self.f_info = {
            "font":font_ttf,
            "size":size,
            "text":text,
            "antialias":antialias,
            "color":color,
        }
        self.f_animation = {
            "done": False,
            "frame": 0
        }
        self.f_pos = pos
        self.f_path = self.json_object.paths["PATH-FONTS"]
        self.f_obj = pyg.font.Font(self.f_path+self.f_info["font"], self.f_info["size"])
        self.f_surface = self.f_obj.render(self.f_info["text"], self.f_info["antialias"], self.f_info["color"]).convert()
        self.f_rect = self.f_surface.get_rect(center = self.f_pos)
    def draw_rect(self, color:str, border_rad:int):
        return pyg.draw.rect(self.display, color, self.f_rect, border_radius=border_rad)
    def long_text_dialog(self, speed: int):
        list_words = [word.split(" ") for word in self.f_info["text"].splitlines()]
        space_height = self.f_obj.size(" ")[0]
        x,y = self.f_pos
        highlight_color = self.f_info["color"]
        for lines in list_words:
            for words in lines:
                if words == "envenenado(a)":
                    highlight_color = "#00FF00"
                elif words == "esfaqueado(a)":
                    highlight_color = "#FF0000"
                else: highlight_color = self.f_info["color"]
                self.f_surface = self.f_obj.render(words, self.f_info["antialias"], highlight_color).convert()
                word_pos = self.f_surface.get_size()
                if x + word_pos[0] >= self.display.get_width():
                    x = self.f_pos[0]
                    y += word_pos[1]
                blank = ""
                if self.f_animation["frame"] < speed * len(words):
                    self.f_animation["frame"] += 1
                    blank = words[0:self.f_animation["frame"]//speed]
                    self.f_surface = self.f_obj.render(blank, self.f_info["antialias"], highlight_color).convert()
                elif self.f_animation["frame"] >= speed * len(words):
                    self.f_animation["done"] = True
                self.display.blit(self.f_surface, (x,y))
                x += word_pos[0] + space_height
        return True
    def apear(self, speed: int):
        blank = ""
        if self.f_animation["frame"] < speed * len(self.f_info["text"]):
            self.f_animation["frame"] += 1
            blank = self.f_info["text"][0:self.f_animation["frame"]//speed]
        elif self.f_animation["frame"] >= speed * len(self.f_info["text"]):
            self.f_animation["done"] = True
            return True
        self.f_obj = pyg.font.Font(self.f_path+self.f_info["font"], self.f_info["size"])
        self.f_surface = self.f_obj.render(blank, self.f_info["antialias"], self.f_info["color"]).convert()
        self.f_rect = self.f_surface.get_rect(center = self.f_pos)
    def render(self, by_pos: bool):
        if by_pos: return self.display.blit(self.f_surface, self.f_pos)
        self.display.blit(self.f_surface, self.f_rect)
    def update(self):
        self.f_obj = pyg.font.Font(self.f_path+self.f_info["font"], self.f_info["size"])
        self.f_surface = self.f_obj.render(self.f_info["text"], self.f_info["antialias"], self.f_info["color"]).convert()
        self.f_rect = self.f_surface.get_rect(center = self.f_pos)
class button_rect():
    def __init__(self, display: pyg.Surface, size: tuple, pos: tuple, color:str, text_obj:text_fonts):
        self.display = display
        self.b_size = size
        self.b_pos = pos
        self.b_color = color
        self.b_text_obj = text_obj
        self.b_surface = pyg.Surface(self.b_size).convert()
        self.b_surface.fill(self.b_color)
        self.b_rect = self.b_surface.get_rect(center=self.b_pos)
        self.b_mask = pyg.mask.from_surface(self.b_surface)
    def outline(self, size:int, color: str):
        outline_surface_pos = (self.b_pos[0], self.b_pos[1])
        outline_surface_size = (self.b_size[0]+size, self.b_size[1]+size)
        outline_surface = pyg.Surface(outline_surface_size).convert()
        outline_surface.fill(color)
        outline_surface_rect = outline_surface.get_rect(center=outline_surface_pos)
        self.display.blit(outline_surface, outline_surface_rect)
    def render(self, by_pos: bool, apear: bool, speed: int):
        self.display.blit(self.b_surface, self.b_rect)
        if apear: self.b_text_obj.apear(speed)
        if by_pos: return self.b_text_obj.render(True)
        self.b_text_obj.render(False)
    def check_collision(self, m_obj: _mous.MOUSE) -> bool:
        if self.b_mask.overlap(m_obj.mask, (m_obj.pos[0] - self.b_rect.x, m_obj.pos[1] - self.b_rect.y)):
            return True
        return False
    def update(self):
        self.b_surface = pyg.Surface(self.b_size).convert()
        self.b_surface.fill(self.b_color)
        self.b_rect = self.b_surface.get_rect(center=self.b_pos)
        self.b_mask = pyg.mask.from_surface(self.b_surface)