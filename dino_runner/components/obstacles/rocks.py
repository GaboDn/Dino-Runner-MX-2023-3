import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import ROCK

class Rock(Obstacle):
    Y_POS_ROCK = 350

    def __init__(self):
        self.image = ROCK
        super().__init__(self.image)
        self.rect.y = self.Y_POS_ROCK