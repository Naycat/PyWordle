"""PyWordle - Python implementation of the popular Wordle game engine
"""

################################################################

# Command line menu
# inputs user guess
# outputs hint
# 1 - one secret world and one try

# Main game class


class PyWordle1982:
    """Main game class"""

    def __init__(self, guess: str):
        """Initialize the game object"""
        self.guess = guess.lower()
        self.hint = ""
        self.secretword = "lapso"
        self.maxtries = 6
        self.right_letters = []
        self.wrong_place = []
        self.not_in_word = []
        self.right_guess = False
        self.current_try = 0
        self.hint_result = []
        self.history = ""

    def green(self, letter): return f'\033[92m {letter}\033[00m'
    def yellow(self, letter): return f'\033[93m {letter}\033[00m'
    def grey(self, letter): return f'\033[90m {letter}\033[00m'

    def create_hints(self):
        self.hint_result = []
        for i in range(5):
            if self.guess[i] in self.secretword:
                if self.guess[i] == self.secretword[i]:
                    self.right_letters.append(self.guess[i])
                    self.hint_result.append(self.green(self.guess[i]))
                else:
                    self.wrong_place.append(self.guess[i])
                    self.hint_result.append(self.yellow(self.guess[i]))
            else:
                self.not_in_word.append(self.guess[i])
                self.hint_result.append(self.grey(self.guess[i]))

    def print_and_save_hints(self):
        self.history += str(
            f"+ --- + --- + --- + --- + --- + \n | {self.hint_result[0]}  | {self.hint_result[1]}  | {self.hint_result[2]}  | {self.hint_result[3]}  | {self.hint_result[4]}  | \n + --- + --- + --- + --- + --- + \n")
        print(self.history)
        print("Letters in the right place: ", self.right_letters)
        print("Letters in the wrong place: ", self.wrong_place)
        print("Letters not in word: ", self.not_in_word)

    def check_guess(self):
        while True:
            self.create_hints()
            self.print_and_save_hints()
            self.current_try += 1
            self.guess = input("Try again, write anotherword: \n")
            if self.guess == self.secretword or self.current_try == self.maxtries:
                break
        if self.guess == self.secretword:
            self.right_guess = True
            print("Acertaste!")
            exit()
        if self.current_try >= self.maxtries:
            print("You didn't guess the right word. The answer was:",
                  self.secretword)
            exit()

    # def game_history(self):

    # getting inputs
    # guess = input("Escreve a tua palavra")


if __name__ == "__main__":

    userinput = input("Please write a 5 letter word: \n")
    while len(userinput) != 5 and userinput.isalpha() is False:
        userinput = input("Please enter a word with 5 letters: \n")
    userguess = PyWordle1982(userinput)
    while userguess.current_try <= userguess.maxtries:
        userguess.check_guess()
    exit()
