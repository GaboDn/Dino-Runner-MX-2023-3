import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS

class Cactus(Obstacle):
    Y_POS_CACTUS = 325

    def __init__(self):
        self.image = random.choice(
            [SMALL_CACTUS[0],
             SMALL_CACTUS[1],
             SMALL_CACTUS[2],
             LARGE_CACTUS[0],
             LARGE_CACTUS[1],
             LARGE_CACTUS[2]])

        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUS
