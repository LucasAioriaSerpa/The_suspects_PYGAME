#imports external
import pygame as pyg
#import internal
import SCRIPTS.utilities as _util
class NPC():
    def __init__(self, display: pyg.display, pos: tuple, name: str, text_obj: _util.text_fonts):
        self.display = display
        self.npc_pos = pos
        self.npc_name = name
        self.text_obj = text_obj
        self.util_obj = _util.utility(display)
        self.npc_dialog = {
            "part": 0,
            "done_part": False
        }
        self.npc_surface_img = self.util_obj.image_load("PATH-IMAGES-characteres","NPCs/cop.png")
        self.npc_rect = self.util_obj.get_rect(self.npc_surface_img, self.npc_pos)
        self.npc_mask = pyg.mask.from_surface(self.npc_surface_img)
    def dialog(self, list_dialog: list[str], continue_dialog: bool):
        outline_block_pos = (self.display.get_width()/2, self.display.get_height())
        outline_block_size = (self.display.get_width(), 110)
        outline_block_text = pyg.Surface(outline_block_size).convert()
        outline_block_text.fill("#ffffff")
        outline_block_rect = outline_block_text.get_rect(center=outline_block_pos)
        block_pos = (self.display.get_width()/2, self.display.get_height())
        block_size = (self.display.get_width()-10, 100)
        block_text = pyg.Surface(block_size).convert()
        block_text.fill("#000000")
        block_rect = block_text.get_rect(center=block_pos)
        self.display.blit(outline_block_text, outline_block_rect)
        self.display.blit(block_text, block_rect)
        self.text_obj.f_info["text"] = list_dialog[self.npc_dialog["part"]]
        if continue_dialog and self.npc_dialog["done_part"] and self.npc_dialog["part"] < len(list_dialog):
            self.npc_dialog["part"] += 1
            self.npc_dialog["done_part"] = False
            return
        self.npc_dialog["done_part"] = self.text_obj.apear(5)
        self.text_obj.render(True)
        self.text_obj.update()
    def render(self):
        self.display.blit(self.npc_surface_img, self.npc_rect)
    def update(self):
        self.npc_surface_img = self.util_obj.image_load("PATH-IMAGES-characteres","NPCs/cop.png")
        self.npc_rect = self.util_obj.get_rect(self.npc_surface_img, self.npc_pos)
        self.npc_mask = pyg.mask.from_surface(self.npc_surface_img)