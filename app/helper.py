"""Helper functions"""
import urllib.request
import random

random.seed(42)
dictionay_path = "../data/wordl_dictionary.txt"

old_url = "https://raw.githubusercontent.com/fserb/pt-br/master/palavras"
new_url = "https://raw.githubusercontent.com/gusbemacbe/LanguagePortuguese/master/Portuguese%20(European%20-%20Before%20OA%201990).dic"


def update_word_dictionary(dictionary):
    count = 0
    with urllib.request.urlopen(new_url) as rfile:
        for line in rfile.readlines():
            word = line.decode().split()[0].split("/")[0].split()[0].strip()
            # print(word if word.isalpha() else "\n")
            if len(word) == 5 and word.isalpha() and word not in open(dictionary, 'r').read():
                with open(dictionary, 'a') as f:
                    count += 1
                    f.write(f'{word}\n')
                    print(word)
    print(count)


def validate_word(word: str):
    return word in open(dictionay_path, 'r').read()


def get_random_word():
    with open(dictionay_path, 'r') as dfile:
        words = dfile.readlines()
        rand_word = words[random.randrange(0, len(words))]
    return rand_word.strip()


def control_input(userinputs):
    check = validate_word(userinputs)
    while check is False:
        userinputs = input(
            "Check if you've inserted a valid 5 letter portuguese word and try again\n ")
        check = validate_word(userinputs)
    return userinputs.upper()


def green(letter): return f'\033[1;97;42m{letter}\033[00m'
def yellow(letter): return f'\033[1;97;43m{letter}\033[00m'
def grey(letter): return f'\033[1;97;100m{letter}\033[00m'


def colorizer(colorword: str, letter: str, keyboard=False):
    valid = ["green", "yellow", "grey"]
    letter = f"  {letter}  " if keyboard is False else f" {letter} "
    if colorword not in valid:
        raise ValueError(
            "Invalid color, must be one of the following: ", " ".join(valid))
    elif colorword == "green":
        return green(letter)
    elif colorword == "yellow":
        return yellow(letter)
    elif colorword == "grey":
        return grey(letter)
    else:
        return letter


def check_n_append(item, items: list):
    if item not in items:
        items.append(item)
    return items


def print_dict(dictionary):
    for key in dictionary.keys():
        print(dictionary[key])
