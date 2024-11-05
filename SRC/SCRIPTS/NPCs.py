#imports external
import pygame as pyg, random
#imports internal
import SCRIPTS.utilities as _util
import SCRIPTS.mouse as _mous
class COP_NPC():
    def __init__(self, display: pyg.display, pos: tuple, name: str, text_obj: _util.text_fonts):
        self.display = display
        self.npc_pos = pos
        self.npc_name = name
        self.text_obj = text_obj
        self.util_obj = _util.utility(display)
        self.npc_dialog = {
            "part": 0
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
        if continue_dialog and self.npc_dialog["part"] != len(list_dialog):
            self.npc_dialog["part"] += 1
            self.text_obj.f_animation["frame"] = 0
            return
        self.npc_dialog["flag"] = self.text_obj.long_text_dialog(10)
        self.text_obj.update()
    def render(self):
        self.display.blit(self.npc_surface_img, self.npc_rect)
    def update(self):
        self.npc_surface_img = self.util_obj.image_load("PATH-IMAGES-characteres","NPCs/cop.png")
        self.npc_rect = self.util_obj.get_rect(self.npc_surface_img, self.npc_pos)
        self.npc_mask = pyg.mask.from_surface(self.npc_surface_img)
class SUS_NPC():
    def __init__(self, display: pyg.display, pos: tuple, npc_info: list[dict], text_obj: _util.text_fonts):
        self.display = display
        self.npc_pos = pos
        self.npc_info = npc_info
        self.text_obj = text_obj
        self.util_obj = _util.utility(display)
        self.npc_dialog = {
            "part": 0
        }
        self.npc_surfaces_imgs = [
            self.util_obj.image_load("PATH-IMAGES-characteres","NPCs/suspect_shadow.png"),
            self.util_obj.image_load("PATH-IMAGES-characteres","NPCs/suspect_M.png"),
            self.util_obj.image_load("PATH-IMAGES-characteres","NPCs/suspect_F.png")
        ]
        self.dialog_cache = []
        self.type_int = 0
        self.selected = False
        self.npc_rect = self.util_obj.get_rect(self.npc_surfaces_imgs[self.type_int], self.npc_pos)
        self.npc_mask = pyg.mask.from_surface(self.npc_surfaces_imgs[self.type_int])
    def generate_dialog(self, op_ss: list[str], npc_index: int):
        type_dialog_rand = random.choice(op_ss)
        evidence_rand = random.choice(type_dialog_rand)
        dialog_rand = evidence_rand["DIALOG"]
        int_dialog = (int(dialog_rand[0]))
        timer = 0
        while npc_index+1 != int_dialog:
            timer += 1
            if timer >= 10000: break
            evidence_rand = random.choice(type_dialog_rand)
            dialog_rand = evidence_rand["DIALOG"]
            int_dialog = (int(dialog_rand[0]))
            #print(npc_index+1, (int(dialog_rand[0])))
        npc_dialog = dialog_rand[1]
        return [npc_dialog, evidence_rand]
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
        if continue_dialog and self.npc_dialog["part"] != len(list_dialog):
            self.npc_dialog["part"] += 1
            self.text_obj.f_animation["frame"] = 0
            return
        self.text_obj.long_text_dialog(10)
        self.text_obj.update()
    def check_collision(self, m_obj: _mous.MOUSE) -> bool:
        if self.npc_mask.overlap(m_obj.mask, (m_obj.pos[0]-self.npc_rect.x, m_obj.pos[1]-self.npc_rect.y)):
            return True
        return False
    def render(self):
        self.display.blit(self.npc_surfaces_imgs[self.type_int], self.npc_rect)
    def update(self):
        self.npc_rect = self.util_obj.get_rect(self.npc_surfaces_imgs[self.type_int], self.npc_pos)
        self.npc_mask = pyg.mask.from_surface(self.npc_surfaces_imgs[self.type_int])