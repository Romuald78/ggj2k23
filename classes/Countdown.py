from classes import Camera
from core.utils.utils import Text, Gfx


class Countdown:
    def __init__(self,camera:Camera,process, timeSecondes = 1*60):
        self.timeSecondes = timeSecondes
        self.camera = camera
        self.sprite = Gfx.create_fixed({
            "filePath": "resources/images/ui_chrono.png",
            "filterColor": (255, 255, 255, 255),
        })
        self.pos = (-(self.camera.W // 2) + 90, (self.camera.H // 2) - 70)
        #
        self.sprite.angle = 0
        self.sprite.scale = 0.5
        self.process = process

    def draw(self):
        seconds = self.timeSecondes
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        formatted_time = "{:02d}:{:02d}".format(int(minutes), int(remaining_seconds))

        self.sprite.center_x = self.camera.x - (self.camera.W // 2) + (self.sprite.width // 2)
        self.sprite.center_y = self.camera.y + (self.camera.H // 2) - (self.sprite.height // 2)
        self.sprite.draw()
        message = formatted_time
        Text.draw({"x": self.camera.x + self.pos[0],
                    "y": self.camera.y + self.pos[1],
                    "alignH": "center",
                    "alignV": "center",
                    "message": message,
                    "size": 30,
                    "color": (0, 0, 0, 255),
                    "angle":19
                    })

    def update(self, deltaTime):
        if(self.timeSecondes < 0):
            self.timeSecondes += 1000000000
            print("You WIN")
            #self.process.setup()
            self.process.selectPage(4)
        self.timeSecondes -= deltaTime