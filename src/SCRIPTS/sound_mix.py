#imports external
import pygame as _pyg, time, os
#imports internal
import load_json as _json
class sounds_mix():
    def __init__(self):
        self.json_data = _json.CONFIG()
        self.json_data.create_config()
        self.paths = self.json_data.paths
        self.sounds = {
            ...
        }