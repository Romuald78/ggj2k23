import math

from arcade import Sprite


class IGunner():

    def __init__(self, projName, projectileManager, fireRateSecond=0.1):
        self.shootTimer = 0
        self.fireRate = fireRateSecond
        self.projName = projName
        self.projectileManager = projectileManager
        self.view_x = 1
        self.view_y = 0

    def viewToGunner(self, body: Sprite, x, y):
        dx = x - body.center_x
        dy = -y + body.center_y
        norm = math.sqrt(self.view_x * self.view_x + self.view_y * self.view_y)
        dx /= norm
        dy /= norm
        self.view_x = dx
        self.view_y = dy

    def updateGunner(self, deltatime, body: Sprite):
        self.shootTimer += deltatime
        if self.shootTimer > self.fireRate:
            self.shootTimer -= self.fireRate
            norm = math.sqrt(self.view_x * self.view_x + self.view_y * self.view_y)
            self.projectileManager.createProjectile(
                (body.center_x, body.center_y),
                (self.view_x / norm, -self.view_y / norm),
                self.projName)
                #body.userData.getSpeed()) not a gud idea
