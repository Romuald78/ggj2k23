import math

from classes.Root import Root


class Branch():

    def __init__(self, initPos, angle, branchMgr, player):

        self.firstRoot = Root(initPos, angle)
        self.lastRoot  = self.firstRoot
        self.nextEnemy = None
        self.branchMgr = branchMgr
        self.branchMgr.addRoot(self.firstRoot)
        self.player    = player
        self.mustBeDestroyed = False

    def destroy(self):
        self.mustBeDestroyed = True

    def canReap(self):
        if not self.mustBeDestroyed:
            return False
        return self.firstRoot.canReap() and self.lastRoot.canReap()


    def update(self, deltaTime):
        if not self.mustBeDestroyed:
            self.lastRoot.update(deltaTime)
            if self.lastRoot.hasGrown():
                # get relative angle to player
                # TODO
                dx = self.player.center_x - self.lastRoot.sprite.center_x
                dy = self.player.center_y - self.lastRoot.sprite.center_y
                targetAngle = math.atan2(dy,dx)*180/math.pi
                newRoot = self.lastRoot.addNextRoot(targetAngle)
                self.lastRoot = newRoot
                self.branchMgr.addRoot(newRoot)
        else:
            self.firstRoot.destroy()
            self.firstRoot.update(deltaTime)