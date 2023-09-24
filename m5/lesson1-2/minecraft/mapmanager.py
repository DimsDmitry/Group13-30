# напиши здесь код создания и управления картой
class Mapmanager():
    #управление картой
    def __init__(self):
        #модель кубика лежит в файле block.egg
        self.model = 'block'
        self.texture = 'block.png'
        #цвет блока (rgba-палитра)
        self.color = (0.2, 0.2, 0.35, 1)
        #создаём основной узел карты
        self.startNew()
        #создаём строительные блоки
        self.addBlock((0, 10, 0))


    def startNew(self):
    #метод создаёт основу для новой карты
        self.land = render.attachNewMode('Land')


    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
