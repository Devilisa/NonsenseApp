from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.graphics import Color
from kivy.graphics import Rectangle


class CardsPanel(AnchorLayout):
    card_words = ["что", "где", "когда", "с кем", "oseuhlgius"]
    counter = 1
    labels = []

    def __init__(self, **kw):
        super().__init__(**kw)
        label = self.create_label(self.card_words[0])
        self.labels.append(label)
        self.add_widget(label)

    def change_card(self):
        anim_from_window_back_to_pos = Animation(x=-300, y=800)
        anim_from_window_back_to_pos.start(self.labels[len(self.labels) - 1])
        label = self.create_label(self.card_words[self.counter])
        self.counter += 1
        self.labels.append(label)
        self.add_widget(label)

    def create_label(self, message):
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
    cards_panel = CardsPanel()
    text_field = TextInput()
    button = 0
    answers = []

    def __init__(self, **kwargs):
        super(BasicPanel, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical')
        self.button = ButtonPanel(self, anchor_x='center', anchor_y='top')
        box.add_widget(self.cards_panel)
        box.add_widget(self.text_field)
        box.add_widget(self.button)
        self.add_widget(box)
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

    def do_all(self, instance):
        self.cards_panel.change_card()
        self.answers.append(self.text_field.text)
        self.text_field.text = ''


class ButtonExample(App):
    def build(self):
        bp = BasicPanel()
        return bp


example = ButtonExample()
example.run()
