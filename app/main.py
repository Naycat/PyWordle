"""PyWordle - Python implementation of the popular Wordle game engine
"""
import game as Game
import scores as Scores
from helper import *
import pickle
gengine = Game.PyWordle1982
gscores = Scores.Scores
with open('saved_dictionary.pkl', 'rb') as f:
    datadict = pickle.load(f)
# datadict = config.demo_scores

################################################################
# Command line menu
# inputs user guess
# outputs hint
# 1 - one secret world and one try
# TODO: add background color to spaces surronding letters
################################################################


def main():
    play_on = True if input(
        "Do you  want to play Wordle1982?") == "y" else False
    while play_on:
        gamescore = gscores(username="demo")
        gamescore.load_score_dict_file()
        userinput = control_input(
            input("Let's start!\n Please enter your 5 letter guess!\n"))
        userguess = gengine(userinput)
        while userguess.current_try <= userguess.maxtries:
            userguess.check_guess()
            gamescore.end_of_game(userguess.on_game_end())
            gamescore.draw_score_board()
            gamescore.save_scores_to_file(file=True)
            play_on = True if input(
                "Do you  want to play Again?") == "y" else exit()
            userinput = control_input(
                input("Let's start!\n Please enter your 5 letter guess!\n"))
            userguess = gengine(userinput)
            if play_on == False:
                exit()
                break

        if play_on == False:
            exit()
            break


if __name__ == "__main__":
    main()
