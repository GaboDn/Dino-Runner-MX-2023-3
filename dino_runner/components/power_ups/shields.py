from dino_runner.components.power_ups.power_up import PoweUp
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

class Shield(PoweUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE


        super().__init__(SHIELD, SHIELD_TYPE)