import math
import random

import arcade

from classes import Player
from classes.Branch import Branch
from classes.Enemy import Enemy

MAIN_ENEMY = "main_enemy"


# https://api.arcade.academy/en/latest/api/sprite_list.html
class EnemyManager():

    def __init__(self, camera, projectileManager, branchMgr, player):
        self.enemies = arcade.SpriteList()
        self.defines = {
            MAIN_ENEMY: {
                "path": "resources/images/enemy.png"
            }
        }
        self.SPAWN_TIME = 0.25  # secondes betwwen enemy spawn
        self.lastSpawn = 0
        self.camera = camera
        self.projectileManager = projectileManager
        self.player = player
        self.branchMgr = branchMgr

    def createEnemy(self, initPos=(0, 0), enemy=MAIN_ENEMY):
        # add randomness for projectile (10%)
        enemy_ = self.defines[enemy]
        sprite = arcade.Sprite(enemy_["path"], scale=0.1)
        sprite.center_x = initPos[0]
        sprite.center_y = initPos[1]
        sprite.userData = Enemy(sprite, self.projectileManager)
        self.enemies.append(sprite)
        # create first branch of flower
        brnch = Branch( initPos, 0, self.branchMgr, self.player )
        sprite.userData.addBranch(brnch)


    def checkRemove(self, sprite):
        # Remove sprite if life time is over
        if sprite.userData.hp <= 0:
            self.enemies.remove(sprite)

    def enemyAim(self, enemy: Enemy, x, y):
        enemy.target(x, y)

    def update(self, deltaTime):
        self.lastSpawn += deltaTime
        self.enemies.update()

        for sprite in self.enemies:
            enemy: Enemy = sprite.userData
            enemy.update(deltaTime)
            self.checkRemove(sprite)
            self.enemyAim(sprite.userData, self.player.center_x, self.player.center_y)

        if self.lastSpawn > self.SPAWN_TIME:
            self.lastSpawn -= self.SPAWN_TIME

            radius = max(self.camera.W, self.camera.H) / 2
            delta = min(self.camera.W, self.camera.H) / 2
            radius += random.randint(0, delta)
            ang = random.randint(0, 360)
            x = radius * math.cos(ang * math.pi / 180)
            y = radius * math.sin(ang * math.pi / 180)
            y = y * 1.0 * self.camera.H / self.camera.W
            x += self.camera.x
            y += self.camera.y
            self.createEnemy((x, y))

    def draw(self):
        self.enemies.draw()
