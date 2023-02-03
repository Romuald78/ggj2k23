from core.utils.utils import Gfx

class Player():

    def __init__(self, initPos=(0,0)):
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
        self.view_x = 0
        self.view_y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.SPEED = 750

    def update(self, deltaTime):
        self.bodyL.center_x += self.speed_x * self.SPEED * deltaTime
        self.bodyL.center_y += self.speed_y * self.SPEED * deltaTime
        self.bodyR.center_x = self.bodyL.center_x
        self.bodyR.center_y = self.bodyL.center_y
        self.gunL.center_x = self.bodyL.center_x
        self.gunL.center_y = self.bodyL.center_y
        self.gunR.center_x = self.bodyL.center_x
        self.gunR.center_y = self.bodyL.center_y


    def draw(self):
        if self.view_x >= 0:
            self.bodyR.draw()
            self.gunR.draw()
        else:
            self.bodyL.draw()
            self.gunL.draw()


