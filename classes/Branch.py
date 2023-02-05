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
                dx = self.player.center_x - self.lastRoot.sprite.center_x
                dy = self.player.center_y - self.lastRoot.sprite.center_y
                targetAngle = math.atan2(dy,dx)*180/math.pi
                diff = (targetAngle - self.lastRoot.sprite.angle + 3600) % 360
                if diff > 180:
                    diff -= 360
                if diff < -180:
                    diff += 360
                maxTurn = 10
                if abs(diff) > maxTurn:
                    diff = min(maxTurn, max(-maxTurn, diff))
                targetAngle = self.lastRoot.sprite.angle + diff
                if random.random() <= 0.05 and self.nbRoots >= 5:
                    self.enemyMgr.createEnemy( self.lastRoot.getNextPosition(targetAngle) )
                    self.duplicated = True
                else:
                    if self.nbRoots <= 3:
                        targetAngle = self.lastRoot.sprite.angle + random.randint(-45,45)
                    newRoot = self.lastRoot.addNextRoot(targetAngle)
                    self.lastRoot = newRoot
                    self.branchMgr.addRoot(newRoot)
                    self.nbRoots += 1
            else:
                self.lastRoot.update(deltaTime)
        else:
            self.firstRoot.destroy()
            self.firstRoot.update(deltaTime)