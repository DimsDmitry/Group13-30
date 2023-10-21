# напиши здесь код создания и управления картой
class Mapmanager():
    # управление картой
    def __init__(self):
        # модель кубика лежит в файле block.egg
        self.model = 'block'
        self.texture = 'block.png'
        # цвет блока (rgba-палитра)
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.2, 0.3, 1),
            (0.5, 0.5, 0.2, 1),
            (0.0, 0.6, 0.0, 1)
            ]
        # создаём основной узел карты
        self.startNew()
        # создаём строительные блоки
        # self.addBlock((0, 10, 0))

    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors)-1]

    def clear(self):
        # метод обнуляет карты
        self.land.removeNode()
        self.startNew()

    def startNew(self):
        # метод создаёт основу для новой карты
        self.land = render.attachNewNode('Land')

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def loadLand(self, filename):
        # создаёт карту земли из текстового файла, возвращает её размеры
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z) + 1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x, y
