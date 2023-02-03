import arcade

from classes.Player import Player


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
        self.player = Player( initPos=(500,500) )

    def update(self, deltaTime):
        self.player.update(deltaTime)

    def draw(self):
        self.player.draw()


    def onKeyEvent(self, key, isPressed):
        pass

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        if axisName == "X":
            if abs(analogValue) <= 0.2:
                analogValue = 0
            self.player.speed_x = analogValue
        if axisName == "Y":
            if abs(analogValue) <= 0.2:
                analogValue = 0
            self.player.speed_y = -analogValue
        if axisName == "RX":
            self.player.view_x = analogValue
        if axisName == "RY":
            self.player.view_y = analogValue

