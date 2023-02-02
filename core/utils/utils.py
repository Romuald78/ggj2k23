import arcade
import math
from random import *


# ===============================================
class Sound():
    # ===========================================

    @staticmethod
    def create(fileName):
        snd = arcade.load_sound(fileName)
        return snd


# ===============================================
class Text():
    # ===========================================

    @staticmethod
    def draw(params):
        # retrieve parameters
        x = params["x"]
        y = params["y"]
        message = params["message"]
        size = 12 if "size" not in params else params["size"]
        color = (255, 255, 255, 255) if "color" not in params else params["color"]
        alignH = "center" if "alignH" not in params else params["alignH"]  # left, center, right
        alignV = "center" if "alignV" not in params else params["alignV"]  # top, center, bottom
        angle = 0 if "angle" not in params else params["angle"]
        bold = False if "bold" not in params else params["bold"]
        italic = False if "italic" not in params else params["italic"]
        # draw text according to configuration
        arcade.draw_text(text=message, start_x=x, start_y=y, color=color, font_size=size, anchor_x=alignH,
                         anchor_y=alignV, rotation=angle, bold=bold, italic=italic)


# ===============================================
class Gfx():
    # ===========================================

    @staticmethod
    def create_fixed(params):
        # retrieve parameters
        filePath = params["filePath"]
        size = None if "size" not in params else params["size"]
        filterColor = (255, 255, 255, 255) if "filterColor" not in params else params["filterColor"]
        isMaxRatio = False if "isMaxRatio" not in params else params["isMaxRatio"]
        position = (0, 0) if "position" not in params else params["position"]
        flipH = False if "flipH" not in params else params["flipH"]
        flipV = False if "flipV" not in params else params["flipV"]

        # load texture for sprite
        texture = arcade.load_texture(filePath, flipped_horizontally=flipH, flipped_vertically=flipV)
        akf = arcade.AnimationKeyframe(0, 1, texture)
        # Create sprite
        spr = arcade.AnimatedTimeBasedSprite()
        spr.color = filterColor
        spr.frames.append(akf)
        # Select first frame
        spr.texture = spr.frames[0].texture
        # set dimensions
        if size != None:
            if isMaxRatio:
                ratio = max(size[0] / spr.width, size[1] / spr.height)
            else:
                ratio = min(size[0] / spr.width, size[1] / spr.height)
            spr.scale = ratio
        # set position
        spr.center_x = position[0]
        spr.center_y = position[1]
        return spr

    @staticmethod
    def create_animated(params):
        # retrieve parameters
        filePath = params["filePath"]
        size = None if "size" not in params else params["size"]
        filterColor = (255, 255, 255, 255) if "filterColor" not in params else params["filterColor"]
        isMaxRatio = False if "isMaxRatio" not in params else params["isMaxRatio"]
        position = (0, 0) if "position" not in params else params["position"]
        spriteBox = params["spriteBox"]
        startIndex = params["startIndex"]
        endIndex = params["endIndex"]
        frameduration = 1 / 60 if "frameDuration" not in params else params["frameDuration"]
        flipH = False if "flipH" not in params else params["flipH"]
        flipV = False if "flipv" not in params else params["flipV"]

        # get sprite box (nb sprites X, nb Y, size X size Y)
        nbX, nbY, szW, szH = spriteBox
        # Create sprite
        spr = arcade.AnimatedTimeBasedSprite()
        spr.color = filterColor
        # Read Horizontal first, then vertical
        idx = 0
        for y in range(nbY):
            for x in range(nbX):
                index = x + y * nbX
                # add index only if in range
                if index >= startIndex and index <= endIndex:
                    # load texture for sprite
                    tex = arcade.load_texture(filePath, x * szW, y * szH, szW, szH, flipped_horizontally=flipH,
                                              flipped_vertically=flipV)
                    akf = arcade.AnimationKeyframe(idx, frameduration*1000, tex)
                    idx += 1
                    spr.frames.append(akf)
        # Select first frame
        spr.texture = spr.frames[0].texture
        # set dimensions
        if size != None:
            if isMaxRatio:
                ratio = max(size[0] / spr.width, size[1] / spr.height)
            else:
                ratio = min(size[0] / spr.width, size[1] / spr.height)
            spr.scale = ratio
        # Set position
        spr.center_x = position[0]
        spr.center_y = position[1]
        # return sprite object
        return spr


