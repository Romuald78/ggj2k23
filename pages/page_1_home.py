import random

import arcade

from classes.Camera import Camera
from classes.Collisions import CollisionMgr
from classes.EnemyManager import EnemyManager
from classes.Player import Player
from classes.ProjectileManager import ProjectileManager
from core.utils import utils
from core.utils.utils import Gfx


class Page1Home():


    def __init__(self, w, h, window: arcade.Window):
        super().__init__()
        self.window = window
        self.W = w
        self.H = h

    def setup(self):
        self.camera = Camera(self.window, 0, 0, self.W, self.H)
        self.playerProjectileManager = ProjectileManager()
        self.enemyProjectileManager = ProjectileManager()
        self.enemyManager = EnemyManager(self.camera)
        self.player = Player( self.playerProjectileManager, initPos=(500,500) )

        # TODO test collisions
        self.collMgr = CollisionMgr(self.playerProjectileManager.projs,
                                    self.enemyManager.enemies)


    def update(self, deltaTime):
        self.player.update(deltaTime)
        self.playerProjectileManager.update(deltaTime)
        self.enemyProjectileManager.update(deltaTime)
        self.enemyManager.update(deltaTime)
        self.collMgr.update()
        self.camera.update( self.player.bodyL.center_x,
                            self.player.bodyL.center_y )

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

