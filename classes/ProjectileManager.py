import math
import random

import arcade

from classes.Projectile import Projectile

PLAYER_PROJ = "player_proj"
ENEMY_PROJ = "enemy_proj"

# https://api.arcade.academy/en/latest/api/sprite_list.html
class ProjectileManager():

    def __init__(self):
        self.activated = True #for dev
        self.projs = arcade.SpriteList()
        self.defines = {
            PLAYER_PROJ: {
                "path":"resources/images/player_projectile.png",
                "color":(255,255,255,255),
                "scale":0.5,
                "speed":(2000,2000)
            },
            ENEMY_PROJ: {
                "path":"resources/images/enemy_projectile.png",
                "color":(255,255,255,255),
                "scale":0.3,
                "speed":(500,500)
            }
        }

    def __updateOneSprite(self, sprite, deltaTime):
        # Move sprite
        sprite.center_x += (sprite.speed[0]+sprite.parentSpeed[0]) * sprite.direction[0] * deltaTime
        sprite.center_y += (sprite.speed[1]+sprite.parentSpeed[1]) * sprite.direction[1] * deltaTime
        # Remove sprite if life time is over
        sprite.lifeTime -= deltaTime
        if sprite.lifeTime <= 0 or sprite.userData.hp <= 0:
            self.projs.remove(sprite)

    def createProjectile(self, initPos=(0,0), direction=(1,0), projectile=PLAYER_PROJ, parentSpeed=(0,0)):
        if(not self.activated):
            return
        # add randomness for projectile (10%)
        dx = direction[0] + random.randint(-100,100)/1000
        dy = direction[1] + random.randint(-100,100)/1000
        projectile_ = self.defines[projectile]
        sprite = arcade.Sprite(projectile_["path"])
        sprite.color = projectile_["color"]
        sprite.scale = projectile_["scale"]
        sprite.speed = projectile_["speed"]
        sprite.parentSpeed = parentSpeed
        sprite.center_x = initPos[0]
        sprite.center_y = initPos[1]
        sprite.lifeTime = 3.0
        sprite.hp = 1
        sprite.angle = 180 * math.atan2(dy,dx) / math.pi
        sprite.direction = (dx,dy)
        sprite.userData = Projectile(1,1)
        self.projs.append(sprite)

    def update(self ,deltaTime):
        for sprite in self.projs:
            self.__updateOneSprite(sprite, deltaTime)
        self.projs.update()

    def draw(self):
        try:
            self.projs.draw()
        except:
            pass #yolo



