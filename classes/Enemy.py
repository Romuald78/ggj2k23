from random import randint

from classes.Branch import Branch
from classes.IDamage import IDamage
from classes.IGunner import IGunner
from classes.ProjectileManager import ENEMY_PROJ

NEW_BRANCH_TIMER = 5

class Enemy(IDamage,IGunner):

    def __init__(self, sprite, projectileManager, hp = 1, dmg = 1):
        IDamage.__init__(self,hp, dmg)
        IGunner.__init__(self,ENEMY_PROJ, projectileManager,0.75)
        self.projectileManager = projectileManager
        self.sprite = sprite
        self.branches = []
        self.mustBeDestroyed = False

    def addBranch(self, brnch):
        self.branches.append(brnch)

    def destroy(self):
        self.mustBeDestroyed = True
        for b in self.branches:
            b.destroy()

    def update(self, deltaTime):
        if self.hp <= 0:
            self.destroy()
        # update branches if needed
        for b in self.branches:
            # growing the branch
            b.update(deltaTime)
            if not self.mustBeDestroyed:
                # launch projectile
                self.updateGunner(deltaTime, self.sprite)
            elif b.canReap():
                self.branches.remove(b)
            else:
                # enemy is dead but we have to keep it in memory for a while
                # just for display
                pass

    def canReap(self):
        return self.mustBeDestroyed and len(self.branches)==0

    def target(self,x,y):
        self.viewToGunner(self.sprite,x,y)


