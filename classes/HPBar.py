import arcade

from classes.Camera import Camera
from classes.Player import Player


class HPBar:

    def __init__(self, camera: Camera, player: Player):
        self.camera = camera
        self.player = player

    def draw(self):
        percent = (self.player.hp / self.player.maxHP) * 100
        refx = self.camera.x - 50
        x = refx + percent/2

        arcade.draw_rectangle_filled(x, self.camera.y - (self.camera.H//2) + 30, percent, 30,
                                     arcade.color.BLUE)
        pass

    def update(self, deltatime):
        if(self.player.hp < 0):
            print("You Died")
            self.player.hp += 100000000
