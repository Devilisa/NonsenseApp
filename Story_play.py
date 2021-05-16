from Game import GamePeriod
from Game import BasicPanel
from Story import Story
from kivy.app import App


# Запускает реализацию истории
class StoryPlay(App):

    def __init__(self, questions, text, names, **kwargs):
        super(StoryPlay, self).__init__(**kwargs)
        self.my_story = Story(questions, text)
        self.game = GamePeriod(self.my_story, names)
        self.players_names = names

    def build(self):
        bp = BasicPanel(self.game, self.my_story)
        return bp


# example = StoryPlay(qu1, tx1, 16)
# example.run()
