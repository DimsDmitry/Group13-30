# напиши модуль для работы с анимацией
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import NumericProperty, BooleanProperty

from kivy.uix.boxlayout import BoxLayout


class Runner(BoxLayout):
    finished = BooleanProperty(False) #все ли сделаны перемещения
    value = NumericProperty(0) #сколько сделано перемещений

    def __init__(self):
        pass

    def start(self):
        pass

    def next(self, widget, step):
        pass