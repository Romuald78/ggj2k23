import arcade

from classes.Camera import Camera
from classes.Player import Player
from core.utils.utils import Gfx


class HPBar:

    def __init__(self, camera: Camera, player: Player):
        self.camera = camera
        self.player = player
        self.sprite = Gfx.create_fixed({
            "filePath": "resources/images/ui_life_o2.png",
            "filterColor": (255, 255, 255, 255),
        })
        self.sprite.angle = 0
        self.sprite.scale = 0.6

    def draw(self):

        self.sprite.center_x = self.camera.x - (self.camera.W // 2) + (self.sprite.width // 2)
        self.sprite.center_y = self.camera.y - (self.camera.H // 2) + (self.sprite.height // 2)

        percent = (self.player.hp / self.player.maxHP)

        arcade.draw_rectangle_filled(self.sprite.center_x+10, self.sprite.center_y - 15, 150, 40,(96,96,96,256),tilt_angle=80)

        ymid = self.sprite.center_y - (1-percent) * 142 / 2
        arcade.draw_rectangle_filled(self.sprite.center_x+12, ymid-13, 40, 142*percent,arcade.color.BLUE_GRAY,tilt_angle=-10)

        self.sprite.draw()

    def update(self, deltatime):

        if(self.player.hp < 0):
            print("You Died")
            self.player.hp = 10000000