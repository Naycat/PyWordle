"""Game module"""
import config
import helper as h
import os


class PyWordle1982:
    """Main game class"""

    def __init__(self, guess: str):
        """Initialize the game object"""
        self.guess = guess.upper()
        self.hint = ""
        self.secretword = h.get_random_word().upper()
        self.maxtries = 6
        self.right_letters = []
        self.wrong_place = []
        self.not_in_word = []
        self.right_guess = False
        self.current_try = 0
        self.history = config.empty_wordle
        self.hint_result = []
        self.game_on = False
        self.game_result = ""

    def create_hints(self):
        """
        creates a hint result list and updates used letters list
        """
        self.hint_result = []
        for i in range(5):
            if self.guess[i] in self.secretword:
                if self.guess[i] == self.secretword[i]:
                    self.right_letters = h.check_n_append(
                        self.guess[i], self.right_letters)
                    self.hint_result.append(
                        h.colorizer("green", self.guess[i]))
                else:
                    self.wrong_place = h.check_n_append(
                        self.guess[i], self.wrong_place)
                    self.hint_result.append(
                        h.colorizer("yellow", self.guess[i]))
            else:
                self.not_in_word = h.check_n_append(
                    self.guess[i], self.not_in_word)
                self.hint_result.append(
                    h.colorizer("grey", self.guess[i]))

    def print_and_save_hints(self):
        """Prints the hints to the terminal and shows used letters"""
        keyboard_str = config.keyboard
        self.history.update({str(self.current_try): str(
            f"|{self.hint_result[0]}|{self.hint_result[1]}|{self.hint_result[2]}|{self.hint_result[3]}|\
{self.hint_result[4]}| \n+ --- + --- + --- + --- + --- + \n")})
        print("".join(self.history.values()))
        print("Letters in the right place: ", self.right_letters)
        print("Letters in the wrong place: ", self.wrong_place)
        print("Letters not in word: ", self.not_in_word)
        for letter in set(keyboard_str):
            if letter.isalpha() and letter.isupper():
                if letter in self.right_letters:
                    keyboard_str = keyboard_str.replace(
                        f" {letter} ", h.colorizer("green", letter, True))
                elif letter in self.wrong_place:
                    keyboard_str = keyboard_str.replace(
                        f" {letter} ", h.colorizer("yellow", letter, True))
                elif letter in self.not_in_word:
                    keyboard_str = keyboard_str.replace(
                        f" {letter} ", h.colorizer("grey", letter, True))
            else:
                continue

        print(keyboard_str)

    def check_guess(self):
        self.game_on = True
        while True:
            self.current_try += 1
            print(self.current_try)
            self.create_hints()
            self.print_and_save_hints()
            if self.guess == self.secretword:
                os.system("clear")
                self.right_guess = True
                self.history.update({"Solution": str(f"|{h.colorizer('green', self.secretword[0])}|{h.colorizer('green', self.secretword[1])}|{h.colorizer('green', self.secretword[2])}|{h.colorizer('green', self.secretword[3])}|\
{h.colorizer('green', self.secretword[4])}| \n+ --- + --- + --- + --- + --- + \n")})
                print("".join(self.history.values()))
                print(config.you_won_text)
                self.game_result = "win"
                self.game_on = False
                print(self.game_on)
                self.on_game_end()
                break
            elif self.current_try == self.maxtries:
                os.system("clear")
                print("You didn't guess the right word. The answer was:",
                      self.secretword)
                self.history.update({"Solution": str(f"|{h.colorizer('green', self.secretword[0])}|{h.colorizer('green', self.secretword[1])}|{h.colorizer('green', self.secretword[2])}|{h.colorizer('green', self.secretword[3])}|\
{h.colorizer('green', self.secretword[4])}| \n+ --- + --- + --- + --- + --- + \n")})
                print("".join(self.history.values()))
                print(config.game_over_text)
                self.game_result = "lost"
                self.game_on = False
                print(self.game_on)
                self.on_game_end()

                break
            else:
                self.guess = h.control_input(
                    input("Try again, write anotherword: \n"))
                os.system("clear")

    def on_game_end(self):
        # nonlocal tries
        # nonlocal gresult
        tries = self.current_try
        gresult = self.game_result
        self.guess = ""
        self.reset()

        return [tries, gresult]

    def reset(self):
        self.hint = ""
        self.secretword = h.get_random_word().upper()
        self.maxtries = 6
        self.right_letters = []
        self.wrong_place = []
        self.not_in_word = []
        self.right_guess = False
        self.current_try = 0
        self.history = config.empty_wordle
        self.hint_result = []
        self.game_on = False
        self.game_result = ""
    # def game_history(self):

    # getting inputs
    # guess = input("Escreve a tua palavra")
