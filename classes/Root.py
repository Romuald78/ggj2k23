import math
import random

from core.utils.utils import Gfx


class Root():

    def __init__(self, initPos, angle):
        idx = random.randint(0,2)
        self.sprite = Gfx.create_animated({
            "filePath": "resources/images/root.png",
             #"size": (250, 250),
            "filterColor": (255, 255, 255, 255),
            "spriteBox":(1,3,890,640//3),
            "startIndex":idx,
            "endIndex":idx,
            "frameDuration":1,
            "position": initPos
        })
        self.sprite.scale = 0.20
        self.sprite.update_animation(0)
        self.sprite.angle = angle
        self.maxScale = self.sprite.scale
        self.sprite.scale = 0
        self.scaleStep = 5
        self.growing   = True
        self.nextRoot  = None
        self.mustBeDestroyed = False

    def hasGrown(self):
        return self.growing == False

    def canReap(self):
        return self.sprite.scale <= 0 and self.mustBeDestroyed
        # TODO : use scale 0 instead

    def update(self, deltaTime):
        self.sprite.update_animation()
        if not self.mustBeDestroyed:
            if self.sprite.scale < self.maxScale:
                self.sprite.scale += self.scaleStep*self.maxScale*deltaTime
                self.sprite.scale = min(self.sprite.scale, self.maxScale)
            else:
                self.growing = False
        else:
            reduce = False
            if self.nextRoot is not None:
                self.nextRoot.destroy()
                self.nextRoot.update(deltaTime)
                if self.nextRoot.canReap() :
                    reduce = True
            else:
                reduce = True
            if reduce:
                self.sprite.scale -= self.scaleStep * self.maxScale * deltaTime
                if self.sprite.scale <= 0:
                    self.sprite.scale = 0

    def addNextRoot(self, targetAngle):
        ang = self.sprite.angle
        x = self.sprite.center_x + 0.5 * self.sprite.width * math.cos(ang*math.pi/180)
        y = self.sprite.center_y + 0.5 * self.sprite.width * math.sin(ang * math.pi / 180)
        newRoot = Root( (x,y), targetAngle) # TODO limit target angle
        self.nextRoot = newRoot
        return newRoot

    def destroy(self):
        self.mustBeDestroyed = True
        self.sprite.color = (128,64,64)
