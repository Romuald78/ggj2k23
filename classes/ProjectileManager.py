import arcade

PLAYER_PROJ = "player_proj"

# https://api.arcade.academy/en/latest/api/sprite_list.html
class ProjectileManager():

    def __init__(self):
        self.projs = arcade.SpriteList()
        self.defines = {
            PLAYER_PROJ: {
                "path":"resources/images/gun.png"
            },
        }

        pass

    def createProjectile(self,initPos=(0,0),speed=(1,0),projectile=PLAYER_PROJ):
        projectile_ = self.defines[projectile]
        sprite = arcade.Sprite(projectile_["path"])
        sprite.center_x = initPos[0]
        sprite.center_y = initPos[1]
        sprite.speed = speed
        self.projs.append(sprite)
        pass

    def update(self ,deltaTime):
        for sprite in self.projs:
            sprite.center_x = sprite.center_x + sprite.speed[0]
            sprite.center_y = sprite.center_y + sprite.speed[1]
        self.projs.update()

    def draw(self):
        self.projs.draw()