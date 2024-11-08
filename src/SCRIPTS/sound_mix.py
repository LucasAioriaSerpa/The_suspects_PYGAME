#imports external
import pygame as pyg
#imports internal
import SCRIPTS.load_json as _json
class sounds_mix():
    def __init__(self):
        self.json_data = _json.CONFIG()
        self.json_data.create_config()
        self.paths_audio = self.json_data.paths["PATH-AUDIOS"]
        self.sounds = {
            "menuMusic.wav": ...,
            "menuBeep.wav":...
        }
        self.flag_playing = False
        pyg.mixer.init()
    def load_audios(self):
        for file in self.sounds.keys(): self.sounds[file] = pyg.mixer.Sound(f"{self.paths_audio}/{file}")
    def play_sound(self, file: str):
        self.sounds[file].play()
    def play_background_sound(self, file: str):
        if not self.flag_playing:
            self.sounds[file].play(-1)
            self.sounds[file].set_volume(0.2)
            self.flag_playing = True
    def stop_sounds(self):
        self.flag_playing = False
        pyg.mixer.fadeout(1)
    def stop_sound(self, file: str):
        self.sounds[file].fadeout(1)