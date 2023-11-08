from panda3d.core import loadPrcFileData
from direct.showbase.ShowBase import ShowBase
from MapManger import MapManager
from hero import Hero

# Set the window title
loadPrcFileData("", "window-title My Game")

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapManager()  # Create an instance of MapManager
        x, y = self.land.loadLand("land.txt")
        self.hero = Hero((x // 2, y // 2, 2), self.land)
        base.camLens.setFov(90)


game = Game()
game.run()
