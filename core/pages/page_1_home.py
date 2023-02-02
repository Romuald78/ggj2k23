import random

import arcade

from core.shaders.track_path import TrackPathShader
from core.ships.ship_core import Ship
from core.tracks.track import Track
from students.student_script import Student10


# TODO : use SpriteList to increase perfs ?
# TODO : SpriteList would gather all ship sprites
class Page1Home():

    def __update_viewport(self):
        x0 = 1000000000
        x1 = -1000000000
        y0 = 1000000000
        y1 = -1000000000
        ship_radius = 50
        for ship in self.ships:
            x0 = min(x0, ship.stat.center_x)
            x1 = max(x1, ship.stat.center_x)
            y0 = min(y0, ship.stat.center_y)
            y1 = max(y1, ship.stat.center_y)

        x0, y0, x1, y1 = self.track.getViewport()

        xm = (x0 + x1) / 2
        ym = (y0 + y1) / 2
        W = self.vp[1] - self.vp[0]
        H = self.vp[3] - self.vp[2]
        dx = x1 - x0 + 2 * ship_radius
        dy = y1 - y0 + 2 * ship_radius
        ratiox = dx / W
        ratioy = dy / H
        ratio = max(ratiox, ratioy)
        ratio = max(0.75, ratio)
        W = ratio * W
        H = ratio * H
        self.window.set_viewport(xm - W / 2, xm + W / 2, ym - H / 2, ym + H / 2)
        self.view_ratio = 1.5 / ratio

    def __getNormPos(self, pos):
        vp = self.window.get_viewport()
        w = vp[1] - vp[0]
        h = vp[3] - vp[2]
        x0 = vp[0]
        y0 = vp[2]
        xn = (pos[0] - x0) / w
        yn = (pos[1] - y0) / h
        return (xn, yn)

    def __init__(self, w, h, window: arcade.Window):
        super().__init__()
        self.window = window
        self.vp = self.window.get_viewport()
        self.W = w
        self.H = h
        self.ships = []
        self.track = Track(1)  # TODO track loading will be done in setup ??
        self.view_ratio = 1.0
        # Time management
        self.time_upd = 1  # number of frame to update
        self.time_drw = 1  # number of frames to draw
        self.time_count = 0  # value to know when to update
        # Shaders
        self.shaders = {
            "track_path": TrackPathShader(int(self.vp[1]), int(self.vp[3]))
        }

    def setup(self):
        for i in range(30):
            ship = Ship(Student10())
            self.ships.append(ship)

        # Load track
        # TODO
        # Set all ships at start position
        for ship in self.ships:
            ship.stat.center_x = self.track.CPs[0][0]
            ship.stat.center_y = self.track.CPs[0][0]

    def update(self, deltaTime):

        # Frame Time management
        self.time_count = (self.time_count + 1) % self.time_drw
        if self.time_upd < self.time_drw and self.time_count != 0:
            return

        # --------------------------------
        # Frame update
        for i in range(self.time_upd):
            # Update track checkpoint positions
            try:
                self.track.update()
            except Exception as ex:
                print("[ERROR][Phase=track.update]")
                print(ex)

            # Prepare AI scripts
            for ship in self.ships:
                try:
                    ship.prepare_actions(self.track)
                except Exception as ex:
                    print("[ERROR][Phase=prepare_actions]")
                    print(ex)

            # Process AI scripts
            for ship in self.ships:
                try:
                    ship.process_actions()
                except Exception as ex:
                    print("[ERROR][Phase=process_actions]")
                    print(ex)

            # Apply actions
            for ship in self.ships:
                try:
                    ship.apply_actions()
                except Exception as ex:
                    print("[ERROR][Phase=apply_actions]")
                    print(ex)

            # Update sprites according to actions
            for ship in self.ships:
                try:
                    ship.update()
                except Exception as ex:
                    print("[ERROR][Phase=ship.update]")
                    print(ex)

        # --------------------------------
        # Change Camera position (only once
        self.__update_viewport()

    def draw(self):

        # Clear buffers (main and framebuffer objects)
        self.window.clear()
        self.shaders["track_path"].clear()
        #
        # # Set uniform variables for this shader
        # # TODO : SHADER
        # posA = (self.track.getPositionCP(0))
        # posB = (self.track.getPositionCP(1))
        # posC = (self.track.getPositionCP(2))
        # posD = (self.track.getPositionCP(3))
        # posE = (self.track.getPositionCP(4))
        # points = [posA,posB,posC,posD,posE]
        # my_line_strip = arcade.create_line_strip(points, (255,255,255), 5)
        # shape_list = arcade.ShapeElementList()
        # shape_list.append(my_line_strip)
        # self.shaders["track_path"].setTrackPath(posA, posB, posC, posD, posE)
        # self.shaders["track_path"].setViewRatio(self.view_ratio)

        # Draw background
        self.window.use()


        # Use shader
        self.shaders["track_path"].use()
        # Draw track
        self.track.draw()
        # draw Track framebuffer on the main screen
        self.window.use()
        self.shaders["track_path"].draw()



        # Draw ships
        for ship in self.ships:
            try:
                ship.draw()
            except Exception as ex:
                print("Ship Drawing EXCEPTION : " + str(ex))

    def onKeyEvent(self, key, isPressed):
        # Increase time speed
        if (key == arcade.key.NUM_ADD or key == arcade.key.P) and isPressed:
            if self.time_upd >= self.time_drw:
                self.time_upd *= 2
            else:
                self.time_drw //= 2
        # Decrease time speed
        if (key == arcade.key.NUM_SUBTRACT or key == arcade.key.M) and isPressed:
            if self.time_upd > self.time_drw:
                self.time_upd //= 2
            else:
                self.time_drw *= 2
