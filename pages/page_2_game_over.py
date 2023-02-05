import random

import arcade

from core.utils.utils import Gfx


class Page2GameOver():

    def __init__(self, w, h, window: arcade.Window, process=None):
        super().__init__()
        self.window = window
        self.W = w
        self.H = h
        self.process = process

    def refresh(self):
        pass

    def setup(self):
        self.steps = 0
        params = {
            "filePath" : "resources/images/hazmat_boy.png",
            "position" : (self.W//2, 5*self.H//4),
            "filterColor": (255,255,255,255)

        }
        self.hazmat = Gfx.create_fixed(params)
        params = {
            "filePath": "resources/images/VS.png",
            "position": (3*self.W // 2, 0.63 * self.H ),
            "filterColor": (255, 255, 255, 255)

        }
        self.vs = Gfx.create_fixed(params)
        params = {
            "filePath": "resources/images/the_evil_roots.png",
            "position": (self.W // 2, 5 * self.H // 4),
            "filterColor": (255, 255, 255, 255)

        }
        self.evilRoots = Gfx.create_fixed(params)
        params = {
            "filePath": "resources/images/From_beyond.png",
            "position": (self.W // 2, - self.H // 4),
            "filterColor": (255, 255, 255, 255)

        }
        self.fromBeyond = Gfx.create_fixed(params)
        params = {
            "filePath": "resources/images/BG.png",
            "position": (self.W // 2,  self.H // 2),
            "filterColor": (255, 255, 255, 255)
        }
        self.bg = Gfx.create_fixed(params)
        self.timer = 1
        self.initTimer = 0
        params = {
                "filePath": "resources/images/enemy.png",
                "scale": 0.3,
                "filterColor": (255, 255, 255, 0),
                "spriteBox": (3, 1, 1376//4, 356),
                "startIndex": 0,
                "endIndex": 2,
                "frameDuration": 0.30,
        }
        self.enemy = Gfx.create_animated(params)
        self.enemy.scale = 1.25
        self.enemy.center_y = self.enemy.height/2
        self.enemy.center_x = self.W / 6

    def update(self, deltaTime):
        self.initTimer += deltaTime
        self.enemy.update_animation(deltaTime)
        timer_HM = 2
        timer_VS = 0.75
        timer_ER = 0.75
        timer_FB = 0.75
        timer_EN = 1.5
        # Time control
        self.timer -= deltaTime
        if self.steps == 0:
            if self.timer < 0:
                self.timer = timer_HM
                self.steps += 1

        # set Hazmat from sky to ground
        if self.steps == 1:
            self.hazmat.center_y = 3*self.H//4
            self.hazmat.scale = 1 + (self.timer)*20
            if self.timer < 0:
                self.hazmat.scale = 1
                self.timer = timer_VS
                self.steps += 1

        # set VS
        if self.steps == 2:
            self.vs.center_x = ((5*self.W//6) * (timer_VS-self.timer) + (5*self.W//4) * self.timer)/timer_VS
            if self.timer < 0:
                self.timer = timer_ER
                self.steps += 1

        # set Evil Roots
        if self.steps == 3:
            self.evilRoots.center_y = ((self.H//1.9) * (timer_ER-self.timer) + (-self.H//4) * self.timer)/timer_ER
            if self.timer < 0:
                self.timer = timer_FB
                self.steps += 1

        # set from beyond
        if self.steps == 4:
            self.fromBeyond.center_y = ((self.H//3) * (timer_FB-self.timer) + (-self.H//4) * self.timer)/timer_FB
            if self.timer < 0:
                self.timer = timer_EN
                self.steps += 1

        # enemy
        if self.steps == 5:
            a = 255 - int(255 * self.timer / timer_EN)
            a = min(255, max(0, a))
            self.enemy.color = (255,255,255,a)
            if self.timer < 0:
                self.enemy.color = (255,255,255,255)
                self.timer = 2
                self.steps += 1

        # blink start
        if self.steps == 6:
            if self.timer < 0:
                self.timer = 2


    def draw(self):
        self.bg.draw()
        self.hazmat.draw()
        self.vs.draw()
        self.evilRoots.draw()
        self.fromBeyond.draw()
        self.enemy.draw()

    def startGame(self, ctrlID):
        self.process.selectPage(1)#start page

    def onKeyEvent(self, key, isPressed):
        if not isPressed and self.initTimer>1:
            self.startGame(-1)

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        if not isPressed and self.initTimer>1:
            self.startGame(gamepadNum)

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        pass

    def onMouseMotionEvent(self, x, y, dx, dy):
        pass
