import random
from random import randint

from classes.Branch import Branch
from classes.IDamage import IDamage
from classes.IGunner import IGunner
from classes.ProjectileManager import ENEMY_PROJ
from classes.Root import Filter

NEW_BRANCH_TIMER = 5
MAX_ELITE = 5

class Enemy(IDamage,IGunner):

    def getElitness(self):
        i = random.randint(0, 100)
        if i<50:
            return 0
        if i<70:
            return 1
        if i<80:
            return 2
        if i<90:
            return 3
        if i<95:
            return 4
        return 5

    def __init__(self, sprite, projectileManager, hp = 1, dmg = 1):
        self.elitness = self.getElitness()
        self.initialColor = (255, 255, int((1-(self.elitness/MAX_ELITE))*255), 255)
        IDamage.__init__(self,hp*self.elitness*3, dmg*self.elitness)
        IGunner.__init__(self,ENEMY_PROJ, projectileManager,1.25)
        self.projectileManager = projectileManager
        self.sprite = sprite
        self.sprite.scale = self.sprite.scale * (1+(self.elitness/MAX_ELITE))
        self.branches = []
        self.mustBeDestroyed = False
        self.initAng = 0
        self.hitTimer = 0

    def addBranch(self, brnch):
        self.branches.append(brnch)

    def destroy(self):
        self.mustBeDestroyed = True
        self.sprite.color = Filter
        for b in self.branches:
            b.destroy()

    def getSpeed(self):
        return (0,0)

    def triggerHitEffect(self):
        self.sprite.color = (255, 0, 0, 255)
        self.hitTimer = 0.1

    def update(self, deltaTime):
        self.hitTimer -= deltaTime
        if(self.hitTimer < 0):
            self.sprite.color = self.initialColor
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
        if len(self.branches)==0:
            self.sprite.scale -= 1 * deltaTime

    def canReap(self):
        return self.mustBeDestroyed and len(self.branches)==0 and self.sprite.scale <= 0

    def target(self, x, y):
        self.viewToGunner(self.sprite,x,y)


