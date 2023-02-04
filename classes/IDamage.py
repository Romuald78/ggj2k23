
class IDamage():

    def __init__(self, hp=1, dmg=1):
        self.hp = hp
        self.dmg = dmg

    def getDMG(self):
        return self.dmg

    def reduceHP(self, dmg):
        self.hp -= max(0, dmg)

