### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade
from Process import Process
import os

### ====================================================================================================
### CONSTANTS
### ====================================================================================================
TITLE = "Python RGR coding challenge !"


### ====================================================================================================
### GAME CLASS
### ====================================================================================================
class MyGame(arcade.Window):
    BUTTON_NAMES = ["A",
                    "B",
                    "X",
                    "Y",
                    "LB",
                    "RB",
                    "VIEW",
                    "MENU",
                    "LSTICK",
                    "RSTICK",
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    ]

    # ----------------------------------
    # PRIVATE METHODS FOR INPUT MANAGEMENT
    # ----------------------------------
    def __onButtonPressed(self, _gamepad, button):
        idx = self.gamepads[_gamepad]
        self.onButtonPressed(idx, MyGame.BUTTON_NAMES[button])

    def __onButtonReleased(self, _gamepad, button):
        idx = self.gamepads[_gamepad]
        self.onButtonReleased(idx, MyGame.BUTTON_NAMES[button])

    def __onCrossMove(self, _gamepad, x, y):
        idx = self.gamepads[_gamepad]
        self.onCrossMove(idx, x, -y)

    def __onAxisMove(self, _gamepad, axis, value):
        idx = self.gamepads[_gamepad]
        self.onAxisMove(idx, axis, value)

    # ----------------------------------
    # PRIVATE METHODS FOR SCREEN COORDS
    # ----------------------------------
    def __convertXY(self, x, y):
        winW, winH = self.get_size()
        x0, x1, y0, y1 = self.get_viewport()
        x = x0 + x * (x1 - x0) / winW
        y = y0 + y * (y1 - y0) / winH
        return x, y

    def __toggleFullScreen(self):
        # toggle screen mode (process ratio must be compliant with screen resolution
        self.set_fullscreen(not self.fullscreen)
        if self.fullscreen:
            winW, winH = self.get_size()
            ratioX = self.process.SCREEN_WIDTH / winW
            ratioY = self.process.SCREEN_HEIGHT / winH
            ratio = max(ratioX, ratioY)
            finalW = int(round(ratio * winW, 0))
            finalH = int(round(ratio * winH, 0))
            x0 = -int((finalW - self.process.SCREEN_WIDTH) / 2)
            y0 = -int((finalH - self.process.SCREEN_HEIGHT) / 2)
            self.set_viewport(x0, finalW + x0, y0, finalH + y0)
        else:
            self.set_viewport(0, self.process.SCREEN_WIDTH, 0, self.process.SCREEN_HEIGHT)

    # ----------------------------------
    # CONSTRUCTOR
    # ----------------------------------
    def __init__(self, width, height, ratio, title):
        # init application window
        super().__init__(int(width*ratio), int(height*ratio), title)
        # init process object
        self.process = Process(width, height, ratio, self)
        # set application window background color
        arcade.set_background_color(arcade.color.BLACK)
        # Store gamepad list
        self.gamepads = arcade.get_joysticks()
        # check every connected gamepad
        if self.gamepads:
            for g in self.gamepads:
                # link all gamepad callbacks to the current class methods
                g.open()
                g.on_joybutton_press = self.__onButtonPressed
                g.on_joybutton_release = self.__onButtonReleased
                g.on_joyhat_motion = self.__onCrossMove
                g.on_joyaxis_motion = self.__onAxisMove
            # transform list into a dictionary to get its index faster
            self.gamepads = {self.gamepads[idx]: idx for idx in range(len(self.gamepads))}
        else:
            print("There are no Gamepad connected !")
            self.gamepads = None
        # full screen config
        self.appW = None
        self.appH = None

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #                                SETUP your game here
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def setup(self):
        # - - - - - - - - - - - - - - - - - - - - - - - - -#
        self.process.setup()
        # - - - - - - - - - - - - - - - - - - - - - - - - -#

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #                               DRAW your game elements here
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_draw(self):
        # - - - - - - - - - - - - - - - - - - - - - - - - -#
        arcade.start_render()
        self.process.draw()
        # - - - - - - - - - - - - - - - - - - - - - - - - -#

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #                                  UPDATE your game model here
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def update(self, delta_time):
        # - - - - - - - - - - - - - - - - - - - - - - - - -#
        self.process.update(delta_time)
        # - - - - - - - - - - - - - - - - - - - - - - - - -#

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # KEY PRESSED events
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_key_press(self, key, modifiers):
        # - - - - - - - - - - - - - - - - - - - - - - - - -#
        # Close application if ESCAPE key is hit
        if key == arcade.key.ESCAPE:
            self.close()
        if key == arcade.key.F11:
            self.__toggleFullScreen()
        self.process.onKeyEvent(key, True)
        # - - - - - - - - - - - - - - - - - - - - - - - - -#

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # KEY RELEASED events
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_key_release(self, key, modifiers):
        # - - - - - - - - - - - - - - - - - - - - - - - - -#
        self.process.onKeyEvent(key, False)
        # - - - - - - - - - - - - - - - - - - - - - - - - -#

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # GAMEPAD BUTTON PRESSED events
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def onButtonPressed(self, gamepadNum, buttonNum):
        # - - - - - - - - - - - - - - - - - - - - - - - - -#
        self.process.onButtonEvent(gamepadNum, buttonNum, True)
        # - - - - - - - - - - - - - - - - - - - - - - - - -#

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # GAMEPAD BUTTON RELEASED events
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def onButtonReleased(self, gamepadNum, buttonNum):
        # - - - - - - - - - - - - - - - - - - - - - - - - -#
        self.process.onButtonEvent(gamepadNum, buttonNum, False)
        # - - - - - - - - - - - - - - - - - - - - - - - - -#

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # GAMEPAD CROSSPAD events
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def onCrossMove(self, gamepadNum, xValue, yValue):
        # - - - - - - - - - - - - - - - - - - - - - - - - -#
        self.process.onAxisEvent(gamepadNum, "x", xValue)
        self.process.onAxisEvent(gamepadNum, "y", yValue)
        # - - - - - - - - - - - - - - - - - - - - - - - - -#

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # GAMEPAD AXIS events
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def onAxisMove(self, gamepadNum, axisName, analogValue):
        # - - - - - - - - - - - - - - - - - - - - - - - - -#
        if axisName == "z":
            analogValue = -analogValue
        self.process.onAxisEvent(gamepadNum, axisName.upper(), analogValue)
        # - - - - - - - - - - - - - - - - - - - - - - - - -#

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # MOUSE MOTION events
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_mouse_motion(self, x, y, dx, dy):
        x, y = self.__convertXY(x, y)
        self.process.onMouseMotionEvent(x, y, dx, dy)

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # MOUSE BUTTON PRESSED events
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_mouse_press(self, x, y, button, modifiers):
        x, y = self.__convertXY(x, y)
        self.process.onMouseButtonEvent(x, y, button, True)

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # MOUSE BUTTON RELEASED events
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def on_mouse_release(self, x, y, button, modifiers):
        x, y = self.__convertXY(x, y)
        self.process.onMouseButtonEvent(x, y, button, False)


### ====================================================================================================
### MAIN PROCESS
### ====================================================================================================
def main():
    # add current file path
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
    os.chdir(file_path)

    game = MyGame(1920, 1080, 0.8, TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
