
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import HEART_FALSE

class HeartFalse(Obstacle):
    Y_POS_HEART = 125
    X_POS_HEART = 2000

    def __init__(self):
        self.image = HEART_FALSE
        super().__init__(self.image)
        self.rect.y = self.Y_POS_HEART
        self.rect.x = self.X_POS_HEART