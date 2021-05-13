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

Config.set("graphics", "resizeable", "0")
Config.set("graphics", "height", "667")
Config.set("graphics", "width", "375")
kvlang = '''
<ScreenManagement>:
    ScreenOne:
    ScreenTwo:
    ScreenThree:
    
<ScreenOne>:
    name: 'First'
    id: screen1
    Image:
        source: 'img/main.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Button:
        background_normal: "img/настройки.png"
        background_down: "img/настройки_н.png"
        pos_hint: {'center_x': .5, 'center_y': .3}
        size_hint: 0.8, 0.1
        on_release: app.root.current = 'Second'
    Button:
        background_normal: "img/прочее.png"
        background_down: "img/прочее_н.png"
        size_hint:0.8, 0.1
        pos_hint:{'center_x': .5, 'center_y': .15}
    Button:
        background_normal: "img/играть.png"
        background_down: "img/играть_н.png"
        size_hint:0.8, 0.1
        pos_hint:{'center_x': .5, 'center_y': .45}
        on_release: app.root.current = 'Third'

<ScreenTwo>:
    name: 'Second'
    id: 'screen2'
    FloatLayout:
        id: settings
        Image:
            source: 'img/фон.png'
            size_hint: 1, 1
            pos_hint: {'center_x': .5, 'center_y': .5}
            
        Image:
            source: 'img/НАСТРОЙКИ_11.png'
            size_hint: 1, 1
            pos_hint: {'center_x': .5, 'center_y': .95}
        
        FloatLayout:
            id: tempo_settings
            top_hint: .5
            pos_hint: {'center_x': self.top_hint, 'center_y': .5}
            Image:
                source: 'img/фон 2.png'
                size_hint: 0.92, 1
                pos_hint: {'center_x': 0.5, 'center_y': .42}
            Image:
                source: 'img/Настройки/МУЗЫКА.png'
                size_hint: 1, 1
                pos_hint: {'center_x': 0.5, 'center_y': .45}
            Image:
                source: 'img/Настройки/ОБЩЕЕ.png'
                size_hint: 0.3, 0.3
                pos_hint: {'center_x': 0.5, 'center_y': .6}
            Image:
                source: 'img/Настройки/Group.png'
                size_hint: 0.3, 0.3
                pos_hint: {'center_x': 0.15, 'center_y': .525}
            Image:
                source: 'img/Настройки/Group.png'
                size_hint: 0.3, 0.3
                pos_hint: {'center_x': 0.15, 'center_y': .375}
            Slider:
                size_hint: 0.7, 0.02
                background_horizontal: 'img/Настройки/Group 39.png'
                cursor_image: 'img/Настройки/Ellipse 2.png'
                cursor_size: 15, 15
                pos_hint: {'center_x': 0.55, 'center_y': .375}
                id: slider
                min: 20
                max: 100
                step: 1
            Slider:
                size_hint: 0.7, 0.02
                background_horizontal: 'img/Настройки/Group 39.png'
                cursor_image: 'img/Настройки/Ellipse 2.png'
                cursor_size: 15, 15
                pos_hint: {'center_x': 0.55, 'center_y': .525}
                id: slider
                min: 20
                max: 100
                step: 1
            Image:
                source: 'img/Настройки/ВИБРАЦИЯ.png'
                size_hint: 0.5, 0.5
                pos_hint: {'center_x': 0.5, 'center_y': .3}
            Image:
                source: 'img/фон 2.png'
                size_hint: 0.92, 1
                pos_hint: {'center_x': 1.6, 'center_y': .42}
            Image:
                source: 'img/фон 2.png'
                size_hint: 0.92, 1
                pos_hint: {'center_x': 2.7, 'center_y': .42}
            Button:
                id: button_swiper
                background_normal: 'img/Настройки/подложка под кнопку вкл.png'
                background_down: 'img/Настройки/подложка под кнопку вкл.png'
                size_hint: 0.3, 0.06
                pos_hint: {'center_x': .5, 'center_y': .225}
                on_release: root.AnimButton1(button_swipe1)
            Image:
                id: button_swipe1
                source: 'img/Настройки/кнопка вкл.png'
                size_hint: 0.2, 0.2
                top_hint: 0.065
                pos_hint: {'center_x': 0.5 - self.top_hint, 'center_y': .225}
            Button:
                id: button_swiper
                background_normal: 'img/Настройки/подложка под кнопку вкл.png'
                background_down: 'img/Настройки/подложка под кнопку вкл.png'
                size_hint: 0.3, 0.06
                pos_hint: {'center_x': 1.6, 'center_y': .5}
                on_release: root.AnimButton2(button_swipe2)
            Image:
                id: button_swipe2
                source: 'img/Настройки/кнопка вкл.png'
                size_hint: 0.2, 0.2
                top_hint: 0.065
                pos_hint: {'center_x': 1.6 - self.top_hint, 'center_y': .5}
            Button:
                id: button_swiper
                background_normal: 'img/Настройки/подложка под кнопку вкл.png'
                background_down: 'img/Настройки/подложка под кнопку вкл.png'
                size_hint: 0.3, 0.06
                pos_hint: {'center_x': 1.6, 'center_y': .3}
                on_release: root.AnimButton3(button_swipe3)
            Image:
                id: button_swipe3
                source: 'img/Настройки/кнопка вкл.png'
                size_hint: 0.2, 0.2
                top_hint: 0.065
                pos_hint: {'center_x': 1.6 - self.top_hint, 'center_y': .3}
            Image:
                source: 'img/Настройки/АНИМАЦИИ.png'
                size_hint: 0.5, 0.5
                pos_hint: {'center_x': 1.6, 'center_y': .6}
            Image:
                source: 'img/Настройки/ЦВЕТ ТЕМЫ.png'
                size_hint: 0.5, 0.5
                pos_hint: {'center_x': 1.6, 'center_y': .4}
            Button:
                id: back_button
                background_normal: 'img/Настройки/назад.png'
                background_down: 'img/Настройки/назад_н.png'
                size_hint: .8, .1
                pos_hint: {'center_x': 2.7, 'center_y': .1}
                on_release: app.root.current = 'First'
                
                
        Button:
            id: sound_button
            background_normal: 'img/звук_кнопка.png'
            background_down: 'img/звук_кнопка.png'
            size_hint: 0.27, 0.051
            pos_hint: {'center_x': .18, 'center_y': .86}
            on_release: root.AnimMenuSoundButton(tempo_settings)
        Button:
            id: graphic_button
            background_normal: 'img/графика.png'
            background_down: 'img/кнопка графика.png'
            size_hint: 0.27, 0.051
            pos_hint: {'center_x': .5, 'center_y': .86}
            on_release: root.AnimMenuGraphicButton(tempo_settings)
        Button:
            id: smth_button
            background_normal: 'img/кнопка прочее.png'
            background_down: 'img/кнопка прочее.png'
            size_hint: 0.27, 0.051
            pos_hint: {'center_x': .82, 'center_y': .86}
            on_release: root.AnimMenuSmthButton(tempo_settings)

            

<ScreenThree>:
    name: 'Third'
    id: screen3
    Image:
        source: 'img/режимы.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Button:
        background_normal: "img/назад.png"
        background_down: "img/назад_н.png"
        size_hint:0.8, 0.1
        left_hint: .5
        pos_hint:{'center_x': self.left_hint, 'center_y': .1}
        on_release: app.root.current = 'First'
'''


