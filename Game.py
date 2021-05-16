from texts import dictionary
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.graphics import Color
from kivy.graphics import Rectangle


# Реализация вопросов и ответов на них, в конце выведет поле с целой историей
class GamePeriod(AnchorLayout):
    counter = 1
    labels = []

    def __init__(self, story, players, **kw):
        super().__init__(**kw)
        self.players = players
        self.answers = story.answers
        self.card_words = story.questions
        self.hint = "Пример:" + dictionary[self.card_words[0]]
        print(self.players)
        label = self.create_label(self.players[0] + ': ' + self.card_words[0])
        self.labels.append(label)
        self.add_widget(label)

    def change_card(self):
        anim_from_window_back_to_pos = Animation(x=-300, y=800)
        anim_from_window_back_to_pos.start(self.labels[len(self.labels) - 1])
        label = self.create_label(self.players[self.counter % len(self.players)] + ': ' + self.card_words[self.counter])
        self.counter += 1
        if self.counter < len(self.card_words):
            self.hint = "Пример:" + dictionary[self.card_words[self.counter]]
        self.labels.append(label)
        self.add_widget(label)

    @staticmethod
    def create_label(message):
        return Button(text=message,
                      size_hint=[0.8, 0.8],
                      background_normal='',
                      background_color=[.88, .80, .31, 1],
                      border=[10, 10, 10, 10]
                      )


class ButtonPanel(AnchorLayout):
    def __init__(self, basic_panel, **kw, ):
        super().__init__(**kw)
        self.add_widget(Button(text='ответить', size_hint=[.5, .5], on_release=basic_panel.do_all))


class BasicPanel(BoxLayout):
    box = BoxLayout(orientation='vertical')
    button = 0
    hints = dictionary

    def __init__(self, panel, story, **kwargs):
        super(BasicPanel, self).__init__(**kwargs)
        self.cards_panel = panel
        self.story = story
        self.button = ButtonPanel(self, anchor_x='center', anchor_y='top')
        self.text_field = TextInput(hint_text=self.cards_panel.hint)
        self.box.add_widget(self.cards_panel)
        self.box.add_widget(self.text_field)
        self.box.add_widget(self.button)
        self.add_widget(self.box)
        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )

        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def ready_to_get_result(self):
        completed_story = self.story.end_of_game(self.cards_panel.answers)
        result_box = BoxLayout(orientation='vertical')
        result_box.add_widget(Button(text='Завершить игру', size_hint=[.5, .5]))
        result_box.add_widget(Label(text=completed_story))
        self.remove_widget(self.box)
        self.add_widget(result_box)

    def do_all(self, instance):
        if self.cards_panel.counter < len(self.cards_panel.card_words):
            self.cards_panel.change_card()
            self.cards_panel.answers.append(self.text_field.text)
            self.text_field.hint_text = self.cards_panel.hint
            self.text_field.text = ''
        else:
            self.ready_to_get_result()
