# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase


# класс
class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        # загружаем модель
        self.model = loader.loadModel('models/environment')
        # перемещение модели в рендер, смена родителя
        self.model.reparentTo(render)
        # попробуйте поменять размер модели
        self.model.setScale(0.1)
        # попробуйте переместить модель по всем осям
        self.model.setPos(-2, 25, -3)


game = Game()
game.run()
