
from classes.IDamage import IDamage
from classes.IGunner import IGunner
from classes.ProjectileManager import ENEMY_PROJ


class Enemy(IDamage,IGunner):

    def __init__(self, sprite, projectileManager, hp = 20, dmg = 1):
        IDamage.__init__(self,hp, dmg)
        IGunner.__init__(self,ENEMY_PROJ, projectileManager,0.1)
        self.projectileManager = projectileManager
        self.sprite = sprite

    def update(self, deltaTime):
        self.updateGunner(deltaTime,self.sprite)

    def target(self,x,y):
        self.viewToGunner(self.sprite,x,y)


