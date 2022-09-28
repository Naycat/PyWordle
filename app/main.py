"""PyWordle - Python implementation of the popular Wordle game engine
"""
import urllib.request
################################################################

# Command line menu
# inputs user guess
# outputs hint
# 1 - one secret world and one try


def validate_word(word: str):
    url = "https://raw.githubusercontent.com/fserb/pt-br/master/palavras"
    lineword = word + "\n"
    dfile = urllib.request.urlopen(url)
    for line in dfile:
        if lineword.encode() == line and len(word) == 5:
            dfile.close()
            return True
    return False
# Main game class


def control_input(userinput):
    check = validate_word(userinput)
    while check == False:
        userinput = input(
            "Check if you've inserted a valid 5 letter portuguese word and try again\n ")
        check = validate_word(userinput)
    return userinput


def colorizer(colorword: str, letter: str):
    valid = ["green", "yellow", "grey"]
    if colorword not in valid:
        raise ValueError(
            "Invalid color, must be one of the following: ", " ".join(valid))
    elif colorword == "green":
        return str(f'\033[92m {letter}\033[00m')
    elif colorword == "yellow":
        return str(f'\033[93m {letter}\033[00m')
    elif colorword == "grey":
        return str(f'\033[90m {letter}\033[00m')
    else:
        return letter


# valid_words = []
keyboard_str = ", ---,---,---,---,---,---,---,---,---,---,---,---,---,-------,\n \
|1/2| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' | <-    |\n \
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|\n \
| ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     |\n \
|-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |\n \
| Caps | A | S | D | F | G | H | J | K | L | \\ | [ | * |    |\n \
|----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|\n \
|    | < | Z | X | C | V | B | N | M | , | . | - |          |\n \
|----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|\n \
| ctrl |  | alt |                          |altgr |  | ctrl |\n \
'------'  '-----'--------------------------'------'  '------\n"


# def printnewline(word):


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

    def create_hints(self):
        """
        creates a hint result list and updates used letters list
        """
        self.hint_result = []
        for i in range(5):
            if self.guess[i] in self.secretword:
                if self.guess[i] == self.secretword[i]:
                    self.right_letters.append(self.guess[i].upper())
                    self.hint_result.append(
                        colorizer("green", self.guess[i].upper()))
                else:
                    self.wrong_place.append(self.guess[i].upper())
                    self.hint_result.append(
                        colorizer("yellow", self.guess[i].upper()))
            else:
                self.not_in_word.append(self.guess[i].upper())
                self.hint_result.append(
                    colorizer("grey", self.guess[i].upper()))

    def print_and_save_hints(self):
        """Prints the hints to the terminal and shows used letters"""
        self.history += str(
            f"+ --- + --- + --- + --- + --- + \n | {self.hint_result[0]}  | {self.hint_result[1]}  | {self.hint_result[2]}  | {self.hint_result[3]}  | {self.hint_result[4]}  | \n + --- + --- + --- + --- + --- + \n")
        print(self.history)
        print("Letters in the right place: ", self.right_letters)
        print("Letters in the wrong place: ", self.wrong_place)
        print("Letters not in word: ", self.not_in_word)
        # for i in len(keyboard_str):
        #     if keyboard_str[i].isalpha():
        #         if keyboard_str in self.right_letters:
        #             keyboard_str.replace(
        #                 keyboard_str, colorizer("green", keyboard_str))
        #         elif keyboard_str[i] in self.wrong_place:
        #             keyboard_str.replace(
        #                 keyboard_str, colorizer("yellow", keyboard_str))
        #         elif keyboard_str[i] in self.not_in_word:
        #             keyboard_str.replace(
        #                 keyboard_str, colorizer("grey", keyboard_str))
        #     else:
        #         continue
        print(keyboard_str)

    def check_guess(self):
        while True:
            self.create_hints()
            self.print_and_save_hints()
            self.current_try += 1
            if self.guess == self.secretword:
                self.right_guess = True
                print("Acertaste!")
                exit()
                break
            elif self.current_try == self.maxtries:
                print("You didn't guess the right word. The answer was:",
                      self.secretword)
                exit()
                break
            else:
                self.guess = control_input(
                    input("Try again, write anotherword: \n"))

    # def game_history(self):

    # getting inputs
    # guess = input("Escreve a tua palavra")


if __name__ == "__main__":

    userinput = control_input(
        input("Let's start!\n Please enter your 5 letter guess!\n"))
    userguess = PyWordle1982(userinput)
    while userguess.current_try <= userguess.maxtries:
        userguess.check_guess()
    exit()
