import math
from random import randint

from classes.IDamage import IDamage
from classes.IGunner import IGunner
from classes.ProjectileManager import PLAYER_PROJ
from core.utils.utils import Gfx

class Player(IGunner,IDamage):

    def __init__(self, projectileManager,camera, initPos=(0, 0),maxHP = 10):
        self.maxHP = maxHP
        self.camera = camera
        IGunner.__init__(self,PLAYER_PROJ, projectileManager, 0.15)
        IDamage.__init__(self,maxHP,2)
        playerScale = 0.50
        params = {
            "filePath": "resources/images/player.png",
            "filterColor": (255, 255, 255, 255),
            "spriteBox":(4,1,139,163),
            "startIndex":0,
            "endIndex":3,
            "frameDuration":0.15,
            "position": initPos
        }
        self.bodyR = Gfx.create_animated(params)
        params["flipH"] = True
        self.bodyL = Gfx.create_animated(params)
        params = {
            "filePath": "resources/images/player.png",
            "filterColor": (255, 255, 255, 255),
            "spriteBox":(4,1,139,163),
            "startIndex":0,
            "endIndex":0,
            "frameDuration":0.15,
            "position": initPos
        }
        self.bodyIdleR = Gfx.create_animated(params)
        params["flipH"] = True
        self.bodyIdleL = Gfx.create_animated(params)

        params = {
            "filePath": "resources/images/gun.png",
            "spriteBox":(1,4,460,400//5),
            "startIndex":0,
            "endIndex":4,
            "frameDuration":0.15,
            "position": initPos
        }
        self.gunR = Gfx.create_animated(params)
        params["flipH"] = True
        self.gunL = Gfx.create_animated(params)

        self.bodyR.scale = playerScale
        self.bodyL.scale = playerScale
        self.bodyIdleL.scale = playerScale
        self.bodyIdleR.scale = playerScale
        self.gunR.scale = playerScale
        self.gunL.scale = playerScale

        self.hitTimer = 0

        #collisions
        self.bodyL.userData = self
        self.bodyR.userData = self
        self.gunL.userData = self
        self.gunR.userData = self
        self.bodyIdleL.userData = self
        self.bodyIdleR.userData = self

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
        self.hitTimer -= deltaTime
        if(self.hitTimer < 0):
            color = (255,255,255,255)
        else:
            value = randint(0,4) * 63
            color = (255, value, value, 255)
        self.bodyL.color = color
        self.bodyR.color = color
        self.bodyIdleL.color = color
        self.bodyIdleR.color = color
        self.gunL.color =  color
        self.gunR.color = color

        self.bodyR.update_animation(deltaTime)
        self.bodyL.update_animation(deltaTime)
        self.gunR.update_animation(deltaTime)
        self.gunL.update_animation(deltaTime)
        self.bodyIdleL.update_animation(deltaTime)
        self.bodyIdleR.update_animation(deltaTime)
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

        if not (self.center_x > -(self.camera.maxWidth-40) and self.center_x < (self.camera.maxWidth-40)) :
            #revert
            self.bodyL.center_x -= self.speed_x * self.SPEED * deltaTime

        if not (self.center_y > -(self.camera.maxHeight-60) and self.center_y < (self.camera.maxHeight-60)) :
            #revert
            self.bodyL.center_y -= self.speed_y * self.SPEED * deltaTime


        self.bodyR.center_x = self.bodyL.center_x
        self.bodyR.center_y = self.bodyL.center_y
        self.bodyIdleL.center_x = self.bodyL.center_x
        self.bodyIdleL.center_y = self.bodyL.center_y
        self.bodyIdleR.center_x = self.bodyL.center_x
        self.bodyIdleR.center_y = self.bodyL.center_y
        self.gunL.center_x = self.bodyL.center_x
        self.gunL.center_y = self.bodyL.center_y
        self.gunR.center_x = self.bodyL.center_x
        self.gunR.center_y = self.bodyL.center_y

        ang = 180 * math.atan2(-self.view_y, self.view_x) / math.pi
        self.gunL.angle = ang + 180
        self.gunR.angle = ang

        self.updateGunner(deltaTime,self.bodyL)

    def getSpeed(self):
        return (self.speed_x * self.SPEED,self.speed_y * self.SPEED)

    @property
    def center_x(self):
        return self.bodyL.center_x

    @property
    def center_y(self):
        return self.bodyL.center_y

    def getBody(self):
        return self.bodyL

    def triggerHitEffect(self):
        self.hitTimer = 0.1

    def isMoving(self):
        return self.speed_x != 0 or self.speed_y !=0 or self.moveL or self.moveR or self.moveD or self.moveU

    def draw(self):

        if(self.isMoving()):
            if self.view_x >= 0:
                self.bodyR.draw()
                self.gunR.draw()
            else:
                self.bodyL.draw()
                self.gunL.draw()
        else:
            if self.view_x >= 0:
                self.bodyIdleR.draw()
                self.gunR.draw()
            else:
                self.bodyIdleL.draw()
                self.gunL.draw()
