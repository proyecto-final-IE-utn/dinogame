from dino import *

class Game:
    def __init__(self, name, func):
        self.name = name
        self.start_func = func



dino = Game("dino",dino_start)
dino.start_func()
