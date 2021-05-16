from kivy.app import App
from Players import EnterPlayerNum
from texts import questions_story1 as qu1
from texts import text_story1 as tx1


# Запускает реализацию сначала ввода количества игроков, а потом ввода имен и проигрывание истории
class Players(App):
    def __init__(self,  max_num, questions, text, **kwargs):
        super(Players, self).__init__(**kwargs)
        self.max_num = max_num
        self.questions = questions
        self.text = text

    def build(self):
        epn = EnterPlayerNum(self.max_num, self.questions, self.text)
        return epn


# Example = Players(16, qu1, tx1)
# Example.run()
