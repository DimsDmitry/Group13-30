# программа с двумя экранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class ScrButton(Button):
    def __init__(self, screen: object, direction: object = "right", goal: object = "main", **kwargs: object):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self. screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", padding=8, spacing=8)
        hl = BoxLayout()
        txt = Label(text="Выбери экран.")
        vl.add_widget(ScrButton(self, direction="down", goal="first", text="1"))
        vl.add_widget(ScrButton(self, direction="left", goal="second", text="2"))
        vl.add_widget(ScrButton(self, direction="right", goal="third", text="3"))
        vl.add_widget(ScrButton(self, direction="up", goal="fourth", text="4"))
        hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn = Button(text="Выбор: 1", size_hint=(0.5, 1), pos_hint={"left": 0})
        btn_back = ScrButton(self, direction="up", goal="main", text="Назад", size_hint=(0.5, 1), pos_hint={"right": 1})
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)

class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn = Button(text="Выбор: 1", size_hint=(0.5, 1), pos_hint={"left": 0})
        btn_back = ScrButton(self, direction="down", goal="main", text="Назад", size_hint=(0.5, 1), pos_hint={"right": 1})
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical")
        self.text = Label(text="Выбор 2:")
        vl.add_widget(self.text)

        hl_0 = BoxLayout(size_hint=(0.8, None), height="30sp")
        lbl1 = Label(text="Введите проль:", halign="right")
        self.input = TextInput(multiline=False)

        hl_0.add_widget(lbl1)
        hl_0.add_widget(self.input)
        vl.add_widget(hl_0)

        hl = BoxLayout(size_hint=(0.6, 0.3), pos_hint={"center_x": 0.5})
        btn_false = Button(text="OK!")
        btn_back = ScrButton(self, direction="right", goal="main", text="Назад")

        hl.add_widget(btn_false)
        hl.add_widget(btn_back)
        vl.add_widget(hl)
        self.add_widget(vl)
    def change_text(self):
        self.txt.text = self.input.text + '? Не сработало ...'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(FourthScreen(name="fourth"))
        sm.add_widget(SecondScreen(name="second"))
        return sm

MyApp().run()