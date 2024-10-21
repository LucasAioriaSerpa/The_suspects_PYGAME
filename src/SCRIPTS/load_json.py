#imports external
import json
#imports internal
...
class CONFIG():
    def __init__(self):
        self.json_config = dict
        self.game_config = {
            "CAPTION": ...,
            "RESOLUTION": ...,
            "BACKGROUND": ...,
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
        '''reads and loads DATA from json to the dictionary'''
        #? loads game_config.json to json_config dict
        with open('src/JSON/game_config.json', 'r') as file:
            self.json_config = json.load(file)
        print(f"\nJSON DATA: {self.json_config}\n")
        #? loads game_config dict with json_config
        for key in self.game_config.keys():
            self.game_config[key] = self.json_config["configs"][key]
        print(f"game_config DATA: {self.game_config}\n")
        #? loads paths dict with json_config
        for key in self.paths.keys():
            self.paths[key] = self.json_config["paths"][key]
        print(f"paths DATA: {self.paths}")