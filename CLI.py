from backend.recommend import recommend_games
from backend.knn import kNN
from backend.utils import DataManager, align_text_with_window

def exit_the_program():
        print('\nThanks for using Recosteam! Exiting...')


DATA_DIR = "preprocessing/data/"
DEFAULT_SAMP_SIZE = 100000
DEFAULT_NUM_GAMES = 20

if __name__ == "__main__":
        #courtesy: https://patorjk.com/software/taag/
        print(r'''
        _____  ______ _____ ____   _____ _______ ______          __  __
        |  __ \|  ____/ ____/ __ \ / ____|__   __|  ____|   /\   |  \/  |
        | |__) | |__ | |   | |  | | (___    | |  | |__     /  \  | \  / |
        |  _  /|  __|| |   | |  | |\___ \   | |  |  __|   / /\ \ | |\/| |
        | | \ \| |___| |___| |__| |____) |  | |  | |____ / ____ \| |  | |
        |_|  \_\______\_____\____/|_____/   |_|  |______/_/    \_\_|  |_|
        ''')

        print(
               align_text_with_window(
              'Recosteam provides a simple command-line interface to get upto 10000 game recs or search for games sourced from our 100,000-' \
              'game dataset based on an input string you enter. You can provide the follwing parameters: number of games -- how many games you want' \
              ', and sample size -- which chooses those many games as our search base based on relevance metrics. Additionally,' \
              'you must provide a choice of algorithm, as guided by the prompt. We hope you\'ll find some new cool games! '
               )
             )

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
        
        print('All set!\n')
        while True:
                print('\nEnter input (ideally, a valid game name; 0000 for exit): ')
                input_name = input()
                if input_name == "0000":
                        exit_the_program()
                        break
                
                num_of_games = int()
                while True:
                        print('\nEnter number of games you want(enter 0 for default): ')
                        try:
                           num_of_games = int(input())
                        except:
                           print('Not a valid number of games. Enter an non-negative integer.')
                           continue
                        if(num_of_games >= 0):
                                if(num_of_games == 0):
                                        num_of_games = DEFAULT_NUM_GAMES
                                elif num_of_games > 10000:
                                      num_of_games = 10000
                                      print('Choice exceeded our limit. Defaulting to 10,000 games.')
                                break

                        print('Not a valid number of games. Enter an non-negative integer.')

                sample_size = int()
                while True:
                        print('\nEnter sample size from the dataset to consider(enter 0 for default): ')    
                        try:
                           sample_size = int(input())
                        except:
                           print('Not a valid sample size. Enter an non-negative integer.')
                           continue
                        if(sample_size >= 0):
                                if(sample_size == 0):
                                        sample_size = DEFAULT_SAMP_SIZE
                                elif sample_size < num_of_games:
                                      sample_size = int(min(1.4*num_of_games, 100000))
                                      print('Sample size is lesser than number of games needed; it has been set to around (1.4 * number_of_games). ')
                                break

                        print('Not a valid sample size. Enter an non-negative integer.')

                algo_code = int()
                while True:
                        print('\nEnter 0 for using k-nearest neighbors, 1 for our heuristic approach: ')    
                        try:
                           algo_code = int(input())
                        except:
                           print('Not a valid code. Enter either 0 or 1.')
                           continue
                        if algo_code == 0 or algo_code == 1:
                                break

                        print('Not a valid code. Enter either 0 or 1.')
   
                output = recommend_games(knn, dm, input_name, algo_code, sample_size, num_of_games)
                print('Games found: ')
                for i, game_idx in enumerate(output):
                        print('  '+ dm.games[game_idx].name)

