
from classes.IDamage import IDamage

class Enemy(IDamage):

    def __init__(self, sprite, projectileManager, hp = 20, dmg = 1):
        super().__init__(hp, dmg)
        self.projectileManager = projectileManager

    def update(self, deltaTime):
        pass


