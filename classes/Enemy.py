import math

from classes.IDamage import IDamage
from classes.ProjectileManager import PLAYER_PROJ
from core.utils.utils import Gfx

class Enemy(IDamage):

    def __init__(self, sprite, hp = 20, dmg=1):
        super().__init__(hp, dmg)

    def update(self, deltaTime):
        pass


