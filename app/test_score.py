import config
import scores as Scores
from helper import *
gscores = Scores.Scores
datadict = config.demo_scores
# with open('saved_dictionary.pkl', 'rb') as f:
# datadict2 = pickle.load(f)

if __name__ == '__main__':
    gamescore = gscores(username="demo", datasource=datadict)
    gamescore.load_score_dict_file(file=False)
    print(gamescore.dict)
    gamescore.draw_score_board()
    gamescore.save_scores_to_file(file=True)
