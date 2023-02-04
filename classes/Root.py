import math

from core.utils.utils import Gfx


class Root():

    def __init__(self, initPos, angle):
        params = {
            "filePath": "resources/images/root.png",
            "size": (200, 200),
            "filterColor": (255, 255, 255, 255),
            "position": initPos
        }
        self.sprite = Gfx.create_fixed(params)
        self.sprite.angle = angle
        self.maxScale = self.sprite.scale
        self.sprite.scale = 0
        self.scaleStep = 5
        self.growing   = True
        self.nextRoot  = None

    def hasGrown(self):
        return self.growing == False

    def update(self, deltaTime):
        if self.sprite.scale < self.maxScale:
            self.sprite.scale += self.scaleStep*self.maxScale*deltaTime
            self.sprite.scale = min(self.sprite.scale, self.maxScale)
        else:
            self.growing = False

    def addNextRoot(self, targetAngle):
        ang = self.sprite.angle
        x = self.sprite.center_x + 0.5 * self.sprite.width * math.cos(ang*math.pi/180)
        y = self.sprite.center_y + 0.5 * self.sprite.height * math.sin(ang * math.pi / 180)
        newRoot = Root( (x,y), targetAngle) # TODO use targetAngle instead of relative angle
        self.nextRoot = newRoot
        return newRoot