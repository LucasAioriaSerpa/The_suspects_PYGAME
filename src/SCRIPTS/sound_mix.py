#imports external
import pygame as _pyg, time, os
#imports internal
import SCRIPTS.load_json as _json
class sound_mix:
    def __init__(self):
        self.json_data = _json.CONFIG()
        self.json_data.create_config()
        self.paths = self.json_data.paths
        self.sounds = ...
    def tocar_som_em_loop(self, arquivo_som, duracao):
        """
        Toca o som em loop por uma duração específica.

        Parâmetros:
        - arquivo_som (str): Caminho para o arquivo de som.
        - duracao (float): Tempo em segundos para manter o som em loop.
        """
        som = _pyg.mixer.Sound(arquivo_som)
        som.play(loops=-1)
        time.sleep(duracao)
        som.stop()
    def carregar_sons(self, pasta):
        for arquivo in os.listdir(f"{self.paths["PATH-AUDIOS"]}/{pasta}"):
            if arquivo.endswith(".wav"):
                nome = arquivo.split(".")[0]
                caminho = os.path.join(pasta, arquivo)
                self.sounds[nome] = _pyg.mixer.Sound(caminho)
    def tocar_som(self, nome_do_som, sons):
        som = sons.get(nome_do_som)
        if som:
            som.play()