import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.heart_false import HeartFalse
from dino_runner.components.obstacles.potion import FakePotion
from dino_runner.components.obstacles.rocks import Rock

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self,game_speed,player):
        if len(self.obstacles) == 0:
            choice = random.choice([0,1,2,3,4])
            if choice == 0:
                self.obstacles.append(Cactus())
            elif choice == 1:
                self.obstacles.append(HeartFalse())
            elif choice == 2:
                self.obstacles.append(FakePotion())
            elif choice == 3:
                self.obstacles.append(Rock())
            else:
                self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width or obstacle.hammered:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed,player)

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []