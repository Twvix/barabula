
# программа с двумя экранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image
from prognoz import get_weather, get_weather_zavtra
from datetime import datetime
dt = datetime.now().date()

# Экран (объект класса Screen) - это виджет типа "макет" (Screen - наследник класса RelativeLayout).
# ScreenManager - это особый виджет, который делает видимым один из прописанных в нём экранов.
Window.clearcolor = (0.9, 0.9, 0.9, 1)
Window.size = (1000, 700)

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        lbl = Label(text='Выберите город', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, color=(0,0,0,1))
        # inpt = TextInput(size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        img = Image(source='oblako.png', size_hint=(0.65, 0.65), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        img2 = Image(source='solnce.png', size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.Vyborg = Button(text="Выборг", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.Saint_Peterburg = Button(text="Санкт-Петербург", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        self.Moscow = Button(text="Москва", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.add_widget(self.Vyborg) # экран - это виджет, на котором могут создаваться все другие (потомки)
        self.add_widget(self.Saint_Peterburg)
        self.add_widget(self.Moscow)
        self.add_widget(img2)
        self.add_widget(img)
        self.add_widget(lbl)
        self.Vyborg.on_press = self.vbg
        self.Saint_Peterburg.on_press = self.spb
        self.Moscow.on_press = self.msc


    def vbg(self):
        # self.manager.transition.direction = 'left'
        self.manager.current = 'second'
    def spb(self):
        # self.manager.transition.direction = 'left'
        self.manager.current = 'spb'
    def msc(self):
    #     self.manager.transition.direction = 'left'
        self.manager.current = 'msc'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        lbl = Label(text='Выборг', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, color=(0,0,0,1))
        lbl2 = Label(text=get_weather('Погода_в_Выборге'), size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.3}, color=(0,0,0,1))
        lbl3 = Label(text=get_weather_zavtra('Погода_в_Выборге'), size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.25}, color=(0,0,0,1))
        img = Image(source='oblako.png', size_hint=(0.65, 0.65), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        img2 = Image(source='solnce.png', size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        with open('history.txt', 'a+', encoding='utf-8') as file:
            print(file.readline())
            if str(dt) in file.readline():
                print('qwe')
                pass
            else:
                file.write(str(dt) + '\n\n')
                file.write('Выборг' + ': ' + lbl2.text + '\n\n')
        file.close()
        btn = Button(text="Назад", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        btn.on_press = self.next
        self.add_widget(img2)
        self.add_widget(img)
        self.add_widget(btn)
        self.add_widget(lbl)
        self.add_widget(lbl2)
        self.add_widget(lbl3)


        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'



class mscScr(Screen):
    def __init__(self, name='msc'):
        super().__init__(name=name)
        lbl = Label(text='Москва', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, color=(0,0,0,1))
        lbl2 = Label(text=get_weather('Погода_в_Москве_(ВДНХ)'), size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.3}, color=(0,0,0,1))
        img = Image(source='oblako.png', size_hint=(0.65, 0.65), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        img2 = Image(source='solnce.png', size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        lbl3 = Label(text=get_weather_zavtra('Погода_в_Москве_(ВДНХ)'), size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.25}, color=(0,0,0,1))
        with open('history.txt', 'a', encoding='utf-8') as file:
            file.write('Москва' + ': ' + lbl2.text + '\n\n')
        file.close()
        btn = Button(text="Назад", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        btn.on_press = self.next
        self.add_widget(img2)
        self.add_widget(img)
        self.add_widget(btn)
        self.add_widget(lbl)
        self.add_widget(lbl2)
        self.add_widget(lbl3)

        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'



class spbScr(Screen):
    def __init__(self, name='spb'):
        super().__init__(name=name)
        lbl = Label(text='Санкт-Петербург', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, color=(0,0,0,1))
        lbl2 = Label(text=get_weather('Погода_в_Санкт-Петербурге'), size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.3}, color=(0,0,0,1))
        img = Image(source='oblako.png', size_hint=(0.65, 0.65), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        img2 = Image(source='solnce.png', size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        btn = Button(text="Назад", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        lbl3 = Label(text=get_weather_zavtra('Погода_в_Санкт-Петербурге'), size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.25}, color=(0,0,0,1))
        with open('history.txt', 'a', encoding='utf-8') as file:
            file.write('Санкт-Петербург' + ': ' + lbl2.text + '\n\n')
        file.close()
        btn.on_press = self.next
        self.add_widget(img2)
        self.add_widget(img)
        self.add_widget(btn)
        self.add_widget(lbl)
        self.add_widget(lbl2)
        self.add_widget(lbl3)
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(mscScr())
        sm.add_widget(spbScr())

        return sm

app = MyApp()
app.run()
