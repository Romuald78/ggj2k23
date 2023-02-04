from random import randint

from classes.Branch import Branch
from classes.IDamage import IDamage
from classes.IGunner import IGunner
from classes.ProjectileManager import ENEMY_PROJ

NEW_BRANCH_TIMER = 5

class Enemy(IDamage,IGunner):

    def __init__(self, sprite, projectileManager, hp = 1, dmg = 1):
        IDamage.__init__(self,hp, dmg)
        IGunner.__init__(self,ENEMY_PROJ, projectileManager,1.25)
        self.projectileManager = projectileManager
        self.sprite = sprite
        self.branches = []

    def addBranch(self, brnch):
        self.branches.append(brnch)

    def update(self, deltaTime):
        self.updateGunner(deltaTime,self.sprite)
        # update branches
        for b in self.branches:
            b.update(deltaTime)

    def target(self,x,y):
        self.viewToGunner(self.sprite,x,y)


