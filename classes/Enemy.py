import math

from classes.ProjectileManager import PLAYER_PROJ
from core.utils.utils import Gfx

class Enemy():

    def __init__(self, sprite, hp = 20):
        self.hp = hp
        pass

    def update(self, deltaTime):
        pass

    def reduceHP(self,dmg=1):
        pass

    def getDMG(self):
        return 1

