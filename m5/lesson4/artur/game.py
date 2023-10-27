from panda3d.core import loadPrcFileData
from direct.showbase.ShowBase import ShowBase
from MapManger import MapManager

# Set the window title
loadPrcFileData("", "window-title My Game")

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapManager()  # Create an instance of MapManager
        self.land.loadLand("land.txt")
        base.camLens.setFov(90)


game = Game()
game.run()
