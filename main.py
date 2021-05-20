from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.animation import Animation
from kivy.core.text import LabelBase
import texts

Config.set("graphics", "resizeable", "0")
Config.set("graphics", "height", "667")
Config.set("graphics", "width", "375")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
import kivy
import os, random

kivy.require('1.9.0')

kvlang = '''
<ScreenManagement>:
    ScreenOne:
    ScreenTwo:
    ScreenThree:
    ScreenFourth:
    ScreenFifth:
    ScreenSix:
    ScreenSeven:
    ScreenEighth:
    ScreenNine:
    ScreenTen:
    ScreenEleven:
    ScreenTwelve:
    ScreenThirteen:
    ScreenFourteen:
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
            size_hint: .03, .06
            pos_hint: {'center_x': 1.62, 'center_y': .5}
            on_release: root.AnimScreen3Left(screen3pages)
        Button:
            background_normal: 'img/Режимы/Стрелочка_Вправо.png'
            background_down: "img/Режимы/Стрелочка_Вправо.png"
            size_hint: .03, .06
            pos_hint: {'center_x': .98, 'center_y': .5}
            on_release: root.AnimScreen3Right(screen3pages)
        Button:
            background_normal: 'img/Режимы/Текст_Классический Режим.png'
            background_down: "img/Режимы/Текст_Классический Режим.png"
            size_hint: .92, .6
            pos_hint: {'center_x': .5, 'center_y': .54}
            on_release: app.root.current = 'Fourth'
        Button:
            background_normal: 'img/Режимы/Текст_Истории.png'
            background_down: "img/Режимы/Текст_Истории.png"
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
    Label:
        text:'Ввод игроков:'
        font_size: 35
        color: .2578125, .12109375, .14453125, .98
        font_name:'Ubuntu'
        text_size: 300, None 
        pos_hint: {'center_x': .5, 'center_y': .7}   
    TextInput:
        id: input_players_1
        background_normal: "img/Режимы/Истории/Фон.png"
        background_active: "img/Режимы/Истории/Фон.png"
        font_size: 30
        hint_text:'Введите кол-во игроков от 1 до 10'
        font_name:'Ubuntu'
        foreground_color: 1, 1, 1, 1
        size_hint:0.9, 0.2
        pos_hint:{'center_x': .5, 'center_y': .5}
        on_text: root.process()
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .28, 'center_y': .32}
        on_release: app.root.current = 'Third'
    Button:
        background_normal: "img/Режимы/Истории/Принять.png"
        background_down: "img/Режимы/Истории/Принять.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .72, 'center_y': .32}
        on_release: app.root.current = 'Eighth'
         

<ScreenFifth>:
    name: 'Fifth'
    id: screen5
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Label:
        text:'Ввод игроков:'
        font_size: 35
        color: .2578125, .12109375, .14453125, .98
        font_name:'Ubuntu'
        text_size: 300, None 
        pos_hint: {'center_x': .5, 'center_y': .7}   
    TextInput:
        id: input_players_2
        background_normal: "img/Режимы/Истории/Фон.png"
        background_active: "img/Режимы/Истории/Фон.png"
        font_size: 30
        hint_text:'Введите кол-во игроков от 1 до 10'
        font_name:'Ubuntu'
        foreground_color: 1, 1, 1, 1
        size_hint:0.9, 0.2
        pos_hint:{'center_x': .5, 'center_y': .5}
        on_text: root.process()
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .28, 'center_y': .32}
        on_release: app.root.current = 'Third'
    Button:
        background_normal: "img/Режимы/Истории/Принять.png"
        background_down: "img/Режимы/Истории/Принять.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .72, 'center_y': .32}
        on_release: app.root.current = 'Six'

<ScreenSix>:        
    name: 'Six'
    id: screen6
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    FloatLayout:
        top_hint: .5
        id: sf
        name:'ScreenFloat'
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    FloatLayout:
        top_hint: .5
        id: page_buttons
        name:'ScreenFloat'
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    Label:
        text:'Придумайте Имена:'
        font_size: 40
        color: .2578125, .12109375, .14453125, .98
        font_name:'Ubuntu'
        text_size: 300, None 
        pos_hint: {'center_x': .5, 'center_y': .9} 
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .28, 'center_y': .1}
        on_release: app.root.current = 'Third'
        on_release: sf.clear_widgets()
        on_release: page_buttons.clear_widgets()
        on_release: sf.top_hint = .5   
    Button:
        id: enter 
        background_normal: "img/Режимы/Истории/Принять.png"
        background_down: "img/Режимы/Истории/Принять.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .72, 'center_y': .1}
        on_release: app.root.current = 'Seven'   
        on_release: sf.clear_widgets()
        on_release: page_buttons.clear_widgets()
        on_release: sf.top_hint = .5

<ScreenSeven>:         
    name: 'Seven'
    id: screen7
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Label:
        text:'Выберете историю'
        font_size: 40
        color: .2578125, .12109375, .14453125, .98
        font_name:'Ubuntu'
        text_size: 300, None 
        pos_hint: {'center_x': .5, 'center_y': .9} 
    Button:
        background_normal: "img/Режимы/Истории/Фон_конпки.png"
        background_down: "img/Режимы/Истории/Фон_конпки.png"
        font_size: 35
        font_name:'Ubuntu'
        text: 'Тени Кавголово'
        size_hint:0.8, 0.1
        pos_hint:{'center_x': .5, 'center_y': .8}
        on_release: app.root.current = 'Nine' 
    Button:
        background_normal: "img/Режимы/Истории/Фон_конпки.png"
        background_down: "img/Режимы/Истории/Фон_конпки.png"
        font_size: 30
        font_name:'Ubuntu'
        text: 'Моя купчинская история'
        size_hint:0.8, 0.1
        pos_hint:{'center_x': .5, 'center_y': .68}
        on_release: app.root.current = 'Ten'  
    Button:
        background_normal: "img/Режимы/Истории/Фон_конпки.png"
        background_down: "img/Режимы/Истории/Фон_конпки.png"
        font_size: 35
        font_name:'Ubuntu'
        text: 'Секрет лесов'
        size_hint:0.8, 0.1
        pos_hint:{'center_x': .5, 'center_y': .56}
        on_release: app.root.current = 'Eleven'  
    Button:
        background_normal: "img/Режимы/Истории/Фон_конпки.png"
        background_down: "img/Режимы/Истории/Фон_конпки.png"
        font_size: 35
        font_name:'Ubuntu'
        text: 'Как выжить в Москве'
        size_hint:0.8, 0.1
        pos_hint:{'center_x': .5, 'center_y': .44}
        on_release: app.root.current = 'Twelve'   
    Button:
        background_normal: "img/Режимы/Истории/Фон_конпки.png"
        background_down: "img/Режимы/Истории/Фон_конпки.png"
        font_size: 35
        font_name:'Ubuntu'
        text: '10 вопросов'
        size_hint:0.8, 0.1
        pos_hint:{'center_x': .5, 'center_y': .32}
        on_release: app.root.current = 'Thirteen'  
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.6, 0.09
        pos_hint:{'center_x': .5, 'center_y': .1}
        on_release: app.root.current = 'Third'  
        
<ScreenEighth>: 
    name: 'Eighth'
    id: screen8
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    FloatLayout:
        top_hint: .5
        id: ef
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    FloatLayout:
        top_hint: .5
        id: page_buttons_e
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    Label:
        text:'Придумайте Имена:'
        font_size: 40
        color: .2578125, .12109375, .14453125, .98
        font_name:'Ubuntu'
        text_size: 300, None 
        pos_hint: {'center_x': .5, 'center_y': .9} 
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .28, 'center_y': .1}
        on_release: app.root.current = 'Third'   
        on_release: ef.clear_widgets()
        on_release: page_buttons_e.clear_widgets()
        on_release: ef.top_hint = .5
    Button:
        id: enter1 
        background_normal: "img/Режимы/Истории/Принять.png"
        background_down: "img/Режимы/Истории/Принять.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .72, 'center_y': .1}
        on_release: app.root.current = 'Nine'   
        on_release: ef.clear_widgets()
        on_release: page_buttons_e.clear_widgets()
        on_release: ef.top_hint = .5
    

<ScreenNine>:
    name: 'Nine'
    id: screen9
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Image:
        id: player_img
        size_hint: .16, .09
        pos_hint: {'center_x': .1, 'center_y': .9}
    Label:
        id:player
        size_hint: .6, .09
        pos_hint: {'center_x': .72, 'center_y': .9}
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        text_size: 300, None 
    FloatLayout:
        top_hint: .5
        id: ti1
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .28, 'center_y': .1}
        on_release: app.root.current = 'Seven'   
        on_release: root.back_button()   
    Button:
        id: confirm_button
        background_normal: "img/Режимы/Истории/Принять.png"
        background_down: "img/Режимы/Истории/Принять.png"
        size_hint:0.4, 0.08   
        pos_hint: {'center_x': .72, 'center_y': .1}
        on_release: root.ret()
    TextInput:
        id: lala
        background_normal:"img/Режимы/Истории/Фон.png"
        background_active:"img/Режимы/Истории/Фон.png"
        font_size:40
        font_name:'Ubuntu'
        foreground_color: 1, 1, 1, 1
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .3}
        on_text: root.process()
    Label:
        id: text_story_1
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .7}
        text_size: 300, None 

<ScreenTen>:
    name: 'Ten'
    id: screen10
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Image:
        id: player_img
        size_hint: .16, .09
        pos_hint: {'center_x': .1, 'center_y': .9}
    Label:
        id:player
        size_hint: .6, .09
        pos_hint: {'center_x': .72, 'center_y': .9}
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        text_size: 300, None 
    FloatLayout:
        top_hint: .5
        id: ti1
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .28, 'center_y': .1}
        on_release: app.root.current = 'Seven'   
        on_release: root.back_button()   
    Button:
        id: confirm_button
        background_normal: "img/Режимы/Истории/Принять.png"
        background_down: "img/Режимы/Истории/Принять.png"
        size_hint:0.4, 0.08   
        pos_hint: {'center_x': .72, 'center_y': .1}
        on_release: root.ret()
    TextInput:
        id: lala
        background_normal:"img/Режимы/Истории/Фон.png"
        background_active:"img/Режимы/Истории/Фон.png"
        font_size:40
        font_name:'Ubuntu'
        foreground_color: 1, 1, 1, 1
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .3}
        on_text: root.process()
    Label:
        id: text_story_1
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .7}
        text_size: 300, None 

        
<ScreenEleven>:
    name: 'Eleven'
    id: screen11
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Image:
        id: player_img
        size_hint: .16, .09
        pos_hint: {'center_x': .1, 'center_y': .9}
    Label:
        id:player
        size_hint: .6, .09
        pos_hint: {'center_x': .72, 'center_y': .9}
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        text_size: 300, None 
    FloatLayout:
        top_hint: .5
        id: ti1
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .28, 'center_y': .1}
        on_release: app.root.current = 'Seven'   
        on_release: root.back_button()   
    Button:
        id: confirm_button
        background_normal: "img/Режимы/Истории/Принять.png"
        background_down: "img/Режимы/Истории/Принять.png"
        size_hint:0.4, 0.08   
        pos_hint: {'center_x': .72, 'center_y': .1}
        on_release: root.ret()
    TextInput:
        id: lala
        background_normal:"img/Режимы/Истории/Фон.png"
        background_active:"img/Режимы/Истории/Фон.png"
        font_size:40
        font_name:'Ubuntu'
        foreground_color: 1, 1, 1, 1
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .3}
        on_text: root.process()
    Label:
        id: text_story_1
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .7}
        text_size: 300, None 

<ScreenTwelve>:
    name: 'Twelve'
    id: screen12
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Image:
        id: player_img
        size_hint: .16, .09
        pos_hint: {'center_x': .1, 'center_y': .9}
    Label:
        id:player
        size_hint: .6, .09
        pos_hint: {'center_x': .72, 'center_y': .9}
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        text_size: 300, None 
    FloatLayout:
        top_hint: .5
        id: ti1
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .28, 'center_y': .1}
        on_release: app.root.current = 'Seven'   
        on_release: root.back_button()   
    Button:
        id: confirm_button
        background_normal: "img/Режимы/Истории/Принять.png"
        background_down: "img/Режимы/Истории/Принять.png"
        size_hint:0.4, 0.08   
        pos_hint: {'center_x': .72, 'center_y': .1}
        on_release: root.ret()
    TextInput:
        id: lala
        background_normal:"img/Режимы/Истории/Фон.png"
        background_active:"img/Режимы/Истории/Фон.png"
        font_size:40
        font_name:'Ubuntu'
        foreground_color: 1, 1, 1, 1
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .3}
        on_text: root.process()
    Label:
        id: text_story_1
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .7}
        text_size: 300, None 
        
<ScreenThirteen>:
    name: 'Thirteen'
    id: screen13
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    Image:
        id: player_img
        size_hint: .16, .09
        pos_hint: {'center_x': .1, 'center_y': .9}
    Label:
        id:player
        size_hint: .6, .09
        pos_hint: {'center_x': .72, 'center_y': .9}
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        text_size: 300, None 
    FloatLayout:
        top_hint: .5
        id: ti1
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .28, 'center_y': .1}
        on_release: app.root.current = 'Seven'   
        on_release: root.back_button()   
    Button:
        id: confirm_button
        background_normal: "img/Режимы/Истории/Принять.png"
        background_down: "img/Режимы/Истории/Принять.png"
        size_hint:0.4, 0.08   
        pos_hint: {'center_x': .72, 'center_y': .1}
        on_release: root.ret()
    TextInput:
        id: lala
        background_normal:"img/Режимы/Истории/Фон.png"
        background_active:"img/Режимы/Истории/Фон.png"
        font_size:40
        font_name:'Ubuntu'
        foreground_color: 1, 1, 1, 1
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .3}
        on_text: root.process()
    Label:
        id: text_story_1
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .7}
        text_size: 300, None    
        
<ScreenFourteen>:
    name: 'Fourteen'
    id: screen14
    Image:
        source: 'img/Настройки/Фон/Фон.png'
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    FloatLayout:
        top_hint: .5
        id: page
        pos_hint: {'center_x': self.top_hint, 'center_y': .5}
    Label:
        id: text_story_1
        font_size:30
        font_name:'Ubuntu'
        color: .2578125, .12109375, .14453125, .98
        size_hint: 0.7, 0.09
        pos_hint:{'center_x': .5, 'center_y': .9}
        text_size: 300, None     
        text: 'Результат: '
    FloatLayout:
        top_hint: .5
        id: page_buttons
        pos_hint: {'center_x': self.top_hint, 'center_y': .5} 
    Button:
        background_normal: "img/Настройки/назад.png"
        background_down: "img/Настройки/назад.png"
        size_hint:0.4, 0.08
        pos_hint:{'center_x': .5, 'center_y': .1}
        on_release: app.root.current = 'Seven'
        on_release: root.back_button()   
        on_release: page.clear_widgets()
'''
LabelBase.register(name='Ubuntu', fn_regular='font/UbuntuCondensed-Regular.ttf')


