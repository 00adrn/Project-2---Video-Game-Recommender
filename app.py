from fastapi import FastAPI
import uvicorn

from backend.utils import DataManager
from backend.knn import kNN
from backend.recommend import recommend_games

# -----------------------
# Setup DataManager
# -----------------------
dm = DataManager()
dm.setup(
    main_data_file='preprocessing/modified_games.json',
    vector_data_file='preprocessing/games_vectors.parquet'
)

# -----------------------
# Setup kNN Recommender
# -----------------------
knn = kNN(
    vectorizer='preprocessing/tfidf_vectorizer.pkl',
    svd='preprocessing/svd_model.pkl',
    data_man=dm,
    lemmatizer='preprocessing/lemmatizer.pkl',
    stop_words='preprocessing/stop_words.pkl'
)


app = FastAPI()

recommend_games(knn, dm, input_string, algo_type_flag, sample_size, num_of_games_needed)




# def func1():
#     return [0, 516, 5, 200, 323, 720]

@app.get("/")
def root():
    return func1()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# results = predict(input_string, in_dataset = True)

##show to user
