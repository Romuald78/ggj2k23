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
from classes.Root import Root
from core.utils.utils import Gfx


class Page0Intro():

    def __init__(self, w, h, window: arcade.Window, process=None):
        super().__init__()
        self.window = window
        self.W = w
        self.H = h
        self.process = process

    def setup(self):
        params = {
            "filePath" : "resources/images/ggj2023.png",
            "size"     : (self.W, self.H),
            "position" : (self.W//2, self.H//2),
            "filterColor": (255,255,255,0)
        }
        self.ggj = Gfx.create_fixed(params)
        params["filePath"] = "resources/images/arcade.png"
        self.arcade = Gfx.create_fixed(params)
        params["filePath"] = "resources/images/rphstudio.png"
        self.rph   = Gfx.create_fixed(params)
        self.timer = 0
        self.initTimer = 0
        self.imgs  = [self.ggj, self.arcade, self.rph]
        self.index = 0

    def startGame(self):
        self.process.selectPage(1)

    def update(self, deltaTime):
        self.initTimer+=deltaTime
        PERIOD = 1
        if self.index < len(self.imgs):
            self.timer += deltaTime
            if self.timer <= PERIOD:
                pass
            elif self.timer <= 2*PERIOD:
                self.imgs[self.index].color = (255,255,255,255*(self.timer-PERIOD)//PERIOD)
            elif self.timer <= 3*PERIOD:
                self.imgs[self.index].color = (255,255,255,255)
            elif self.timer <= 4*PERIOD:
                self.imgs[self.index].color = (255,255,255,255-255*(self.timer-3*PERIOD)//PERIOD)
            else:
                self.index += 1
                self.timer = PERIOD
        else:
            self.startGame()

    def draw(self):
        if self.index < len(self.imgs):
            self.imgs[self.index].draw()

    def onKeyEvent(self, key, isPressed):
        if not isPressed:
            self.startGame()

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        if not hasattr(self,"initTimer"):
            return
        if not isPressed:
            self.startGame()

    def onMouseMotionEvent(self, x, y, dx, dy):
        pass

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        pass