class ScreenManagement(ScreenManager):
    pass


class ScreenOne(Screen):
    def switch(self):
        # here you can insert any python logic you like
        self.parent.current = 'Second'
        self.parent.current = 'Third'
        self.parent.current = 'Fourth'
        self.parent.current = 'Fifth'


class ScreenTwo(Screen):
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
    def process(self):
        global text1
        text1 = self.ids.input_players_1.text


class ScreenFifth(Screen):
    def process(self):
        global text
        text = self.ids.input_players_2.text


players_names2 = []


class ScreenSix(Screen):
    def on_pre_enter(self, *args):
        t_int = int(text)
        x = .1
        y = .75
        if t_int > 10:
            t_int = 10
        elif t_int < 1:
            t_int = 1
        for i in range(t_int):
            if i == 4:
                x += 1
                y = .75
                self.ids.page_buttons.add_widget(Button(text='1', size_hint=(0.16, 0.09),
                                                        pos_hint={'center_x': .28, 'center_y': .2},
                                                        background_normal="img/Режимы/Истории/Фон_конпки.png",
                                                        font_size=40, font_name='Ubuntu',
                                                        background_down="img/Режимы/Истории/Фон_конпки.png",
                                                        on_release=lambda x: self.AnimButton1(self.ids.sf)))
                self.ids.page_buttons.add_widget(Button(text='2', size_hint=(0.16, 0.09),
                                                        pos_hint={'center_x': .5, 'center_y': .2},
                                                        background_normal="img/Режимы/Истории/Фон_конпки.png",
                                                        font_size=40, font_name='Ubuntu',
                                                        background_down="img/Режимы/Истории/Фон_конпки.png",
                                                        on_release=lambda x: self.AnimButton2(self.ids.sf)))
            elif i == 8:
                x += 1
                y = .75
                self.ids.page_buttons.add_widget(Button(text='3', size_hint=(0.16, 0.09),
                                                        pos_hint={'center_x': .72, 'center_y': .2},
                                                        background_normal="img/Режимы/Истории/Фон_конпки.png",
                                                        font_size=40, font_name='Ubuntu',
                                                        background_down="img/Режимы/Истории/Фон_конпки.png",
                                                        on_release=lambda x: self.AnimButton3(self.ids.sf)))
            image_name = random.choice(os.listdir('img/Режимы/Истории/Иконки'))
            text_field = TextInput(text='Игрок' + str(i + 1), background_normal="img/Режимы/Истории/Фон.png",
                                             background_active="img/Режимы/Истории/Фон.png", font_size=40,
                                             hint_text='Введите имя игрока', font_name='Ubuntu',
                                             foreground_color=(1, 1, 1, 1),
                                             size_hint=(0.7, 0.09), pos_hint={'center_x': x + .5, 'center_y': y})
            self.ids.sf.add_widget(text_field)
            self.ids.sf.add_widget(Image(source='img/Режимы/Истории/Иконки/' + image_name,
                                         pos_hint={'center_x': x, 'center_y': y}, size_hint=(0.16, 0.09)))
            player_info = [text_field.text, 'img/Режимы/Истории/Иконки/' + image_name]
            players_names2.append(player_info)
            y -= .15


    def AnimButton1(self, widget, *args):
        anim = Animation(top_hint=0.5, duration=0.3)
        anim.start(widget)

    def AnimButton2(self, widget, *args):
        anim = Animation(top_hint=-0.5, duration=0.3)
        anim.start(widget)

    def AnimButton3(self, widget, *args):
        anim = Animation(top_hint=-1.5, duration=0.3)
        anim.start(widget)


