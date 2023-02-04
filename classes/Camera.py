

class Camera():

    def __init__(self, win, x, y, w, h):
        self.window = win
        self.W = w
        self.H = h
        self.x = 0
        self.y = 0

    def update(self, x, y):
        xm = x - self.W / 2
        ym = y - self.H / 2
        xp = xm + self.W
        yp = ym + self.H
        self.x = x
        self.y = y
        self.window.set_viewport(xm, xp, ym, yp)
