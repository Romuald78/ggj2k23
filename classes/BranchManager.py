from arcade import SpriteList


class BranchManager():

    def __init__(self):
        self.roots = SpriteList(use_spatial_hash=True)

    def update(self, deltaTime):
        pass

    def draw(self):
        self.roots.draw()

    def addRoot(self, root):
        self.roots.append(root.sprite)

    def removeRoot(self, root):
        self.roots.remove(root.sprite)

