#imports external
import json
#imports internal
...
class CONFIG():
    """
    ...
    Attributes
    ----------------------------------------------------------------
        @json_config : is a dictionary with the complete json DATA
        @game_config : is a dictionary with values for the game
            "CAPTION": "NAME OF THE GAME",
            "RESOLUTION": [WIDTH, HEIGHT],
            "BACKGROUND": "BACKGROUND COLOR HEX",
            "FPS": INTEGER FRAMES PER SECOND,
        @paths : is a dictionary with paths of the files
            "PATH-DEFAULT": "src",
            "PATH-IMAGES": "src/IMAGES/",
            "PATH-IMAGES-mouse": "src/IMAGES/mouse/",
            "PATH-IMAGES-menu": "src/IMAGES/menu/",
            "PATH-IMAGES-characteres": "src/IMAGES/characteres/",
            "PATH-IMAGES-player": "src/IMAGES/player/",
            "PATH-FONTS": "src/FONTS/",
            "PATH-AUDIOS": "src/AUDIOS/",
            "PATH-JSON": "src/JSON/"
    ----------------------------------------------------------------
    """
    def __init__(self):
        self.json_config = dict
        self.game_config = {
            "CAPTION": ...,
            "RESOLUTION": ...,
            "BACKGROUND": ...,
            "GAME_STATE": ...,
            "FPS": ...,
        }
        self.paths = {
            "PATH-DEFAULT": ...,
            "PATH-IMAGES": ...,
            "PATH-IMAGES-mouse": ...,
            "PATH-IMAGES-menu": ...,
            "PATH-IMAGES-characteres": ...,
            "PATH-IMAGES-player": ...,
            "PATH-FONTS": ...,
            "PATH-AUDIOS": ...,
            "PATH-JSON": ...
        }
    def create_config(self):
        #? loads game_config.json to json_config dict
        with open('src/JSON/game_config.json', 'r') as file: self.json_config = json.load(file)
        #print(f"\nJSON DATA: {self.json_config}\n")
        #? loads game_config dict with json_config
        for key in self.game_config.keys(): self.game_config[key] = self.json_config["configs"][key]
        #print(f"game_config DATA: {self.game_config}\n")
        #? loads paths dict with json_config
        for key in self.paths.keys(): self.paths[key] = self.json_config["paths"][key]
        #print(f"paths DATA: {self.paths}")
    def load_json(self, file_str:str) -> dict[str]:
        path_json = f"{self.paths["PATH-JSON"]}{file_str}"
        with open(path_json, "r") as file: return json.load(file)