import arcade


class CollisionMgr():

    def __init__(self, projMgr, trgtList):
        self.proj = projMgr.projs
        self.trgt = trgtList

    def process(self):
        for proj in self.proj:
            colliding = arcade.check_for_collision_with_list(proj, self.trgt)
            