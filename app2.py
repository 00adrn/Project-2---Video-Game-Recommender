from backend.recommend import recommend_games
from backend.knn import kNN
from backend.utils import DataManager

DATA_DIR = "preprocessing/data/"



if __name__ == "__main__":
        #courtesy: https://patorjk.com/software/taag/
        print('''
        _____  ______ _____ ____   _____ _______ ______          __  __
        |  __ \|  ____/ ____/ __ \ / ____|__   __|  ____|   /\   |  \/  |
        | |__) | |__ | |   | |  | | (___    | |  | |__     /  \  | \  / |
        |  _  /|  __|| |   | |  | |\___ \   | |  |  __|   / /\ \ | |\/| |
        | | \ \| |___| |___| |__| |____) |  | |  | |____ / ____ \| |  | |
        |_|  \_\______\_____\____/|_____/   |_|  |______/_/    \_\_|  |_|
        ''')

        print('\nLoading Data...')

        dm = DataManager()
        dm.setup(
                DATA_DIR + 'modified_games.json',
                DATA_DIR + 'games_vectors.parquet'
                )
        knn = kNN(
                DATA_DIR + 'tfidf_vectorizer.pkl', 
                DATA_DIR + 'svd_model.pkl',
                DATA_DIR + 'lemmatizer.pkl',
                DATA_DIR + 'stop_words.pkl', 
                dm
                )
        while True:
                print('Enter input: ')
                input_name = input()
                output = recommend_games(knn, dm, input_name, 0)
                for i, game_idx in enumerate(output):
                        print(dm.games[game_idx].name)
                        if i%5 == 4:
                                print()