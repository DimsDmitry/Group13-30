key_switch_camera = 'c'  # камера привязана к герою или нет
key_switch_mode = 'z'  # смена игрового режима

key_forward = 'w'  # шаг вперёд
key_back = 's'  # шаг назад
key_left = 'a'  # шаг влево
key_right = 'd'  # шаг вправо
key_up = 'e'  # шаг вверх
key_down = 'q'  # шаг вниз

key_turn_left = 'n'  # поворот камеры направо
key_turn_right = 'm'  # поворот камеры налево

key_build = 'b'  # построить блок перед собой
key_destroy = 'v'  # разрушить блок перед собой

key_savemap = 'k'  # сохранить карту
key_loadmap = 'l'  # загрузить карту


def check_dir(angle):
    ''' возвращает округленные изменения координат X, Y,
    соответствующие перемещению в сторону угла angle.
    Координата Y уменьшается, если персонаж смотрит на угол 0,
    и увеличивается, если смотрит на угол 180.
    Координата X увеличивается, если персонаж смотрит на угол 90,
    Координата X увеличивается, если персонаж смотрит на угол 90,
    и уменьшается, если смотрит на угол 270.
        угол 0 (от 0 до 20)      ->        Y - 1
        угол 45 (от 25 до 65)    -> X + 1, Y - 1
        угол 90 (от 70 до 110)   -> X + 1
        от 115 до 155            -> X + 1, Y + 1
        от 160 до 200            ->        Y + 1
        от 205 до 245            -> X - 1, Y + 1
        от 250 до 290            -> X - 1
        от 290 до 335            -> X - 1, Y - 1
        от 340                   ->        Y - 1  '''
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


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.mode = True  # режим прохождения сквозь блоки (наблюдателя)
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def look_at(self, angle):
        # возвращает координаты в которые двинулся персонаж, если он делает шаг
        # в направлении angle
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())
        dx, dy = check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def try_move(self, angle):
        # перемещение в основном режиме
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            # если isEmpty == True, перед нами нет блока. Надо упасть вниз
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            # перед нами занято. Если получится, заберёмся на этот блок
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
                # если не получится забраться - стоим на месте

    def just_move(self, angle):
        # перемещается в любом случае
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def accept_events(self):
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

        base.accept(key_up, self.up)
        base.accept(key_up + '-repeat', self.up)
        base.accept(key_down, self.down)
        base.accept(key_down + '-repeat', self.down)

        base.accept(key_switch_camera, self.changeView)
        base.accept(key_switch_mode, self.changeMode)

        base.accept(key_build, self.build)
        base.accept(key_destroy, self.destroy)

        base.accept(key_savemap, self.land.saveMap)
        base.accept(key_loadmap, self.land.loadMap)
