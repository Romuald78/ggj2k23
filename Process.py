### ====================================================================================================
### IMPORTS
### ====================================================================================================

from pages.page_1_home import Page1Home


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
        self.frame_time += deltaTime
        self.frame_count += 1
        self.currentPage.update(deltaTime)

    ### ====================================================================================================
    ### RENDERING
    ### ====================================================================================================
    def draw(self):
        self.currentPage.draw()
        # if self.frame_count > 60:
        #     print(int(60/self.frame_time))
        #     self.frame_count = 0
        #     self.frame_time = 0.0

    ### ====================================================================================================
    ### KEYBOARD EVENTS
    ### key is taken from : arcade.key.xxx
    ### ====================================================================================================
    def onKeyEvent(self, key, isPressed):
        self.currentPage.onKeyEvent(key, isPressed)

    ### ====================================================================================================
    ### GAMEPAD BUTTON EVENTS
    ### buttonName can be "A", "B", "X", "Y", "LB", "RB", "VIEW", "MENU", "LSTICK", "RSTICK"
    ### ====================================================================================================
    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        self.currentPage.onButtonEvent(gamepadNum, buttonName, isPressed)

    ### ====================================================================================================
    ### GAMEPAD AXIS EVENTS
    ### axisName can be "X", "Y", "RX", "RY", "Z"
    ### ====================================================================================================
    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        self.currentPage.onAxisEvent(gamepadNum, axisName, analogValue)

    ### ====================================================================================================
    ### MOUSE MOTION EVENTS
    ### ====================================================================================================
    def onMouseMotionEvent(self, x, y, dx, dy):
        self.currentPage.onMouseMotionEvent(x, y, dx, dy)

    ### ====================================================================================================
    ### MOUSE BUTTON EVENTS
    ### ====================================================================================================
    def onMouseButtonEvent(self, x, y, buttonNum, isPressed):
        self.currentPage.onMouseButtonEvent(x, y, buttonNum, isPressed)
