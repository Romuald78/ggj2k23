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
from core.utils.utils import Gfx

DEBUG_REMOVE_ENEMY_PROJECTILES = False


class Page1Home():

    def __init__(self, w, h, window: arcade.Window, process=None):
        super().__init__()
        self.window = window
        self.W = w
        self.H = h
        self.process = process

    def refresh(self):
        self.setup()

    def setup(self, config=None):
        self.camera = Camera(self.window, 0, 0, self.W, self.H)
        params = {
                "filePath": "resources/images/win.png",
                "position" : (self.camera.x,self.camera.y + 2*self.H)
            }
        self.win = Gfx.create_fixed(params)
        params = {
            "filePath": "resources/images/win.png",
            "position": (self.camera.x, self.camera.y + 2 * self.H),
            "flipH" : True
        }
        self.lose = Gfx.create_fixed(params)
        self.playerProjectileManager = ProjectileManager()
        self.enemyProjectileManager = ProjectileManager()
        self.player = Player(self.playerProjectileManager, self.camera, initPos=(500, 500))
        self.countdown = Countdown(self.camera,self.process,60)
        self.HPBar = HPBar(self.camera,self.player,self.process)
        self.branchMgr = BranchManager()
        self.endTime = 2
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
        self.endGame = None

        #15 trop dur
        #10 level high
        #5 normal
        for i in range(0,10):
            self.enemyManager.randomSpawn()


    def update(self, deltaTime):
        if not self.started:
            self.started = True
            arcade.play_sound(self.music, 1.0, 0.0, True)

        self.background.update(deltaTime)

        if self.endGame is None and self.started:

            if self.player.hp <= 0.0 and self.endGame is None:
                self.endGame = "lose"
                print("YOU LOSE")
            if self.countdown.timeSecondes <= 0.0 and self.endGame is None:
                self.endGame = "win"
                print("YOU WIN")

            self.player.update(deltaTime)
            self.playerProjectileManager.update(deltaTime)
            if not DEBUG_REMOVE_ENEMY_PROJECTILES:
                self.enemyProjectileManager.update(deltaTime)
            self.enemyManager.update(deltaTime)
            self.collMgr.update()
            self.branchMgr.update(deltaTime)
            self.collMgrEnemy.update()
            self.countdown.update(deltaTime)
            self.camera.update( self.player.bodyL.center_x,
                                self.player.bodyL.center_y )

        if self.endGame is not None:
            # move win or lose
            spr = self.win
            if self.endGame == "lose":
                spr = self.lose
            spr.center_x = self.camera.x
            spr.center_y = spr.center_y * 0.95 + 0.05*self.camera.y
            self.endTime -= deltaTime
            if self.endTime < 0:
                self.endTime = 0

    def draw(self):
        self.background.draw()
        self.branchMgr.draw()
        self.enemyManager.draw()
        self.enemyProjectileManager.draw()
        self.playerProjectileManager.draw()
        self.player.draw()
        self.countdown.draw()
        self.HPBar.draw()
        self.win.draw()
        self.lose.draw()
        arcade.draw_rectangle_outline(0, 0, self.camera.maxWidth*2, self.camera.maxHeight*2,
                                      (200,255,200,128), 10)

    def onKeyEvent(self, key, isPressed):
        if self.endGame is None:
            if key == arcade.key.Q:
                self.player.moveLeft(isPressed)
            if key == arcade.key.D:
                self.player.moveRight(isPressed)
            if key == arcade.key.Z:
                self.player.moveUp(isPressed)
            if key == arcade.key.S:
                self.player.moveDown(isPressed)

            if self.endTime <= 0 and not isPressed:
                self.process.selectPage(1)


    def onMouseMotionEvent(self, x, y, dx, dy):
        self.player.viewTo(x, y)

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        if not hasattr(self,"player") :
            return

        if self.endGame is None:
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
        if self.endTime <= 0 and not isPressed:
            self.process.selectPage(1)