# ===============================================
class Particles():
    # ===========================================

    @staticmethod
    def create_burst(params):
        # retrieve Sprite parameters
        filePath = None if "filePath" not in params else params["filePath"]
        spriteBox = None if "spriteBox" not in params else params["spriteBox"]
        spriteSelect = None if "spriteSelect" not in params else params["spriteSelect"]
        flipH = False if "flipH" not in params else params["flipH"]
        flipV = False if "flipv" not in params else params["flipV"]

        # Retrieve common emitter parameters
        position = params["position"]
        partSize = params["partSize"]
        partScale = params["partScale"]
        partSpeed = params["partSpeed"]
        color = params["filterColor"]
        startAlpha = params["startAlpha"]
        endAlpha = params["endAlpha"]

        # Retrieve specific burst parameters
        partInterval = params["partInterval"]
        totalDuration = params["totalDuration"]

        # Prepare Texture
        if filePath == None:
            tex = arcade.make_circle_texture(partSize, color)
        else:
            nbX, nbY, szW, szH = spriteBox
            x, y = spriteSelect
            tex = arcade.load_texture(filePath, x * szW, y * szH, szW, szH,
                                      flipped_horizontally=flipH,
                                      flipped_vertically=flipV)
        # create Burst
        e = arcade.Emitter(
            center_xy=position,
            emit_controller=arcade.EmitterIntervalWithTime(partInterval, totalDuration),
            particle_factory=lambda emitter: arcade.FadeParticle(
                filename_or_texture=tex,
                change_xy=arcade.rand_in_circle((0.0, 0.0), partSpeed),
                scale=partScale,
                lifetime=uniform(totalDuration / 4, totalDuration),
                start_alpha=startAlpha,
                end_alpha=endAlpha,
            ),
        )
        # return result
        return e

    @staticmethod
    def create_emitter(params):
        # retrieve Sprite parameters
        filePath = None if "filePath" not in params else params["filePath"]
        spriteBox = None if "spriteBox" not in params else params["spriteBox"]
        spriteSelect = None if "spriteSelect" not in params else params["spriteSelect"]
        flipH = False if "flipH" not in params else params["flipH"]
        flipV = False if "flipv" not in params else params["flipV"]

        # Retrieve common emitter parameters
        position = params["position"]
        partSize = params["partSize"]
        partScale = params["partScale"]
        partSpeed = params["partSpeed"]
        color = params["filterColor"]
        startAlpha = params["startAlpha"]
        endAlpha = params["endAlpha"]

        # Retrieve specific emitter parameters
        partNB = params["partNB"]
        maxLifeTime = params["maxLifeTime"]

        # Prepare Texture
        if filePath == None:
            tex = arcade.make_circle_texture(partSize, color)
        else:
            nbX, nbY, szW, szH = spriteBox
            x, y = spriteSelect
            tex = arcade.load_texture(filePath, x * szW, y * szH, szW, szH,
                                      flipped_horizontally=flipH,
                                      flipped_vertically=flipV)
        # Create emitter
        e = arcade.Emitter(
            center_xy=position,
            emit_controller=arcade.EmitMaintainCount(partNB),
            particle_factory=lambda emitter: arcade.FadeParticle(
                filename_or_texture=tex,
                change_xy=arcade.rand_in_circle((0.0, 0.0), partSpeed),
                lifetime=uniform(maxLifeTime / 10, maxLifeTime),
                scale=partScale,
                start_alpha=startAlpha,
                end_alpha=endAlpha,
            ),
        )
        return e


