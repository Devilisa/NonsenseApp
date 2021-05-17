import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase
Config.set("graphics", "resizeable", "0")
Config.set("graphics", "height", "667")
Config.set("graphics", "width", "375")
kvlang = '''
<ScreenManagement>:
    ScreenOne:
    ScreenTwo:
    ScreenThree:
    ScreenFourth:
    ScreenFifth:
    
<ScreenOne>:
    name: 'First'
    id: screen1
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Image:
        source: 'img/Главное Меню/main.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .4}
    Button:
        background_normal: "img/Главное Меню/Настройки.png"
        background_down: "img/Главное Меню/Настройки_Нажатая.png"
        pos_hint: {'center_x': .5, 'center_y': .20}
        size_hint: 0.8, 0.1
        on_release: app.root.current = 'Second'
    Button:
        background_normal: "img/Главное Меню/Играть.png"
        background_down: "img/Главное Меню/Играть_Нажатая.png.png"
        size_hint:0.8, 0.1
        pos_hint:{'center_x': .5, 'center_y': .35}
        on_release: app.root.current = 'Third'

<ScreenTwo>:
    name: 'Second'
    id: 'screen2'
    FloatLayout:
        id: settings
        Image:
            source: 'img/Настройки/Фон/Фон.png'
            size_hint: 1, 1
            pos_hint: {'center_x': .5, 'center_y': .5}
            
        Image:
            source: 'img/Настройки/Фон/Настройки_Надпись.png'
            size_hint: .49, .49
            pos_hint: {'center_x': .5, 'center_y': .95}
        
        FloatLayout:
            id: tempo_settings
            top_hint: .5
            pos_hint: {'center_x': self.top_hint, 'center_y': .5}
            Image:
                source: 'img/Настройки/Фон/Фон_3.png'
                size_hint: 0.92, 1
                pos_hint: {'center_x': 0.5, 'center_y': .48}
            Image:
                source: 'img/Настройки/Фон/Музыка_Надпись.png'
                size_hint: 1, 1
                pos_hint: {'center_x': 0.5, 'center_y': .51}
            Image:
                source: 'img/Настройки/Фон/Общее_Надпись.png'
                size_hint: 0.3, 0.3
                pos_hint: {'center_x': 0.5, 'center_y': .66}
            Image:
                source: 'img/Настройки/Фон/Картинка_Звук.png'
                size_hint: 0.3, 0.3
                pos_hint: {'center_x': 0.15, 'center_y': .585}
            Image:
                source: 'img/Настройки/Фон/Картинка_Звук.png'
                size_hint: 0.3, 0.3
                pos_hint: {'center_x': 0.15, 'center_y': .435}
            Slider:
                size_hint: 0.7, 0.02
                background_horizontal: 'img/Настройки/Дорожка_Звук.png'
                cursor_image: 'img/Настройки/Трекер_Звук.png'
                cursor_size: 15, 15
                pos_hint: {'center_x': 0.55, 'center_y': .435}
                id: slider
                min: 20
                max: 100
                step: 1
            Slider:
                size_hint: 0.7, 0.02
                background_horizontal: 'img/Настройки/Дорожка_Звук.png'
                cursor_image: 'img/Настройки/Трекер_Звук.png'
                cursor_size: 15, 15
                pos_hint: {'center_x': 0.55, 'center_y': .585}
                id: slider
                min: 20
                max: 100
                step: 1
            Image:
                source: 'img/Настройки/Фон/Вибрация_Надпись.png'
                size_hint: 0.5, 0.5
                pos_hint: {'center_x': 0.5, 'center_y': .36}
            Image:
                source: 'img/Настройки/Фон/Фон_3.png'
                size_hint: 0.92, 1
                pos_hint: {'center_x': 1.6, 'center_y': .48}
            Image:
                source: 'img/Настройки/Фон/Фон_3.png'
                size_hint: 0.92, 1
                pos_hint: {'center_x': 2.7, 'center_y': .48}
            Button:
                id: button_swiper
                background_normal: 'img/Настройки/Фон_Переключатель.png'
                background_down: 'img/Настройки/Фон_Переключатель.png'
                size_hint: 0.3, 0.06
                pos_hint: {'center_x': .5, 'center_y': .285}
                on_release: root.AnimButton1(button_swipe1)
            Image:
                id: button_swipe1
                source: 'img/Настройки/Переключатель.png'
                size_hint: 0.2, 0.2
                top_hint: 0.065
                pos_hint: {'center_x': 0.5 - self.top_hint, 'center_y': .285}
            Button:
                id: button_swiper
                background_normal: 'img/Настройки/Фон_Переключатель.png'
                background_down: 'img/Настройки/Фон_Переключатель.png'
                size_hint: 0.3, 0.06
                pos_hint: {'center_x': 1.6, 'center_y': .52}
                on_release: root.AnimButton2(button_swipe2)
            Image:
                id: button_swipe2
                source: 'img/Настройки/Переключатель.png'
                size_hint: 0.2, 0.2
                top_hint: 0.065
                pos_hint: {'center_x': 1.6 - self.top_hint, 'center_y': .52}
            Button:
                id: button_swiper
                background_normal: 'img/Настройки/Фон_Переключатель.png'
                background_down: 'img/Настройки/Фон_Переключатель.png'
                size_hint: 0.3, 0.06
                pos_hint: {'center_x': 1.6, 'center_y': .32}
                on_release: root.AnimButton3(button_swipe3)
            Image:
                id: button_swipe3
                source: 'img/Настройки/Переключатель.png'
                size_hint: 0.2, 0.2
                top_hint: 0.065
                pos_hint: {'center_x': 1.6 - self.top_hint, 'center_y': .32}
            Image:
                source: 'img/Настройки/Фон/Анимации_Надпись.png'
                size_hint: 0.5, 0.5
                pos_hint: {'center_x': 1.6, 'center_y': .62}
            Image:
                source: 'img/Настройки/Фон/Цвет Темы_Надпись.png'
                size_hint: 0.5, 0.5
                pos_hint: {'center_x': 1.6, 'center_y': .42}

                
        Button:
            id: back_button:
            background_normal: 'img/Настройки/назад.png'
            background_down: 'img/Настройки/назад.png'
            size_hint: .8, .1
            pos_hint: {'center_x': 0.5, 'center_y': .09}
            on_release: app.root.current = 'First'
            on_release: root.AnimMenuSoundButton(tempo_settings)
            
        Button:
            id: sound_button
            background_normal: 'img/Настройки/Звук_Активная.png'
            background_down: 'img/Настройки/Звук_Активная.png'
            size_hint: 0.27, 0.051
            pos_hint: {'center_x': .18, 'center_y': .86}
            on_release: root.AnimMenuSoundButton(tempo_settings)
        Button:
            id: graphic_button
            background_normal: 'img/Настройки/Графика_Не_Активная.png'
            background_down: 'img/Настройки/Графика_Активная.png'
            size_hint: 0.27, 0.051
            pos_hint: {'center_x': .5, 'center_y': .86}
            on_release: root.AnimMenuGraphicButton(tempo_settings)
        Button:
            id: smth_button
            background_normal: 'img/Настройки/Прочее_Не_Активная.png'
            background_down: 'img/Настройки/Прочее_Активная.png'
            size_hint: 0.27, 0.051
            pos_hint: {'center_x': .82, 'center_y': .86}
            on_release: root.AnimMenuSmthButton(tempo_settings)

            

<ScreenThree>:
    name: 'Third'
    id: screen3
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}    
    Image:
        source: 'img/Режимы/Выберете_Режим.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .48, 'center_y': .56}
    FloatLayout:
        id: screen3pages
        top_hint: .5
        pos_hint: {'center_x': self.top_hint, 'center_y': .5}
        Button:
            background_normal: 'img/Режимы/Стрелочка_Влево.png'
            background_down: "img/Режимы/Стрелочка_Влево.png"
            size_hint: .02, .06
            pos_hint: {'center_x': 1.62, 'center_y': .5}
            on_release: root.AnimScreen3Left(screen3pages)
        Button:
            background_normal: 'img/Режимы/Стрелочка_Вправо.png'
            background_down: "img/Режимы/Стрелочка_Вправо.png"
            size_hint: .03, .06
            pos_hint: {'center_x': .98, 'center_y': .5}
            on_release: root.AnimScreen3Right(screen3pages)
        Button:
            background_normal: 'img/Настройки/Фон/Фон_3.png'
            background_down: "img/Настройки/Фон/Фон_3.png"
            size_hint: .92, .6
            pos_hint: {'center_x': .5, 'center_y': .54}
            on_release: app.root.current = 'Fourth'
        Button:
            background_normal: 'img/Настройки/Фон/Фон_3.png'
            background_down: "img/Настройки/Фон/Фон_3.png"
            size_hint: .92, .6
            pos_hint: {'center_x': 2.1, 'center_y': .54}
            on_release: app.root.current = 'Fifth'
        Label:
            text:'Истории'
            font_size: 35
            font_name:'Ubuntu'
            pos_hint: {'center_x': 2.1, 'center_y': .8}
        Label:
            text:'Классический Режим'
            font_size: 35
            font_name:'Ubuntu'
            pos_hint: {'center_x': .5, 'center_y': .8}
    
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.8, 0.1
        left_hint: .5
        pos_hint:{'center_x': self.left_hint, 'center_y': .1}
        on_release: app.root.current = 'First'
    Button:
        background_normal: "img/Главное Меню/Настройки_Картинка.png"
        background_down: "img/Главное Меню/Настройки_Картинка.png"
        pos_hint: {'center_x': .92, 'center_y': .95}
        size_hint: 0.2, 0.1125
        on_release: app.root.current = 'Second'
    

<ScreenFourth>:
    name: 'Fourth'
    id: screen4
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}   
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.8, 0.1
        left_hint: .5
        pos_hint:{'center_x': self.left_hint, 'center_y': .1}
        on_release: app.root.current = 'Third'

<ScreenFifth>:
    name: 'Fifth'
    id: screen5
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}   
    TextInput:
        background_normal: "img/Режимы/Истории/Фон.png"
        background_active: "img/Режимы/Истории/Фон.png"
        size_hint:0.8, 0.3
        pos_hint:{'center_x': .5, 'center_y': .5}
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.8, 0.1
        left_hint: .5
        pos_hint:{'center_x': self.left_hint, 'center_y': .1}
        on_release: app.root.current = 'Third'
            
'''
LabelBase.register(name='Ubuntu', fn_regular='font/UbuntuCondensed-Regular.ttf')

