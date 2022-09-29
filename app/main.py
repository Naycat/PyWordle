"""PyWordle - Python implementation of the popular Wordle game engine
"""
from game import *
from scores import *
from helper import *
from game import PyWordle1982
################################################################

# Command line menu
# inputs user guess
# outputs hint
# 1 - one secret world and one try
# TODO: add background color to spaces surronding letters


def main():
    userinput = control_input(
        input("Let's start!\n Please enter your 5 letter guess!\n"))
    userguess = PyWordle1982(userinput)
    while userguess.current_try <= userguess.maxtries:
        userguess.check_guess()
    exit()


if __name__ == "__main__":
    main()