class ScreenSeven(Screen):
    pass


players_names = []


class ScreenEighth(Screen):
    def on_pre_enter(self, *args):
        t_int = int(text1)
        x = .1
        y = .75
        if t_int > 10:
            t_int = 10
        elif t_int < 2:
            t_int = 2
        for i in range(t_int):
            if i == 4:
                x += 1
                y = .75
                self.ids.page_buttons_e.add_widget(Button(text='1', size_hint=(0.16, 0.09),
                                                          pos_hint={'center_x': .28, 'center_y': .2},
                                                          background_normal="img/Режимы/Истории/Фон_конпки.png",
                                                          font_size=40, font_name='Ubuntu',
                                                          background_down="img/Режимы/Истории/Фон_конпки.png",
                                                          on_release=lambda x: self.AnimButton1(self.ids.ef)))
                self.ids.page_buttons_e.add_widget(Button(text='2', size_hint=(0.16, 0.09),
                                                          pos_hint={'center_x': .5, 'center_y': .2},
                                                          background_normal="img/Режимы/Истории/Фон_конпки.png",
                                                          font_size=40, font_name='Ubuntu',
                                                          background_down="img/Режимы/Истории/Фон_конпки.png",
                                                          on_release=lambda x: self.AnimButton2(self.ids.ef)))
            elif i == 8:
                x += 1
                y = .75
                self.ids.page_buttons_e.add_widget(Button(text='3', size_hint=(0.16, 0.09),
                                                          pos_hint={'center_x': .72, 'center_y': .2},
                                                          background_normal="img/Режимы/Истории/Фон_конпки.png",
                                                          font_size=40, font_name='Ubuntu',
                                                          background_down="img/Режимы/Истории/Фон_конпки.png",
                                                          on_release=lambda x: self.AnimButton3(self.ids.ef)))
            image_name = random.choice(os.listdir('img/Режимы/Истории/Иконки'))
            text_field = TextInput(text='Игрок' + str(i + 1), background_normal="img/Режимы/Истории/Фон.png",
                                             background_active="img/Режимы/Истории/Фон.png", font_size=40,
                                             hint_text='Введите имя игрока', font_name='Ubuntu',
                                             foreground_color=(1, 1, 1, 1),
                                             size_hint=(0.7, 0.09), pos_hint={'center_x': x + .5, 'center_y': y})
            self.ids.sf.add_widget(text_field)
            player_info = [text_field.text, 'img/Режимы/Истории/Иконки/' + image_name]
            players_names.append(player_info)
            self.ids.ef.add_widget(Image(source='img/Режимы/Истории/Иконки/' + image_name,
                                         pos_hint={'center_x': x, 'center_y': y}, size_hint=(0.16, 0.09)))
            y -= .15

    def AnimButton1(self, widget, *args):
        anim = Animation(pos_hint={'center_x': .5}, duration=0.3)
        anim.start(widget)

    def AnimButton2(self, widget, *args):
        anim = Animation(top_hint=-0.5, duration=0.3)
        anim.start(widget)

    def AnimButton3(self, widget, *args):
        anim = Animation(top_hint=-1.5, duration=0.3)
        anim.start(widget)