class ScreenManagement(ScreenManager):
    pass


class ScreenOne(Screen):
    def switch(self):
        # here you can insert any python logic you like
        self.parent.current = 'Second'
        self.parent.current = 'Third'


class ScreenTwo(Screen):
    pass

    def AnimButton1(self, widget, *args):
        if self.ids.button_swipe1.top_hint > 0:
            anim = Animation(top_hint=-0.065, duration=0.3)
            anim.start(widget)
        else:
            anim = Animation(top_hint=0.065, duration=0.3)
            anim.start(widget)

    def AnimButton2(self, widget, *args):
        if self.ids.button_swipe2.top_hint > 0:
            anim = Animation(top_hint=-0.065, duration=0.3)
            anim.start(widget)
        else:
            anim = Animation(top_hint=0.065, duration=0.3)
            anim.start(widget)

    def AnimButton3(self, widget, *args):
        if self.ids.button_swipe3.top_hint > 0:
            anim = Animation(top_hint=-0.065, duration=0.3)
            anim.start(widget)
        else:
            anim = Animation(top_hint=0.065, duration=0.3)
            anim.start(widget)

    def AnimMenuSoundButton(self, widget, *args):
        anim = Animation(top_hint=.5, duration=0.3)
        self.ids.graphic_button.background_normal = 'img/Настройки/Графика_Не_Активная.png'
        self.ids.sound_button.background_normal = 'img/Настройки/Звук_Активная.png'
        self.ids.smth_button.background_normal = 'img/Настройки/Прочее_Не_Активная.png'
        anim.start(widget)

    def AnimMenuGraphicButton(self, widget, *args):
        anim = Animation(top_hint=-0.6, duration=0.3)
        self.ids.graphic_button.background_normal = 'img/Настройки/Графика_Активная.png'
        self.ids.sound_button.background_normal = 'img/Настройки/Звук_Не_Активная.png'
        self.ids.smth_button.background_normal = 'img/Настройки/Прочее_Не_Активная.png'
        anim.start(widget)

    def AnimMenuSmthButton(self, widget, *args):
        anim = Animation(top_hint=-1.7, duration=0.3)
        self.ids.graphic_button.background_normal = 'img/Настройки/Графика_Не_Активная.png'
        self.ids.sound_button.background_normal = 'img/Настройки/Звук_Не_Активная.png'
        self.ids.smth_button.background_normal = 'img/Настройки/Прочее_Активная.png'
        anim.start(widget)



class ScreenThree(Screen):
    def AnimScreen3Right(self, widget, *args):
        anim = Animation(top_hint=-1.1, duration=0.3)
        anim.start(widget)

    def AnimScreen3Left(self, widget, *args):
        anim = Animation(top_hint=.5, duration=0.3)
        anim.start(widget)




class ScreenFourth(Screen):
    pass

class ScreenFifth(Screen):
    pass


class MyApp(App):
    def build(self):
        Builder.load_string(kvlang)
        return ScreenManagement()


if __name__ == '__main__':
    MyApp().run()
