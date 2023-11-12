# напиши здесь код создания и управления картой
import pickle


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
            return self.colors[len(self.colors) - 1]

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
        self.block.setTag('at', str(position))
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

    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        return True

    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return x, y, z

    def buildBlock(self, pos):
        x, y, z = pos
        new = self.findHighestEmpty(pos)  # x-0 y-1 z-2
        if new[2] <= z + 1:
            self.addBlock(new)

    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty(position)
        pos = x, y, z-1
        for block in self.findBlocks(pos):
            block.removeNode()

    def saveMap(self):
        # сохраняет карту в бинарный файл
        # получаем все блоки:
        blocks = self.land.getChildren()
        # открываем бинарный файл для чтения (если нет - он создаётся)
        with open('my_map.dat', 'wb') as file:
            # сохраняем кол-во блоков
            pickle.dump(len(blocks), file)
            for block in blocks:
                # сохраняем коорд-ы каждого блока
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, file)

    def loadMap(self):
        # удаляет все блоки и открывает файл для чтения сохранённой карты
        self.clear()
        # открываем бинарный файл для чтения
        with open('my_map.dat', 'rb') as file:
            # получаем кол-во блоков
            length = pickle.load(file)
            for i in range(length):
                pos = pickle.load(file)
                # получаем коорд-ы блока и добавляем его
                self.addBlock(pos)

