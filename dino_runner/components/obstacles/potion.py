import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import FAKE_POTION

class FakePotion(Obstacle):
    Y_POS_CACTUS = 350

    def __init__(self):
        self.image = FAKE_POTION
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUS