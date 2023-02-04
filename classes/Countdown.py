from classes import Camera
from core.utils.utils import Text


class Countdown:
    def __init__(self,camera:Camera, initPos=(0, 0),timeSecondes = 1*60):
        self.timeSecondes = timeSecondes
        self.pos = initPos
        self.camera = camera

    def draw(self):
        seconds = self.timeSecondes
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        formatted_time = "{:02d}:{:02d}".format(int(minutes), int(remaining_seconds))

        message = formatted_time
        paramTxt = {"x": self.camera.x + self.pos[0],
                    "y": self.camera.y + self.pos[1],
                    "alignH": "center",
                    "alignV": "center",
                    "message": message,
                    "size": 50,
                    "color": (0, 0, 255, 128),
                    }
        Text.draw(paramTxt)

    def update(self, deltaTime):
        if(self.timeSecondes < 0):
            self.timeSecondes += 1000000000
            print("You WIN")
        self.timeSecondes -= deltaTime