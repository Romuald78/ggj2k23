import math

from classes.IGunner import IGunner
from classes.ProjectileManager import PLAYER_PROJ
from core.utils.utils import Gfx

class Player(IGunner):

    def __init__(self, projectileManager, initPos=(0, 0)):
        super().__init__(PLAYER_PROJ, projectileManager, 0.1)
        params = {
            "filePath": "resources/images/player.png",
            "size": (200, 200),
            "filterColor": (255, 255, 255, 255),
            "position": initPos
        }
        self.bodyR = Gfx.create_fixed(params)
        params["flipH"] = True
        self.bodyL = Gfx.create_fixed(params)
        params = {
            "filePath": "resources/images/gun.png",
            "size": (100, 100),
            "filterColor": (255, 255, 255, 255),
            "position": initPos
        }
        self.gunR = Gfx.create_fixed(params)
        params["flipH"] = True
        self.gunL = Gfx.create_fixed(params)

        # Keyboard
        self.useKey = False
        self.moveL = False
        self.moveR = False
        self.moveU = False
        self.moveD = False
        # move and view
        self.speed_x = 0
        self.speed_y = 0
        self.SPEED = 750
        self.projectileManager = projectileManager
        self.FIRE_RATE = 0.1  # s between proj
        self.shootTimer = 0

        # life point
        self.life = 100

        # shooting
        self.isShooting = False

    def moveLeft(self, isEnabled):
        self.useKey = True
        self.moveL = isEnabled

    def moveRight(self, isEnabled):
        self.useKey = True
        self.moveR = isEnabled

    def moveUp(self, isEnabled):
        self.useKey = True
        self.moveU = isEnabled

    def moveDown(self, isEnabled):
        self.useKey = True
        self.moveD = isEnabled

    def viewTo(self, x, y):
        self.viewToGunner(self.bodyL, x, y)

    def isAlive(self):
        return self.life > 0

    def isDead(self):
        return not self.isAlive()

    def update(self, deltaTime):
        if self.useKey:
            # keyboard
            if self.moveL == self.moveR:
                self.speed_x = 0
            elif self.moveL:
                self.speed_x = -1
            elif self.moveR:
                self.speed_x = 1
            if self.moveU == self.moveD:
                self.speed_y = 0
            elif self.moveU:
                self.speed_y = 1
            elif self.moveD:
                self.speed_y = -1

        self.shootTimer += deltaTime
        self.bodyL.center_x += self.speed_x * self.SPEED * deltaTime
        self.bodyL.center_y += self.speed_y * self.SPEED * deltaTime
        self.bodyR.center_x = self.bodyL.center_x
        self.bodyR.center_y = self.bodyL.center_y
        self.gunL.center_x = self.bodyL.center_x
        self.gunL.center_y = self.bodyL.center_y
        self.gunR.center_x = self.bodyL.center_x
        self.gunR.center_y = self.bodyL.center_y

        ang = 180 * math.atan2(-self.view_y, self.view_x) / math.pi
        self.gunL.angle = ang + 180
        self.gunR.angle = ang

        self.updateGunner(deltaTime,self.bodyL)

    def draw(self):
        if self.view_x >= 0:
            self.bodyR.draw()
            self.gunR.draw()
        else:
            self.bodyL.draw()
            self.gunL.draw()
