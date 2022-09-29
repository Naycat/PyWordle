"""Scores Module
    """

from decimal import getcontext, Decimal
import config
import helper as h
import pickle

getcontext().prec = 2
demo_dict = config.demo_scores


class Scores:
    """
    Scores class

    A class that handles the game scores

    - saves game scores
    - loads game scores
    - updates game scores

    """

    def __init__(self, username, datasource={}):
        """Initialize class attributes"""
        self.username = username
        self.latest_n_tries = 0
        self.total_games = 0
        self.best_guess = 0
        self.total_wins = 0
        self.last_game_result = ""
        self.current_streak = 0
        self.best_streak = 0
        self.win_percentage = Decimal(0)
        self.guess_history = []
        self.path = "../data/"
        self.dict = datasource
        self.board = config.empty_scoreboard.copy()
        self.tries_percent = {}

    def save_scores_to_file(self, file=False):
        """Class method to save_scores
        to jason file or global variable
        """
        score_dict = {
            "username": self.username,
            "latest_n_tries": self.latest_n_tries,
            "last_game_result": self.last_game_result,
            "total_games": self.total_games,
            "best_guess": self.best_guess,
            "total_wins": self.total_wins,
            "current_streak": self.current_streak,
            "best_streak": self.best_streak,
            "win_percentage": self.win_percentage,
            "guess_history": self.guess_history
        }
        if file:
            # with open(f'{self.path}{self.username}.json', encoding="utf-8") as json_file:
            #     json.dump(score_dict, json_file, indent=4)
            with open('saved_dictionary.pkl', 'wb') as f:
                pickle.dump(score_dict, f)
        else:
            global demo_dict
            demo_dict = score_dict.copy()

    def load_score_dict_file(self, file=True):
        """Class method to load previously saved scores, ether from file or global variable"""
        if file:
            # with open(f'{self.path}{self.username}.json', 'r', encoding="utf-8") as score_file:
            #     score_data = json.load(score_file, indent=4)
            with open('saved_dictionary.pkl', 'rb') as f:
                score_data = pickle.load(f)
        else:
            score_data = self.dict

        self.username = score_data['username']
        self.latest_n_tries = score_data["latest_n_tries"]
        self.last_game_result = score_data['last_game_result']
        self.total_games = score_data['total_games']
        self.best_guess = score_data['best_guess']
        self.total_wins = score_data['total_wins']
        self.current_streak = score_data['current_streak']
        self.best_streak = score_data['best_streak']
        self.win_percentage = score_data['win_percentage']
        self.guess_history = score_data['guess_history']

    def calc_win_percentage(self):
        """method to calculate win percentage from total wins and games played"""
        self.win_percentage = Decimal(self.total_wins / self.total_games * 100)

    def end_of_game(self, gamedata: list):
        """method called at the end of a game to update the scores object"""
        self.total_games += 1
        self.latest_n_tries = gamedata[0]
        self.guess_history.append(self.latest_n_tries)
        self.best_guess = min(self.guess_history)
        self.last_game_result = gamedata[1]
        if self.last_game_result == "win":
            self.total_wins += 1
            self.current_streak += 1
            self.best_streak = max(self.current_streak, self.best_streak)
        else:
            self.current_streak = 0
        self.calc_win_percentage()

    def calc_format_try(self, try_number: int):
        try_percent = int(round(self.guess_history.count(
            try_number)/len(self.guess_history)*100))
        to_color = str(try_percent) + (" "*try_percent)
        return h.colorizer("green", str(to_color), True)

    def cal_tries(self):
        self.tries_percent = {
            "t1": self.calc_format_try(1),
            "t2": self.calc_format_try(2),
            "t3": self.calc_format_try(3),
            "t4": self.calc_format_try(4),
            "t5": self.calc_format_try(5),
            "t6": self.calc_format_try(6),
        }

    def draw_score_board(self):
        self.cal_tries()
        self.board.update(
            {"1": str(f"|     {self.total_games}         |    {self.total_wins}     |     {self.win_percentage}%    |\n+ --- + --- + --- + --- + --- +\n")})
        self.board.update(
            {"2": str(f"|     {self.best_guess}       |       {self.current_streak}       |      {self.best_streak}     |\n+ --- + --- + --- + --- + --- +\n")})
        self.board.update(
            {"t1": str(f"|#1 {self.tries_percent['t1']}\n+ --- + --- + --- + --- + --- +\n")})
        self.board.update(
            {"t2": str(f"|#2 {self.tries_percent['t2']}\n+ --- + --- + --- + --- + --- +\n")})
        self.board.update(
            {"t3": str(f"|#3 {self.tries_percent['t3']}\n+ --- + --- + --- + --- + --- +\n")})
        self.board.update(
            {"t4": str(f"|#4 {self.tries_percent['t4']}\n+ --- + --- + --- + --- + --- +\n")})
        self.board.update(
            {"t5": str(f"|#5 {self.tries_percent['t5']}\n+ --- + --- + --- + --- + --- +\n")})
        self.board.update(
            {"t6": str(f"|#6 {self.tries_percent['t6']}\n+ --- + --- + --- + --- + --- +\n")})
        print("".join(self.board.values()))

# TODO: these
    # def calc tries percentage
    # def draw tries
    # def show stats