mat = []
story = 1

class ScreenNine(Screen):
    def on_pre_enter(self, *args):
        self.counter_i = 0
        self.counter_j = 0
        self.ids.lala.hint_text = texts.questions_story1[self.counter_i]
        self.ids.player_img.source = players_names2[self.counter_i][1]
        self.ids.player.text = players_names2[self.counter_i][0]

    def ret(self):
        self.counter_i += 1
        self.counter_j += 1
        self.ids.lala.hint_text = texts.questions_story1[self.counter_i]
        if len(players_names2) > self.counter_j:
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        else:
            self.counter_j -= len(players_names2)
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        mat.append(text2)
        self.ids.lala.text = ''
        if self.counter_i == 13:
            global story
            story = 1
            self.manager.current = 'Fourteen'

    def process(self):
        global text2
        text2 = self.ids.lala.text

    def back_button(self):
        global mat
        mat = []


class ScreenTen(Screen):
    def on_pre_enter(self, *args):
        self.counter_i = 0
        self.counter_j = 0
        self.ids.lala.hint_text = texts.questions_story2[self.counter_i]
        self.ids.player_img.source = players_names2[self.counter_i][1]
        self.ids.player.text = players_names2[self.counter_i][0]

    def ret(self):
        self.counter_i += 1
        self.counter_j += 1
        self.ids.lala.hint_text = texts.questions_story2[self.counter_i]
        if len(players_names2) > self.counter_j:
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        else:
            self.counter_j -= len(players_names2)
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        mat.append(text3)
        self.ids.lala.text = ''
        if self.counter_i == 10:
            global story
            story = 2
            self.manager.current = 'Fourteen'


    def process(self):
        global text3
        text3 = self.ids.lala.text

    def back_button(self):
        global mat
        mat = []

