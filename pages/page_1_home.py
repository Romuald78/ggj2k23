import random

import arcade

from classes.Branch import Branch
from classes.BranchManager import BranchManager
from classes.BackGround import Background
from classes.Camera import Camera
from classes.Collisions import CollisionMgr
from classes.Countdown import Countdown
from classes.EnemyManager import EnemyManager
from classes.HPBar import HPBar
from classes.Player import Player
from classes.ProjectileManager import ProjectileManager

DEBUG_REMOVE_ENEMY_PROJECTILES = False


class Page1Home():

    def __init__(self, w, h, window: arcade.Window, process=None):
        super().__init__()
        self.window = window
        self.W = w
        self.H = h
        self.process = process

    def setup(self, config=None):
        self.camera = Camera(self.window, 0, 0, self.W, self.H)
        self.countdown = Countdown(self.camera,self.process,60)
        self.playerProjectileManager = ProjectileManager((2000,2000))
        self.enemyProjectileManager = ProjectileManager((1000,1000))
        self.player = Player(self.playerProjectileManager, initPos=(500, 500))
        self.HPBar = HPBar(self.camera,self.player,self.process)
        self.branchMgr = BranchManager()
        self.enemyManager = EnemyManager(self.camera,
                                         self.enemyProjectileManager,
                                         self.branchMgr,
                                         self.player)

        self.collMgr = CollisionMgr(self.playerProjectileManager.projs,
                                    self.enemyManager.enemies)

        self.collMgrEnemy = CollisionMgr([self.player.getBody()], self.enemyProjectileManager.projs)
        self.background = Background(self.camera)

        self.music = arcade.load_sound("resources/sound/VampireSurvivorGGJ-V2.mp3")
        self.started = False

    def update(self, deltaTime):
        if not self.started:
            self.started = True
            arcade.play_sound(self.music, 1.0, 0.0, True)

        self.background.update(deltaTime)
        self.player.update(deltaTime)
        self.playerProjectileManager.update(deltaTime)
        if not DEBUG_REMOVE_ENEMY_PROJECTILES:
            self.enemyProjectileManager.update(deltaTime)
        self.enemyManager.update(deltaTime)
        self.collMgr.update()
        self.branchMgr.update(deltaTime)
        self.collMgrEnemy.update()
        self.camera.update( self.player.bodyL.center_x,
                            self.player.bodyL.center_y )
        self.countdown.update(deltaTime)

        self.HPBar.update(deltaTime)

    def draw(self):
        self.background.draw()
        self.branchMgr.draw()
        self.enemyManager.draw()
        self.enemyProjectileManager.draw()
        self.playerProjectileManager.draw()
        self.player.draw()
        self.countdown.draw()
        self.HPBar.draw()

    def onKeyEvent(self, key, isPressed):
        if key == arcade.key.Q:
            self.player.moveLeft(isPressed)
        if key == arcade.key.D:
            self.player.moveRight(isPressed)
        if key == arcade.key.Z:
            self.player.moveUp(isPressed)
        if key == arcade.key.S:
            self.player.moveDown(isPressed)

    def onMouseMotionEvent(self, x, y, dx, dy):
        self.player.viewTo(x, y)

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        if not hasattr(self,"player") :
            return

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

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        pass