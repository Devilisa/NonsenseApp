# story_text я представляю как массив строк до момента, когда надо вставить ответ на вопрос, потом когда выводится на
# экран история, то выводятся по очереди элементы из массива с историей и с ответами


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

    # adding_players - функция, которая дает возможность самим ввести имена игроков, в противном случает генерирует по

    def adding_players(self, players_number):
        default_players = ['Игрок ' + str(i) for i in range(1, players_number)]
        for i in range(players_number):
            name = input()
            if name == '':
                name = default_players[i+1]
                self.players_names.append(name)
            else:
                self.players_names.append(name)

    # end_of_game функция, выводящая целиком итог игры - историю или просто предложение, собранное из ответов на вопросы
    # ask_question - функция, которая задает вопросы, пока они не кончатся, потом сама вызывает завершение игры

    def end_of_game(self, answers):
        completed_story = ''
        j = 0
        for i in range(len(answers)):
            if self.story_text[i] == '':
                self.story_text[i] = answers[j]
                j += 1
            completed_story = completed_story + self.story_text[i]
        return completed_story


