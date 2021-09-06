#hangman game
from random import randint
import os

def clear():
    os.system('cls')

class hangman:
    generated_word = []
    error = 0
    theWord = ""
    blanks = 0
    count = 0

    def reset(self):
        self.generated_word = []
        self.error = 0
        self.theWord = ""
        self.blanks = 0
        self.count = 0
        self.generate_word()
        self.number_of_blanks()

    def print_all_letters(self):
        print("\n\t\t\t\t\t\t  Guess the word")
        print("\n\t\t\t\t\t\t   ", end="")
        for i in range(0, len(self.generated_word)):
            print(self.generated_word[i], end="")

    def generate_word(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        word_list = ['babel', 'javascript', 'script', 'python', 'django']
        word = word_list[randint(0, len(word_list) - 1)]
        for i in range(0, len(word)):
            if word[i] in vowels:
                self.generated_word.append(word[i])
            else:
                self.generated_word.append("_")
        self.theWord = word
        return word

    def number_of_blanks(self):
        blanks = 0
        for i in range(0, len(self.theWord)):
            if self.generated_word[i] == "_":
                blanks += 1
        self.blanks = blanks
        return blanks

    def __init__(self):
        self.generate_word()
        self.number_of_blanks()

    def word_check(self, user_input):
        for i in range(self.count, len(self.theWord)):
            if (user_input == self.theWord[i]):
                self.generated_word[i] = user_input
                self.count += 1
                return True
            else:
                continue
        self.error += 1
        self.hangman_log()
        return False

    def word_completed(self):
        if self.number_of_blanks() == 0:
            return True
        else:
            return False

    def hangman_log(self):
        if self.error == 1:
            print("\n\n\n\n\t\t\t\t\t\t______________\n\t\t\t\t\t\t|     |       \n\t\t\t\t\t\t|     O       \n\t\t\t\t\t\t|\n\t\t\t\t\t\t|\n\t\t\t\t\t\t|\n\t\t\t\t\t\t|")
        elif self.error == 2:
            print("\n\n\n\n\t\t\t\t\t\t______________\n\t\t\t\t\t\t|     |       \n\t\t\t\t\t\t|     O       \n\t\t\t\t\t\t|     |       \n\t\t\t\t\t\t|\n\t\t\t\t\t\t|\n\t\t\t\t\t\t|")
        elif self.error == 3:
            print("\n\n\n\n\t\t\t\t\t\t______________\n\t\t\t\t\t\t|     |       \n\t\t\t\t\t\t|     O       \n\t\t\t\t\t\t|    /|\      \n\t\t\t\t\t\t|\n\t\t\t\t\t\t|\n\t\t\t\t\t\t|")
        elif self.error == 4:
            print("\n\n\n\n\t\t\t\t\t\t______________\n\t\t\t\t\t\t|     |       \n\t\t\t\t\t\t|     O       \n\t\t\t\t\t\t|    /|\      \n\t\t\t\t\t\t|    / \      \n\t\t\t\t\t\t|\n\t\t\t\t\t\t|")
            print("\n\n\t\t\t\t\t*********************************************")

    def play(self):
        won = False
        while not hangman_game.word_completed() and hangman_game.error < 4:
            self.print_all_letters()
            user_input = input("\n\n\n\n\t\t\t\tPLease enter a character:  ").lower()
            clear()
            word_check = self.word_check(user_input)
            if not self.word_completed():
                if self.error < 4:
                    if not word_check:
                        print("\n\n\t\t\t\t\t{} is not in the WORD. {} tries left\n\n\n\t\t\t\t  ===================================================".format(user_input, 4 - self.error))
                    else:
                        print("\n\n\n\n\n\n\t\t\t\t\t\t{} is correct. Keep going!!\n\n\n\n\n\n\t\t\t\t  ===================================================".format(user_input))
                else:
                    print("\n\n\n\n\t\t\t\t\t\tYou lost!, the correct word is \n\n\t\t\t\t\t\t\t{}".format(self.theWord.upper()))
            else:
                print("\n\n\t\t\t\t\t\tThe word is ........ {}".format(self.theWord.upper()))
                print("\n\n\n\n\t\t\t\t\t\t    \O/      \n\t\t\t\t\t\t     |       \n\t\t\t\t\t\t    / \      \tYou Won!!")
                won = True
        return won

class Player:
    score = 0
    name = ""
    def add_to_score(self):
        self.score +=1


play = True

thePlayer = Player()

thePlayer.name = input("\n\n\n\n\n\t\t\t\tWelcome to Hangman, please enter your NAME to continue: \n\n\t\t\t\t\t")
while play:
    clear()
    print("\n\n\n\n\t\t\t\t\t*************Welcome to************\n\t\t\t\t\t\t      HANGMAN\t\tSCORE: {}".format(thePlayer.score))
    print("\t\t\t\t\t\t         O       \n\t\t\t\t\t\t        <|>      \n\t\t\t\t\t\t        / \      \n\n\t\t\t\tHi {}\n\n\t\t\t\t  ===================================================".format(thePlayer.name))
    hangman_game = hangman()
    hangman_game.reset()
    result = hangman_game.play()
    if result:
        thePlayer.add_to_score()
    user_input = input("\n\t\t\t\t\t\tDo you want to play again?(y or n)").lower()
    if user_input != 'y':
        play = False

