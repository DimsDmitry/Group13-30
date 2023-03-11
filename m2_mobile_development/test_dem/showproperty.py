# в программе описан класс MyInput - это TextInput, который хранит 
# свойство mytext. При изменении текста это свойство тоже меняется
# (это перевернутый текст, но снаружи виджета мы не обязаны знать алгоритм).
# Далее создаётся интерфейс, в котором обрабатывается изменение свойства mytext:
# каждый раз при изменении это свойство отображается на label
# см. строки 15, 21, 28, 33

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

class MyInput(TextInput):
    mytext = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(text=self.changevalue)
    
    def changevalue(self, widget, value):
        self.mytext = "".join(reversed(self.text))

class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)
        self.txt_in = MyInput(size_hint_y=None, height="30sp")
        self.label = Label()
        self.txt_in.bind(mytext=self.textchanged)
        self.add_widget(self.txt_in)
        self.add_widget(self.label)

    def textchanged(self, widget, value):
        self.label.text = "Что? " + value + " ?"

class MyApp(App):
    def build(self):
        box = MyBox()
        return box


app = MyApp()
app.run()