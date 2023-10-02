# напиши здесь код создания и управления картой
class Mapmanager():
    """ Управление картой """

    def __init__(self):
        self.model = 'block'  # модель кубика лежит в файле block.egg
        # # используются следующие текстуры:
        self.texture = 'block.png'
        self.color = (0.2, 0.2, 0.35, 1)  # rgba

        # создаём основной узел карты:
        self.startNew()
        # создаём строительные блоки
        self.addBlock((0, 10, 0))

    def startNew(self):
        """создаёт основу для новой карты"""
        self.land = render.attachNewNode("Land")  # узел, к которому привязаны все блоки карты

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