class ScreenEleven(Screen):
    def on_pre_enter(self, *args):
        self.counter_i = 0
        self.counter_j = 0
        self.ids.lala.hint_text = texts.questions_story3[self.counter_i]
        mat.append(texts.text_story3[self.counter_i])
        self.ids.player_img.source = players_names2[self.counter_i][1]
        self.ids.player.text = players_names2[self.counter_i][0]

    def ret(self):
        self.counter_i += 1
        self.counter_j += 1
        self.ids.lala.hint_text = texts.questions_story3[self.counter_i]
        if len(players_names2) > self.counter_j:
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        else:
            self.counter_j -= len(players_names2)
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        mat.append(text4)
        self.ids.lala.text = ''
        if self.counter_i == 10:
            global story
            story = 3
            self.manager.current = 'Fourteen'


    def process(self):
        global text4
        text4 = self.ids.lala.text

    def back_button(self):
        global mat
        mat = []


class ScreenTwelve(Screen):
    def on_pre_enter(self, *args):
        self.counter_i = 0
        self.counter_j = 0
        self.ids.lala.hint_text = texts.questions_story4[self.counter_i]
        mat.append(texts.text_story4[self.counter_i])
        self.ids.player_img.source = players_names2[self.counter_i][1]
        self.ids.player.text = players_names2[self.counter_i][0]

    def ret(self):
        self.counter_i += 1
        self.counter_j += 1
        self.ids.lala.hint_text = texts.questions_story4[self.counter_i]
        if len(players_names2) > self.counter_j:
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        else:
            self.counter_j -= len(players_names2)
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        mat.append(text5)
        self.ids.lala.text = ''
        if self.counter_i == 9:
            global story
            story = 4
            self.manager.current = 'Fourteen'

    def process(self):
        global text5
        text5 = self.ids.lala.text

    def back_button(self):
        global mat
        mat = []


