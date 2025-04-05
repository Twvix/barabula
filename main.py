from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from prognoz import get_weather

Window.clearcolor = (0.9, 0.9, 0.9, 1)
Window.size = (500, 600)

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        self.lbl = Label(text='Введите город', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.inpt = TextInput(multiline=False, size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn = Button(text="Прогноз", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn.on_press = self.next
        self.add_widget(btn)
        self.add_widget(self.lbl)
        self.add_widget(self.inpt)
    
    def next(self):
        # Получаем данные о погоде и сохраняем в приложении
        app = App.get_running_app()
        app.weather_data = get_weather(self.inpt.text)
        
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        self.btn = Button(text="Вернуться назад")
        self.btn.on_press = self.next
        self.weather_label = Label(text="", size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(self.weather_label)
        self.add_widget(self.btn)
    
    def on_enter(self):
        # Этот метод вызывается при переходе на экран
        # Получаем данные о погоде из приложения
        app = App.get_running_app()
        weather_data = getattr(app, 'weather_data', None)
        if weather_data:
            self.weather_label.text = f"Погода: {weather_data}"
        else:
            self.weather_label.text = "Данные о погоде недоступны"
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        self.weather_data = None  # Здесь будем хранить данные о погоде
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        return sm

app = MyApp()
app.run()
