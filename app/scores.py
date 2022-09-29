

import json


class Scores:

    def __init__(self, username, ntries: int, won: bool, total_games=0, best_try=0, games_won=0, current_streak=0, best_streak=0, win_percentage=0, try_history=[]):
        self.username = username
        self.ntries = ntries
        self.won = won
        self.total_games = total_games
        self.best_try = best_try
        self.games_won = games_won
        self.current_streak = current_streak
        self.best_streak = best_streak
        self.win_percentage = win_percentage
        self.try_history = try_history
        self.path = "../data/"

    def save_scores(self):
        score_dict = {
            "username": self.username,
            "last_tries": self.ntries,
            "last_game_result": "win" if self.won else "lost",
            "total_games_played": self.total_games,
            "best_guess": self.best_try,
            "total_won": self.games_won,
            "current_streak": self.current_streak,
            "best_streak": self.best_streak,
            "win_percentage": self.win_percentage
        }

        with open(f'{self.path}{self.username}.json', 'w') as json_file:
            json.dump(score_dict, json_file, indent=4)

    def load_score_dict(self):
        with open(f'{self.path}{self.username}.json', 'r') as score_file:
            score_data = json.load(score_file, indent=4)
            self.username = score_data['username']
            # "last_tries": self.ntries,
            # "last_game_result": "win" if self.won else "lost",
            # "total_games_played": self.total_games,
            # "best_guess": self.best_try,
            # "total_won": self.games_won,
            # "current_streak": self.current_streak,
            # "best_streak": self.best_streak,
            # "win_percentage": self.win_percentage

    def calc_win_percentage(self):
        self.win_percentage = self.games_won / self.total_games * 100

    def end_of_game(self):
        self.total_games += 1
        self.try_history.append(self.ntries)
        self.best_try = min(self.try_history)
        if self.won:
            self.games_won += 1
            self.current_streak += 1
            self.best_streak = max(self.current_streak, self.best_streak)
        else:
            self.current_streak = 0
        self.calc_win_percentage()
    # def calc tries percentage
    # def draw tries
    # def show stats
