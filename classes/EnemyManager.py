import math
import random

import arcade

from classes import Player
from classes.Enemy import Enemy

MAIN_ENEMY = "main_enemy"

# https://api.arcade.academy/en/latest/api/sprite_list.html
class EnemyManager():

    def __init__(self,projectileManager,player:Player):
        self.enemies = arcade.SpriteList()
        self.defines = {
            MAIN_ENEMY: {
                "path":"resources/images/enemy.png"
            }
        }
        self.SPAWN_TIME = 1 # secondes betwwen enemy spawn
        self.lastSpawn = 0
        self.W = 1000 #change
        self.H = 1000 #change
        self.projectileManager = projectileManager
        self.player = player

    def createEnemy(self, initPos=(0,0), enemy=MAIN_ENEMY):
        # add randomness for projectile (10%)
        enemy_ = self.defines[enemy]
        sprite = arcade.Sprite(enemy_["path"],scale=0.1)
        sprite.center_x = initPos[0]
        sprite.center_y = initPos[1]
        sprite.userData = Enemy(sprite,self.projectileManager)
        self.enemies.append(sprite)

    def checkRemove(self, sprite):
        # Remove sprite if life time is over
        if sprite.userData.hp <= 0:
            self.enemies.remove(sprite)

    def enemyAim(self, enemy:Enemy,x,y):
        enemy.target(x,y)

    def update(self,deltaTime):
        self.lastSpawn += deltaTime
        self.enemies.update()

        for sprite in self.enemies:
            enemy:Enemy = sprite.userData
            enemy.update(deltaTime)
            self.checkRemove(sprite)
            self.enemyAim(sprite.userData,self.player.center_x,self.player.center_y)

        if self.lastSpawn > self.SPAWN_TIME:
            self.lastSpawn -= self.SPAWN_TIME
            self.createEnemy((random.randint(0,self.W),random.randint(0,self.H)))


    def draw(self):
        self.enemies.draw()



