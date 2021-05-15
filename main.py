from Game import GamePeriod
from Game import BasicPanel
from Players import EnterPlayerNum
from texts import questions_story1 as qu1
from texts import text_story1 as tx1
from Story import Story
from kivy.app import App


class NonsenseApp(App):

    def __init__(self, questions, text, **kwargs):
        super(NonsenseApp, self).__init__()
        self.my_story = Story(questions, text)
        self.game = GamePeriod(self.my_story)
        self.player_number = EnterPlayerNum(self.my_story.max_player_number)

    def build(self):
        bp = BasicPanel(self.game, self.my_story, self.player_number)
        return bp


example = NonsenseApp(qu1, tx1)
example.run()
