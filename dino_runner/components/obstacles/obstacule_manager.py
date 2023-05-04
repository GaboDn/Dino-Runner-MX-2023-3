import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self,game_speed,player):
        if len(self.obstacles) == 0:
            choice = random.choice([0,1])
            if choice == 0:
                self.obstacles.append(Cactus())
            else:
                self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed,player)

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)