### ====================================================================================================
### IMPORTS
### ====================================================================================================

from core.pages.page_1_home import Page1Home


class Process:
    ### ====================================================================================================
    ### PARAMETERS
    ### ====================================================================================================

    ### ====================================================================================================
    ### CONSTRUCTOR
    ### ====================================================================================================
    def __init__(self, width, height, ratio, window):
        self.SCREEN_WIDTH = int(width * ratio)
        self.SCREEN_HEIGHT = int(height * ratio)
        self.window = window

    ### ====================================================================================================
    ### INIT
    ### ====================================================================================================
    def setup(self):
        # Add all pages
        self.pages = []
        # Instanciate all pages
        self.pages.append(Page1Home(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.window))
        # Set first page
        self.pageIndex = 0
        self.currentPage = self.pages[self.pageIndex]
        # Setup all the pages only once
        for p in self.pages:
            p.setup()
        # FPS
        self.frame_count = 0
        self.frame_time = 0.0

    ### ====================================================================================================
    ### UPDATE
    ### ====================================================================================================
    def update(self, deltaTime):
        try:
            self.frame_time += deltaTime
            self.frame_count += 1
            self.currentPage.update(deltaTime)
        except:
            pass

    ### ====================================================================================================
    ### RENDERING
    ### ====================================================================================================
    def draw(self):
        try:
            self.currentPage.draw()
            # if self.frame_count > 60:
            #     print(int(60/self.frame_time))
            #     self.frame_count = 0
            #     self.frame_time = 0.0
        except:
            pass

    ### ====================================================================================================
    ### KEYBOARD EVENTS
    ### key is taken from : arcade.key.xxx
    ### ====================================================================================================
    def onKeyEvent(self, key, isPressed):
        try:
            self.currentPage.onKeyEvent(key, isPressed)
        except:
            pass

    ### ====================================================================================================
    ### GAMEPAD BUTTON EVENTS
    ### buttonName can be "A", "B", "X", "Y", "LB", "RB", "VIEW", "MENU", "LSTICK", "RSTICK"
    ### ====================================================================================================
    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        try:
            self.currentPage.onButtonEvent(gamepadNum, buttonName, isPressed)
        except:
            pass

    ### ====================================================================================================
    ### GAMEPAD AXIS EVENTS
    ### axisName can be "X", "Y", "RX", "RY", "Z"
    ### ====================================================================================================
    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        try:
            self.currentPage.onAxisEvent(gamepadNum, axisName, analogValue)
        except:
            pass

    ### ====================================================================================================
    ### MOUSE MOTION EVENTS
    ### ====================================================================================================
    def onMouseMotionEvent(self, x, y, dx, dy):
        try:
            self.currentPage.onMouseMotionEvent(x, y, dx, dy)
        except:
            pass

    ### ====================================================================================================
    ### MOUSE BUTTON EVENTS
    ### ====================================================================================================
    def onMouseButtonEvent(self, x, y, buttonNum, isPressed):
        try:
            self.currentPage.onMouseButtonEvent(x, y, buttonNum, isPressed)
        except:
            pass
