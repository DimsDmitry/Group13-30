from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):
  def __init__(self):
      ShowBase.__init__(self)
      self.model = self.loader.loadModel('models/environment')
      self.model.reparentTo(self.render)
game = Game()
game.run()
