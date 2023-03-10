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
                    if(A.hp>0 and B.hp>0):
                        A.reduceHP(B.getDMG())
                        B.reduceHP(A.getDMG())
                        A.triggerHitEffect()
                        B.triggerHitEffect()

                except Exception as ex:
                    print(ex)
