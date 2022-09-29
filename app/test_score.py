import pickle
import config
import scores as Scores
from helper import *
gscores = Scores.Scores
datadict = config.demo_scores
with open('saved_dictionary.pkl', 'rb') as f:
    datadict2 = pickle.load(f)

if __name__ == '__main__':
    gamescore = gscores(username="demo", datasource=datadict2)
    gamescore.load_score_dict_file(file=True)
    print(gamescore.dict)
    gamescore.end_of_game([2, "win"])
    gamescore.draw_score_board()
    gamescore.save_scores_to_file(file=True)
