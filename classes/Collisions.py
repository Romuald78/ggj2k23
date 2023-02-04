import arcade


class CollisionMgr():

    def __init__(self, projList, trgtList):
        self.proj = projList
        self.trgt = trgtList

    def update(self):
        for proj in self.proj:
            collidings = arcade.check_for_collision_with_list(proj, self.trgt)
            if(len(collidings)>0):
                collidings[0].userData.reduceHP(1)
