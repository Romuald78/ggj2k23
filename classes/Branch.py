import math
import random

from classes.Root import Root


class Branch():

    def __init__(self, initPos, angle, branchMgr, enemyMgr, player):

        self.firstRoot = Root(initPos, angle)
        self.lastRoot  = self.firstRoot
        self.duplicated = False
        self.branchMgr = branchMgr
        self.branchMgr.addRoot(self.firstRoot)
        self.player    = player
        self.mustBeDestroyed = False
        self.enemyMgr = enemyMgr
        self.nbRoots = 1

    def destroy(self):
        self.mustBeDestroyed = True

    def canReap(self):
        if not self.mustBeDestroyed:
            return False
        return self.firstRoot.canReap() and self.lastRoot.canReap()


    def update(self, deltaTime):
        if not self.mustBeDestroyed:
            if self.lastRoot.hasGrown() and not self.duplicated:
                # get relative angle to player
                # TODO
                dx = self.player.center_x - self.lastRoot.sprite.center_x
                dy = self.player.center_y - self.lastRoot.sprite.center_y
                targetAngle = math.atan2(dy,dx)*180/math.pi
                if random.random() <= 0.05 and self.nbRoots >= 4:
                    self.enemyMgr.createEnemy( self.lastRoot.getNextPosition(targetAngle) )
                    self.duplicated = True
                else:
                    newRoot = self.lastRoot.addNextRoot(targetAngle)
                    self.lastRoot = newRoot
                    self.branchMgr.addRoot(newRoot)
                    self.nbRoots += 1
            else:
                self.lastRoot.update(deltaTime)
        else:
            self.firstRoot.destroy()
            self.firstRoot.update(deltaTime)