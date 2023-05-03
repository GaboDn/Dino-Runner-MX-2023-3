import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class Cactus(Obstacle):
    Y_POS_CACTUS_SMALL= 325
    Y_POS_CACTUS_LARGE = 300
    COMBINATED_CACTUS = []

    def __init__(self):
        self.COMBINATED_CACTUS = SMALL_CACTUS + LARGE_CACTUS
        self.image = random.choice(self.COMBINATED_CACTUS)
        super().__init__(self.image)
        if self.image in SMALL_CACTUS:
            self.rect.y = self.Y_POS_CACTUS_SMALL
        else:
            self.rect.y = self.Y_POS_CACTUS_LARGE

