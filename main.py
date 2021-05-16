from Players_add import Players
from texts import questions_story1 as qu1
from texts import text_story1 as tx1
from Story import Story
from kivy.app import App


# Запускает реализацию всего алгоритма игры после выбора истории(кнопка выбора истории должна запускать
# функцию создания объкта данного класса и его запуск)
class NonsenseApp(App):

    def __init__(self, questions, text, **kwargs):
        super(NonsenseApp, self).__init__(**kwargs)
        self.my_story = Story(questions, text)
        self.questions = questions
        self.text = text
        self.max_num = self.my_story.max_player_number

    def build(self):
        pl = Players(self.max_num, self.questions, self.text)
        pl.run()


example = NonsenseApp(qu1, tx1)
example.run()
