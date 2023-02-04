import math
import random

import arcade

PLAYER_PROJ = "player_proj"
PROJ_SPEED = 2000

# https://api.arcade.academy/en/latest/api/sprite_list.html
class ProjectileManager():

    def __init__(self):
        self.projs = arcade.SpriteList()
        self.defines = {
            PLAYER_PROJ: {
                "path":"resources/images/player_projectile.png"
            }
        }

    def __updateOneSprite(self, sprite, deltaTime):
        # Move sprite
        sprite.center_x += PROJ_SPEED * sprite.direction[0] * deltaTime
        sprite.center_y += PROJ_SPEED * sprite.direction[1] * deltaTime
        # Remove sprite if life time is over
        sprite.lifeTime -= deltaTime
        if sprite.lifeTime <= 0 or sprite.hp <= 0:
            self.projs.remove(sprite)

    def createProjectile(self, initPos=(0,0), direction=(1,0), projectile=PLAYER_PROJ):
        # add randomness for projectile (10%)
        dx = direction[0] + random.randint(-100,100)/1000
        dy = direction[1] + random.randint(-100,100)/1000
        projectile_ = self.defines[projectile]
        sprite = arcade.Sprite(projectile_["path"])
        sprite.center_x = initPos[0]
        sprite.center_y = initPos[1]
        sprite.lifeTime = 0.5
        sprite.hp = 1
        sprite.angle = 180 * math.atan2(dy,dx) / math.pi
        sprite.direction = (dx,dy)
        self.projs.append(sprite)

    def update(self ,deltaTime):
        for sprite in self.projs:
            self.__updateOneSprite(sprite, deltaTime)
        self.projs.update()

    def draw(self):
        self.projs.draw()



