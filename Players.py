from Story_play import StoryPlay
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
# В этом файле описана реализация ввода количества игроков и их имен


# Класс отвечает за ввод количества игроков и проверку вводимого значения
class EnterPlayerNum(BoxLayout):
    box = BoxLayout(orientation='vertical')

    def __init__(self, max_num, questions, text, **kwargs):
        super(EnterPlayerNum, self).__init__(**kwargs)
        self.questions = questions
        self.text = text
        self.max_num = max_num
        self.players_number = 0
        hint = 'Введите количество игроков до ' + str(max_num)
        self.text_field = TextInput(hint_text=hint)
        self.box.add_widget(self.text_field)
        self.box.add_widget(Button(text='', size_hint=[.5, .5], on_release=self.get_number))
        self.add_widget(self.box)

    def get_number(self, instance):
        var_numbers = [i + 1 for i in range(self.max_num)]
        input_info = self.text_field.text
        if input_info != '' and int(input_info) in var_numbers:
            self.players_number = int(input_info)
            self.text_field.text = ''
            self.remove_widget(self.box)
            get_names = Names(self.players_number, self.questions, self.text)
            get_names.run()
        else:
            self.remove_widget(self.box)
            self.press_again()

    def press_again(self):
        hint = 'Ошибка! Введите число от 1 до ' + str(self.max_num)
        self.text_field = TextInput(hint_text=hint)
        self.box = BoxLayout(orientation='vertical')
        self.box.add_widget(self.text_field)
        self.box.add_widget(Button(text='', size_hint=[.5, .5], on_release=self.get_number))
        self.add_widget(self.box)


# Класс отвечает за ввод имен игроков и распределение имен по умолчанию, в случае пустого поля ввода
class EnterPlayersNames(BoxLayout):
    players_number = 0
    players_names = []
    box = BoxLayout(orientation='vertical')
    counter = 1

    def __init__(self, num, questions, text, **kwargs):
        super(EnterPlayersNames, self).__init__(**kwargs)
        self.questions = questions
        self.text = text
        self.players_num = num
        self.default_players = ['Игрок ' + str(i) for i in range(1, self.players_num + 1)]
        self.label = Label(text='Введите имя')
        self.button = Button(text='Готово', size_hint=[.5, .5], on_release=self.getting_names)
        self.hint = self.default_players[0]
        self.text_field = TextInput(hint_text=self.hint)
        self.box.add_widget(self.label)
        self.box.add_widget(self.text_field)
        self.box.add_widget(self.button)
        self.add_widget(self.box)

    def change_hint(self):
        self.hint = self.default_players[self.counter]
        self.counter += 1

    def getting_names(self, instance):
        if self.counter <= len(self.default_players):
            if self.text_field.text != '':
                self.players_names.append(self.text_field.text)
            else:
                self.players_names.append(self.default_players[self.counter - 1])
            if self.counter < len(self.default_players):
                self.change_hint()
                self.text_field.hint_text = self.hint
                self.text_field.text = ''
            else:
                self.counter += 1
        else:
            self.remove_widget(self.box)
            start_story = StoryPlay(self.questions, self.text, self.players_names)
            start_story.run()


# Запускает реализацию ввода имен
class Names(App):
    def __init__(self, num, questions, text, **kwargs):
        super(Names, self).__init__(**kwargs)
        self.number = num
        self.questions = questions
        self.text = text

    def build(self):
        epn = EnterPlayersNames(self.number, self.questions, self.text)
        return epn
