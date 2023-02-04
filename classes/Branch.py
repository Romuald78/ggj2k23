import math

from classes.Root import Root


class Branch():

    def __init__(self, initPos, angle, branchMgr, player):

        self.firstRoot = Root(initPos, angle)
        self.lastRoot  = self.firstRoot
        self.nextEnemy = None
        self.growing   = True
        self.branchMgr = branchMgr
        self.branchMgr.addRoot(self.firstRoot)
        self.player    = player

    def update(self, deltaTime):
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
