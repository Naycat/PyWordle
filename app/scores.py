
class Scores:

    def __init__(self, username, ntries: int, won: bool):
        self.username = username
        self.ntries = ntries
        self.won = won
        self.total_games = None
        self.best_try = None
        self.games_won = None
        self.current_streak = None
        self.best_streak = 0
        self.current_streak = 0
        self.win_percentage = 0
