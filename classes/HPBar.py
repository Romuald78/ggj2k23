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

        percent = (self.player.hp / self.player.maxHP) * 170

        arcade.draw_rectangle_filled(self.sprite.center_x+10, self.sprite.center_y - 15, 150, 40,arcade.color.DARK_GRAY,tilt_angle=80)
        arcade.draw_rectangle_filled(self.sprite.center_x+10, self.sprite.center_y - 15, percent, 40,arcade.color.BLUE_GRAY,tilt_angle=80)

        self.sprite.draw()


    def update(self, deltatime):


        if(self.player.hp < 0):
            print("You Died")
            self.player.hp += 100000000
