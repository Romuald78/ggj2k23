import arcade



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
        pass

    def update(self, deltaTime):
        pass

    def draw(self):
        pass


    def onKeyEvent(self, key, isPressed):
        pass