class Collisions():

    @staticmethod
    def circles(center1, radius1, center2, radius2):
        x1, y1 = center1
        x2, y2 = center2
        dx = x2 - x1
        dy = y2 - y1
        sr = radius1 + radius2
        return (dx * dx + dy * dy) <= (sr * sr)

    @staticmethod
    def AABBs(topLeft1, bottomRight1, topLeft2, bottomRight2):
        x1, y2 = topLeft1
        x2, y1 = bottomRight1
        x3, y4 = topLeft2
        x4, y3 = bottomRight2
        # Horizontal and vertical collisions
        hc = (x4 >= x1) and (x3 <= x2)
        vc = (y4 >= y1) and (y3 <= y2)
        return (hc and vc)

    @staticmethod
    def point_AABB(topLeft, bottomRight, pos):
        x1, y2 = topLeft
        x2, y1 = bottomRight
        x, y = pos
        return (x1 <= x <= x2) and (y1 <= y <= y2)

    @staticmethod
    def point_circle(center, radius, pos):
        return Collisions.circles(center, radius, pos, 0)

    @staticmethod
    ## Horizontal
    #    hor = __segmentProjection(center, (topLeft[0], bottomRight[1]), (topLeft[0], topLeft[1]))
    #    # Vertical
    #    ver = __segmentProjection(center, (topLeft[0], bottomRight[1]), (bottomRight[0], #bottomRight[1]))
    #    if hor or ver:
    #        return True
    #    # Ok there is no collision
    #    return False
    def __segmentProjection(center, corner1, corner2):
        Cx, Cy = center
        Ax, Ay = corner1
        Bx, By = corner2
        dACx = Cx - Ax
        dACy = Cy - Ay
        dABx = Bx - Ax
        dABy = By - Ay
        dBCx = Cx - Bx
        dBCy = Cy - By
        k1 = (dACx * dABx) + (dACy * dABy)
        k2 = (dBCx * dABx) + (dBCy * dABy)
        return k1 * k2 <= 0

    @staticmethod
    def circle_AABB(topLeft, bottomRight, center, radius):
        # first check the circle AABB collision
        if not Collisions.AABBs(topLeft, bottomRight, (center[0] - radius, center[1] + radius),
                                (center[0] + radius, center[1] - radius)):
            return False
        # Now check one of the corner is in the circle
        tl = Collisions.point_circle(center, radius, topLeft)
        br = Collisions.point_circle(center, radius, bottomRight)
        tr = Collisions.point_circle(center, radius, (bottomRight[0], topLeft[1]))
        bl = Collisions.point_circle(center, radius, (topLeft[0], bottomRight[1]))
        if tl or br or tr or bl:
            return True
        # Now check the center of the circle is in the AABB
        if Collisions.point_AABB(topLeft, bottomRight, center):
            return True
        # Check projection on the AABB
        # Horizontal
        hor = Collisions.__segmentProjection(center, (topLeft[0], bottomRight[1]), (topLeft[0], topLeft[1]))
        # Vertical
        ver = Collisions.__segmentProjection(center, (topLeft[0], bottomRight[1]), (bottomRight[0], bottomRight[1]))
        if hor or ver:
            return True
        # Ok there is no collision
        return False

    @staticmethod
    def ellipse_AABB(topLeft, bottomRight, center, radiusX, radiusY):
        x0, y1 = topLeft
        x1, y0 = bottomRight
        cx, cy = center
        # change 2d space
        x0 = (x0 - cx) / radiusX
        x1 = (x1 - cx) / radiusX
        y0 = (y0 - cy) / radiusY
        y1 = (y1 - cy) / radiusY
        return Collisions.circle_AABB((x0, y1), (x1, y0), (0, 0), 1)

    @staticmethod
    def ellipse_point_from_angle(center, radiusX, radiusY, ang):
        c = math.cos(ang)
        s = math.sin(ang)
        ta = s / c  ## tan(a)
        tt = ta * radiusX / radiusY  ## tan(t)
        d = 1. / math.sqrt(1. + tt * tt)
        x = center[0] + math.copysign(radiusX * d, c)
        y = center[1] - math.copysign(radiusY * tt * d, s)
        return x, y

    @staticmethod
    def circle_ellipse(center1, radius1, center2, radius2X, radius2Y):
        dx = center1[0] - center2[0]
        dy = center1[1] - center2[1]
        angle = math.atan2(-dy, dx)
        x, y = Collisions.ellipse_point_from_angle(center2, radius2X, radius2Y, angle)
        distance = math.hypot(x - center1[0], y - center1[1])
        distance2 = math.hypot(center2[0] - center1[0], center2[1] - center1[1])
        return distance <= radius1 or distance2 <= radius1

    @staticmethod
    def ellipses(center1, rx1, ry1, center2, rx2, ry2):
        cx1, cy1 = center1
        cx2, cy2 = center2
        # change 2d space
        rx2 /= rx1
        ry2 /= ry1
        cx2 = (cx2 - cx1) / rx1
        cy2 = (cy2 - cy1) / ry1
        return Collisions.circle_ellipse((0, 0), 1, (cx2, cy2), rx2, ry2)
