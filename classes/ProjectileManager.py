import math
import random

import arcade

from classes.Projectile import Projectile

PLAYER_PROJ = "player_proj"
ENEMY_PROJ = "enemy_proj"

# https://api.arcade.academy/en/latest/api/sprite_list.html
class ProjectileManager():

    def __init__(self, proj_speed=1000):
        self.activated = True #for dev
        self.projs = arcade.SpriteList()
        self.defines = {
            PLAYER_PROJ: {
                "path":"resources/images/player_projectile.png",
                "color":(255,255,128,255),
                "scale":0.5
            },
            ENEMY_PROJ: {
                "path":"resources/images/enemy_projectile.png",
                "color":(128,128,255,255),
                "scale":0.5
            }
        }
        self.proj_speed = proj_speed

    def __updateOneSprite(self, sprite, deltaTime):
        # Move sprite
        sprite.center_x += self.proj_speed * sprite.direction[0] * deltaTime
        sprite.center_y += self.proj_speed * sprite.direction[1] * deltaTime
        # Remove sprite if life time is over
        sprite.lifeTime -= deltaTime
        if sprite.lifeTime <= 0 or sprite.userData.hp <= 0:
            self.projs.remove(sprite)

    def createProjectile(self, initPos=(0,0), direction=(1,0), projectile=PLAYER_PROJ):
        if(not self.activated):
            return
        # add randomness for projectile (10%)
        dx = direction[0] + random.randint(-100,100)/1000
        dy = direction[1] + random.randint(-100,100)/1000
        projectile_ = self.defines[projectile]
        sprite = arcade.Sprite(projectile_["path"])
        sprite.color = projectile_["color"]
        sprite.scale = projectile_["scale"]
        sprite.center_x = initPos[0]
        sprite.center_y = initPos[1]
        sprite.lifeTime = 2.0
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
        self.projs.draw()



