import pygame
import SCRIPTS.load_json as _json

class audio_mix():
    def __init__(self):
        self.json_obj = _json.CONFIG()
        self.json_obj.create_config()
    
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(f"{self.json_obj.paths["PATH-AUDIOS"]}")
        pygame.mixer.music.play()
        
    if __name__ == "__main__":
        play_music()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pygame.mixer.music.stop()
  