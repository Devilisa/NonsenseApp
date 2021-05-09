# story_text я представляю как массив строк до момента, когда надо вставить ответ на вопрос, потом когда выводится на
# экран история, то выводятся по очереди элементы из массива с историей и с ответами


class Story:
    question_number = 0
    answers = []
    players_names = []

    def __init__(self, questions, story_text):
        self.questions = questions
        self.story_text = story_text
        self.max_player_number = len(questions)
        self.variations_of_player_nums = [self.max_player_number]
        for i in range(self.max_player_number // 2 + 1):
            if self.max_player_number % i == 0:
                self.variations_of_player_nums.append(self.max_player_number // i)

# adding_players - функция, которая дает возможность самим ввести имена игроков, в противном случает генерирует по

    def adding_players(self, players_number):
        for i in range(players_number):
            name = input()
            if name == '':
                name = 'Игрок ' + str(i + 1)
                self.players_names.append(name)
            else:
                self.players_names.append(name)


# end_of_game функция, выводящая целиком итог игры - историю или просто предложение, собранное из ответов на вопросы
# ask_question - функция, которая задает вопросы, пока они не кончатся, потом сама вызывает завершение игры

    def get_answer(self):
        self.answers.append(input)

    def end_of_game(self):
        for i in range(len(self.story_text)):


    def ask_question(self):
        if self.question_number < self.max_player_number:
            print(self.questions[self.question_number])
            self.question_number += 1
            self.get_answer()
        else:
            self.end_of_game()