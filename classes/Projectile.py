from classes.IDamage import IDamage


class Projectile(IDamage):


    def __init__(self, hp=1, dmg=1):
        super().__init__(hp, dmg)

    def triggerHitEffect(self):
        pass
