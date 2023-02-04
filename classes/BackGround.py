import math
import random

import arcade

from classes import Camera
from core.utils.utils import Gfx


class Background:

    def mkTile(self):
        idx = random.randint(0,2)
        return Gfx.create_animated({
            "filePath": "resources/images/background_tile.png",
            #"size": (100, 100),
            "filterColor": (255, 255, 255, 255),
            "spriteBox":(3,1,300,300),
            "startIndex":idx,
            "endIndex":idx,
            "frameDuration":1,
        })

    def mkItem(self):
        idx = random.randint(0,8)
        return Gfx.create_animated({
            "filePath": "resources/images/background_items.png",
            "size": (60, 60),
            "filterColor": (255, 255, 255, 255),
            "spriteBox":(3,3,540//3,540//3),
            "startIndex":idx,
            "endIndex":idx,
            "frameDuration":1,
        })

    def __init__(self, camera: Camera, size=3000):
        self.tiles = arcade.SpriteList()
        self.deco = arcade.SpriteList()
        self.camera = camera
        sprite = self.mkTile()
        self.tiles.append(sprite)
        self.tileWidth = int(sprite.width)
        self.tileHeight = int(sprite.height)
        self.areaSize = size
        self.tiles.remove(sprite)
        self.tilesMap = {}

    def update(self, deltaTime):
        self.tiles.update()
        self.deco.update()
        camx = int(self.camera.x)
        camy = int(self.camera.y)
        # create new tiles
        size_ = self.areaSize // 2
        for x in range(camx - size_, (camx + size_)+self.tileHeight, int(self.tileWidth)):
            for y in range(camy - size_, (camy + size_) +self.tileHeight , int(self.tileHeight)):
                alignedX = int(x // self.tileWidth) * self.tileWidth
                alignedY = int(y // self.tileHeight) * self.tileHeight
                id = str(alignedX) + "#" + str(alignedY)
                if not id in self.tilesMap:
                    #print("create tile "+str(alignedX)+" / "+str(alignedY))
                    sprite = self.mkTile()
                    sprite.items = []
                    sprite.center_x = alignedX
                    sprite.center_y = alignedY
                    self.tiles.append(sprite)
                    self.tilesMap[id] = sprite
                    #generate item on map
                    for i in range(0,random.randint(0,3)):
                        itemSprite = self.mkItem()
                        itemSprite.center_x = sprite.center_x + random.randint(-self.tileWidth//2,+self.tileWidth//2)
                        itemSprite.center_y = sprite.center_y + random.randint(-self.tileHeight//2,+self.tileHeight//2)
                        sprite.items.append(itemSprite)
                        self.deco.append(itemSprite)

        # remove tiles out of bound
        refCamPos = [camx, camy]
        for key in list(self.tilesMap):
            sprite = self.tilesMap[key]
            if math.dist([sprite.center_x, sprite.center_y], refCamPos) > self.areaSize:
                #print("remove tile "+str(sprite.center_x)+" / "+str(sprite.center_y)+ " "+key)
                self.tiles.remove(sprite)
                for itemSprite in sprite.items:
                    self.deco.remove(itemSprite)
                del self.tilesMap[key]

    def draw(self):
        self.tiles.draw()
        self.deco.draw()
        pass
