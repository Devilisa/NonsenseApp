from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class EnterPlayerNum(BoxLayout):
    def __init__(self, max_num, **kwargs):
        super(EnterPlayerNum, self).__init__(**kwargs)
        self.players_number = 0
        self.box = BoxLayout(orientation='vertical')
        hint = 'Введите количество игроков до ' + str(max_num)
        self.text_field = TextInput(hint_text=hint)
        self.box.add_widget(self.text_field)
        self.box.add_widget(Button(text='', size_hint=[.5, .5], on_release=self.get_number()))

    def get_number(self, instance):
        self.players_number = int(self.text_field.text)
        self.text_field.text = ''
        self.remove_widget(self.box)

    def press_button(self):
        self.add_widget(self.box)


class OkButton(Button):
    def __init__(self, basic_panel, **kwargs):
        super(OkButton, self).__init__(**kwargs)
        self.add_widget(Button(text='', size_hint=[.5, .5], on_release=basic_panel.getting_names))


class BasicPanel(BoxLayout):
    players_number = 0
    players_names = []
    box = BoxLayout(orientation='vertical')
    counter = 2

    def __init__(self, max_num, **kwargs):
        super(BasicPanel, self).__init__(**kwargs)
        players = EnterPlayerNum(max_num)
        players.press_button()
        self.default_players = ['Игрок ' + str(i) for i in range(1, self.players_num)]
        self.label = Label(text='Введите имя')
        self.hint = self.default_players[1]
        self.text_field = TextInput(hint_text=self.hint)

    """def get_end_number(self, instance):
        self.players_number = int(self.text_field.text)
        self.text_field.text = ''
        self.remove_widget(self.box)
             
    def get_number(self):
        box = BoxLayout(orientation='vertical')
        hint = 'Введите количество игроков до ' + str(self.max_num)
        self.text_field = TextInput(hint_text=hint)
        box.add_widget(self.text_field)
        box.add_widget(Button(text='', size_hint=[.5, .5], on_release=self.get_end_number))
        self.add_widget(box)"""

    def change_hint(self):
        self.hint = self.default_players[self.counter]
        self.counter += 1

    def getting_names(self, instance):
        if self.counter <= len(self.default_players):
            if self.text_field.text != '':
                self.players_names.append(self.text_field.text)
            else:
                self.players_names.append(self.default_players[self.counter - 1])
            self.change_hint()
            self.text_field.hint_text = self.hint
            self.text_field.text = ''


class MyApp(App):
    def build(self):
        bp = BasicPanel(16)
        return bp


Example = MyApp()
Example.run()
