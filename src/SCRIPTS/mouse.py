#imports external
import pygame as pyg
#imports internal
...
class MOUSE():
    def __init__(self, display:pyg.display)->None:
        self.display = display
        self.pos = pyg.mouse.get_pos()
        self.surface = pyg.image.load('src\IMAGES\mouse.png').convert_alpha()
        self.rect = self.surface.get_rect(center=(self.pos[0], self.pos[1]))
        self.mask = pyg.mask.from_surface(self.surface)
        self.clicked=False
    def update(self, size_scale):
        self.pos = pyg.mouse.get_pos()
        self.pos = (self.pos[0]/size_scale, self.pos[1]/size_scale)
        self.rect.center = (self.pos[0], self.pos[1])
    def render(self):
        return self.display.blit(self.surface, self.rect)