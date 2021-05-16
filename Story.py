# Вспомогательный класс для реализации некоторых действий с историей
class Story:
    answers = []
    players_names = []

    def __init__(self, questions, story_text):
        self.questions = questions
        self.story_text = story_text
        self.max_player_number = len(questions)
        self.variations_of_player_nums = [self.max_player_number]
        for i in range(1, self.max_player_number // 2 + 1):
            if self.max_player_number % i == 0:
                self.variations_of_player_nums.append(self.max_player_number // i)

    # end_of_game функция, выводящая целиком итог игры - историю или просто предложение, собранное из ответов на вопросы

    def end_of_game(self, answers):
        completed_story = ''
        j = 0
        for i in range(len(answers)):
            if self.story_text[i] == '':
                self.story_text[i] = answers[j]
                j += 1
            completed_story = completed_story + self.story_text[i]
        return completed_story
