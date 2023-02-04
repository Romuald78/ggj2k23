import arcade


class CollisionMgr():

    def __init__(self, projList, trgtList):
        self.proj = projList
        self.trgt = trgtList

    def update(self):
        for proj in self.proj:
            B = proj.userData
            collidings = arcade.check_for_collision_with_list(proj, self.trgt)
            if(len(collidings)>0):
                try:
                    A = collidings[0].userData
                    A.reduceHP(B.getDMG())
                    B.reduceHP(A.getDMG())

                except Exception as ex:
                    print(ex)
