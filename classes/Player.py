import math

from classes.ProjectileManager import PLAYER_PROJ
from core.utils.utils import Gfx

class Player():

    def __init__(self,projectileManager, initPos=(0,0)):
        params = {
            "filePath" : "resources/images/player.png",
            "size" : (200,200),
            "filterColor" : (255, 255, 255, 255),
            "position" : initPos
        }
        self.bodyR = Gfx.create_fixed(params)
        params["flipH"] = True
        self.bodyL = Gfx.create_fixed(params)
        params = {
            "filePath" : "resources/images/gun.png",
            "size" : (100,100),
            "filterColor" : (255, 255, 255, 255),
            "position" : initPos
        }
        self.gunR = Gfx.create_fixed(params)
        params["flipH"] = True
        self.gunL = Gfx.create_fixed(params)

        # move and view
        self.view_x = 1
        self.view_y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.SPEED = 750
        self.projectileManager = projectileManager
        self.FIRE_RATE = 0.1 #s between proj
        self.shootTimer = 0

        # life point
        self.life = 100

        # shooting
        self.isShooting = False

    def isAlive(self):
        return self.life > 0

    def isDead(self):
        return not self.isAlive()

    def update(self, deltaTime):
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
        self.gunL.angle = ang+180
        self.gunR.angle = ang

        if self.shootTimer > self.FIRE_RATE:
            norm = math.sqrt(self.view_x*self.view_x + self.view_y*self.view_y)
            self.shootTimer -= self.FIRE_RATE
            self.projectileManager.createProjectile(
                (self.bodyR.center_x,self.bodyR.center_y),
                (self.view_x/norm, -self.view_y/norm),
                PLAYER_PROJ)

    def draw(self):
        if self.view_x >= 0:
            self.bodyR.draw()
            self.gunR.draw()
        else:
            self.bodyL.draw()
            self.gunL.draw()


