key_switch_camera = 'c'  # камера привязана к герою или нет
key_switch_mode = 'z'  # можно проходить сквозь препятствия или нет

key_forward = 'w'  # шаг вперёд
key_back = 's'  # шаг назад
key_left = 'a'  # шаг влево
key_right = 'd'  # шаг вправо
key_up = 'e'  # шаг вверх
key_down = 'q'  # шаг вниз

key_turn_left = 'n'  # поворот камеры направо
key_turn_right = 'm'  # поворот камеры налево


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.mode = True  # режим прохождения сквозь блоки
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
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        self.hero.setH((set.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((set.hero.getH() - 5) % 360)

    def look_at(self, angle):
        # возвращает координаты в которые двинулся персонаж, если он делает шаг
        # в направлении angle
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())
        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
            