class ScreenThirteen(Screen):
    def on_pre_enter(self, *args):
        self.counter_i = 0
        self.counter_j = 0
        self.ids.lala.hint_text = texts.questions_story5[self.counter_i]
        mat.append(texts.text_story5[self.counter_i])
        self.ids.player_img.source = players_names2[self.counter_i][1]
        self.ids.player.text = players_names2[self.counter_i][0]

    def ret(self):
        self.counter_i += 1
        self.counter_j += 1
        self.ids.lala.hint_text = texts.questions_story5[self.counter_i]
        if len(players_names2) > self.counter_j:
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        else:
            self.counter_j -= len(players_names2)
            self.ids.player_img.source = players_names2[self.counter_j][1]
            self.ids.player.text = players_names2[self.counter_j][0]
        mat.append(text6)
        self.ids.lala.text = ''
        if self.counter_i == 9:
            global story
            story =  5
            self.manager.current = 'Fourteen'

    def process(self):
        global text6
        text6 = self.ids.lala.text

    def back_button(self):
        global mat
        mat = []


class ScreenFourteen(Screen):
    def on_pre_enter(self, *args):
        text_dict = texts.text_story1
        if story == 2:
            text_dict = texts.text_story2
        elif story == 3:
            text_dict = texts.text_story3
        elif story == 4:
            text_dict = texts.text_story4
        elif story == 5:
            text_dict = texts.text_story5
        counter_i = 0
        counter_j = 0
        text_full = ''
        for i in text_dict:
            if i == '':
                text_dict[counter_i] = mat[counter_j-1]
                counter_j += 1
            text_full += text_dict[counter_i]
            counter_i += 1
        self.ids.page.add_widget(Label(text=text_full, text_size=(300, None), pos_hint={'center_x': .5, 'center_y': .5},
                                       font_size=16, font_name='Ubuntu', color=(.2578125, .12109375, .14453125, .98)))

    def back_button(self):
        global mat
        mat = []


class MyApp(App):
    def build(self):
        Builder.load_string(kvlang)
        return ScreenManagement()


if __name__ == '__main__':
    MyApp().run()