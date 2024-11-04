#imports external
import pygame as pyg
#imports external
import SCRIPTS.utilities as _util
class PLAYER():
    def __init__(self, display: pyg.display, text_obj: _util.text_fonts):
        self.display = display
        self.util_obj = _util.utility(self.display)
        self.text_obj = text_obj
        self.player_info ={
            "day": 1,
            "casos_won": 0,
            "casos_lost": 0,
            "money": 100,
            "tutorial_done": False,
            "number_of_interrogations": 15
        }
        self.dialog_already_seen = [
            {
                "ID": int,
                "NAME": str,
                "DIALOG": str
            }
        ]
        ...