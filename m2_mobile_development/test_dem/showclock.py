# программа с тремя экранами, переключение на третий экран происходит по таймеру
# таймер включается в методе on_enter второго экрана, т.е. сразу после того, как пользователь зашёл на этот экран
# см. строку 58
 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

time_to_read = 5
long_txt = """Используйте эти советы, чтобы увеличить скорость чтения:\n
1. Не проговаривайте читаемый текст.\n
Если привычка проговаривать уже есть, тренируйтесь читать и одновременно пропевайте с закрытыми губами одну ноту.\n 
2. Учитесь схватывать взглядом сразу несколько слов.\n
Тренируйтесь, бросая взгляд на текст. Не перемещая взгляда, закройте глаза и восстановите в памяти, что успели прочитать.\n 
3. Добейтесь движения взгляда сверху вниз.\n
Не возвращайте взгляд на уже прочитанное. Тренируйтесь, читая узкие колонки текста.\n
Можно помогать себе, двигая по тексту лист бумаги, чтобы он закрывал верхнюю часть страницы. Ускоряйте движение листа.\n
4. Концентрируйте внимание на чтении.\n
Читайте длинные тексты. Уберите отвлекающие факторы. Ищите книги, которые вас захватят. """

# класс для аккуратного отображения длинного текста на маленьком экране с прокруткой
# подробнее ты можешь прочитать в документации к первому уроку
class ScrollLabel(ScrollView):
    def __init__(self, ltext, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text=ltext, markup=True, size_hint_y=None, font_size='20sp', halign='left', valign='top')
        self.label.bind(size=self.resize)
        self.add_widget(self.label)

    def resize(self, *argv):
        self.label.text_size = (self.label.width, None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", padding=10)
        box.add_widget(Label(text="Попробуйте прочитать текст за " + str(time_to_read) + " секунд(ы)"))
        btn_next = Button(text="Начать", on_press=self.next)
        box.add_widget(btn_next)
        self.add_widget(box) 

    def next(self, *args):
        self.manager.transition.direction = 'up'
        self.manager.current = 'showtext' 

class ShowText(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(padding=10)
        box.add_widget(ScrollLabel(long_txt, size_hint_x=0.8, pos_hint={'center_x':0.5})) 
        self.add_widget(box)
    
    def on_enter(self):
        Clock.schedule_once(self.next, time_to_read)

    def next(self, dt):
        print("Прошло", dt, "секунд")
        self.manager.current = 'last' 

class LastScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Время!")) 

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr(name='1'))
        sm.add_widget(ShowText(name='showtext'))
        sm.add_widget(LastScr(name='last'))
        return sm

app = MyApp()
app.run()