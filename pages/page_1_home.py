import arcade

from classes.EnemyManager import EnemyManager
from classes.Player import Player
from classes.ProjectileManager import ProjectileManager


class Page1Home():

    def __update_viewport(self):
        x0 = 1000000000
        x1 = -1000000000
        y0 = 1000000000
        y1 = -1000000000

        x0, y0, x1, y1 = self.track.getViewport()

        xm = (x0 + x1) / 2
        ym = (y0 + y1) / 2
        W = self.vp[1] - self.vp[0]
        H = self.vp[3] - self.vp[2]
        self.window.set_viewport(xm - W / 2, xm + W / 2, ym - H / 2, ym + H / 2)

    def __init__(self, w, h, window: arcade.Window):
        super().__init__()
        self.window = window
        self.vp = self.window.get_viewport()
        self.W = w
        self.H = h

    def setup(self):
        self.playerProjectileManager = ProjectileManager()
        self.enemyProjectileManager = ProjectileManager()
        self.enemyManager = EnemyManager()
        self.player = Player( self.playerProjectileManager, initPos=(500,500) )
        self.enemyManager.createEnemy((100,100))

    def update(self, deltaTime):
        self.player.update(deltaTime)
        self.playerProjectileManager.update(deltaTime)
        self.enemyProjectileManager.update(deltaTime)
        self.enemyManager.update(deltaTime)

    def draw(self):
        self.player.draw()
        self.playerProjectileManager.draw()
        self.enemyProjectileManager.draw()
        self.enemyManager.draw()

    def onKeyEvent(self, key, isPressed):
        if key == arcade.key.Q :
            self.player.moveLeft(isPressed)
        if key == arcade.key.D :
            self.player.moveRight(isPressed)
        if key == arcade.key.Z :
            self.player.moveUp(isPressed)
        if key == arcade.key.S :
            self.player.moveDown(isPressed)

    def onMouseMotionEvent(self, x, y, dx, dy):
        self.player.viewTo(x, y)

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        if axisName == "X":
            if abs(analogValue) <= 0.15:
                analogValue = 0
            self.player.speed_x = analogValue
        if axisName == "Y":
            if abs(analogValue) <= 0.15:
                analogValue = 0
            self.player.speed_y = -analogValue
        if axisName == "RX":
            self.player.view_x = analogValue
        if axisName == "RY":
            self.player.view_y = analogValue

