# Класс Hero представляет героя в игре.
# Он имеет различные методы для управления героем, включая перемещение, поворот, изменение режима и т. д.
# Герой также может строить и разрушать блоки в игровом мире.
# Класс Hero также обрабатывает события клавиатуры для управления героем и камерой.
"""
Код из файла hero.py:

Определение некоторых ключей управления для героя в игре.

"""

key_switch_camera = "x"
key_switch_mode = "z"
key_forward = "w"
key_back = "s"
key_left = "a"
key_right = "d"
key_up = "space"
key_down = "c"
key_turn_left = "l"
key_turn_right = "k"


class Hero:
    def __init__(self, pos, land):
        # Инициализация свойств героя
        self.land = land
        self.mode = True
        self.hero = loader  # Загрузка модели героя
        self.hero.setColor(1, 0.5, 0)  # Установка цвета героя
        self.hero.setScale(0.3)  # Установка масштаба героя
        self.hero.setPos(pos)  # Установка позиции героя
        self.hero.reparentTo(render)  # Размещение героя на сцене
        self.cameraBind()  # Привязка камеры
        self.accept_events()  # Регистрация обработчиков событий

    def cameraBind(self):
        # Привязка камеры к герою
        base.disableMouse()  # Отключение мыши
        base.camera.setH(180)  # Установка горизонтального угла обзора камеры
        base.camera.reparentTo(self.hero)  # Привязка камеры к герою
        base.camera.setPos(0, 0, 1.5)  # Установка позиции камеры
        self.cameraOn = True  # Флаг активации камеры

    def cameraUp(self):
        # Отвязка камеры от героя
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        # Изменение вида камеры
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        # Поворот героя влево
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        # Поворот героя вправо
        self.hero.setH((self.hero.getH() - 5) % 360)

    def changeMode(self):
        # Изменение режима героя
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def look_at(self, angle):
        # Определение координат точки, на которую смотрит герой
        x_form = round(self.hero.getX())
        y_form = round(self.hero.getY())
        z_form = round(self.hero.getZ())
        dx, dy = self.hero.check_dir(self, angle)
        x_to = x_form + dx
        y_to = y_form + dy
        return y_to, x_to, z_form

    def just_move(self, angle):
        # Перемещение героя на указанный угол
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        # Перемещение героя в указанном направлении
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def try_move(self, angle):
        # Попытка перемещения героя в указанном направлении
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)

    def check_dir(self, angle):
        # Проверка направления движения героя
        if 0 <= angle <= 20:
            return 0, -1
        elif angle <= 65:
            return 1, -1
        elif angle <= 110:
            return 1, 0
        elif angle <= 155:
            return 1, 1
        elif angle <= 200:
            return 0, 1
        elif angle <= 245:
            return -1, 1
        elif angle <= 290:
            return -1, 0
        elif angle <= 335:
            return -1, -1
        else:
            return 0, -1

    def up(self):
        # Перемещение героя вверх
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        # Перемещение героя вниз
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def forward(self):
        # Перемещение героя вперед
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        # Перемещение героя назад
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        # Перемещение героя влево
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        # Перемещение героя вправо
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def build(self):
        # Построение блока
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)



#    def delBlockFrom(self):
#       x, y, z =
#        pos = x, y, z - 1
#        blocks = self.findBlocks(pos)
#        for block in blocks:
#           block.removeNode()

#    def delBlock(self, position):
#        blocks =

    def destroy(self):
        # Разрушение блока
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def accept_events(self):
        # Регистрация обработчиков событий
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + '-repeat', self.turn_right)

        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)

        base.accept(key_back, self.back)
        base.accept(key_back + '-repeat', self.back)

        base.accept(key_left, self.left)
        base.accept(key_left + '-repeat', self.left)

        base.accept(key_right, self.right)
        base.accept(key_right + '-repeat', self.right)

        base.accept(key_up + '-repeat', self.up)
        base.accept(key_up, self.up)

        base.accept(key_down + '-repeat', self.up)
        base.accept(key_down, self.down)

        base.accept('b', self.build)
        base.accept('v', self.destroy)

        base.accept(key_switch_camera, self.changeView)
