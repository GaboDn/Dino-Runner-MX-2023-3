import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle): 

    def __init__(self):
        self.image = BIRD[0]
        self.step_index = 0
        super().__init__(self.image)
        self.rect.y = random.choice([100,240,260,320])
    
    def update(self,game_speed,player):
        super().update(game_speed,player)
        self.fly()

        if self.step_index >= 10:
            self.step_index = 0

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.dino_rect = self.image.get_rect()
        self.step_index += 1