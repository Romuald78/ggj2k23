from core.utils.utils import Gfx

class Player():

    def __init__(self, initPos=(0,0)):
        params = {
            "filePath" : "resources/images/player.png",
            "size" : (100,100),
            "filterColor" : (255, 0, 0, 255),
            "position" : initPos
        }
        self.sprite = Gfx.create_fixed(params)

    def move(self, dx, dy):
        self.sprite.center_x += dx
        self.sprite.center_y += dy

    def draw(self):
        self.sprite.draw()