class ScreenManagement(ScreenManager):
    pass


class ScreenOne(Screen):
    def switch(self):
        # here you can insert any python logic you like
        self.parent.current = 'Second'
        self.parent.current = 'Third'


class ScreenTwo(Screen):
    def settings(self):
        self.parent.current = 'PageOne'
        self.parent.current = 'PageTwo'

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

    def AnimMenuGraphicButton(self, widget, *args):
        anim = Animation(top_hint=-0.6, duration=0.3)
        self.ids.graphic_button.background_normal = 'img/кнопка графика.png'
        self.ids.sound_button.background_normal = 'img/кнопка звук.png'
        self.ids.smth_button.background_normal = 'img/кнопка прочее.png'
        anim.start(widget)


    def AnimMenuSoundButton(self, widget, *args):
        anim = Animation(top_hint=.5, duration=0.3)
        self.ids.graphic_button.background_normal = 'img/графика.png'
        self.ids.sound_button.background_normal = 'img/звук_кнопка.png'
        self.ids.smth_button.background_normal = 'img/кнопка прочее.png'
        anim.start(widget)

    def AnimMenuSmthButton(self, widget, *args):
        anim = Animation(top_hint=-1.7, duration=0.3)
        self.ids.graphic_button.background_normal = 'img/графика.png'
        self.ids.sound_button.background_normal = 'img/кнопка звук.png'
        self.ids.smth_button.background_normal = 'img/Group 10 (1).png'
        anim.start(widget)


class SettingPageOne(Screen):
    pass


class SettingPageTwo(Screen):
    pass


class ScreenThree(Screen):
    pass


class MyApp(App):
    def build(self):
        Builder.load_string(kvlang)
        return ScreenManagement()


if __name__ == '__main__':
    MyApp().run()
