from fastapi import FastAPI
import uvicorn

from backend.utils import DataManager
from backend.knn import kNN
from backend.heuristic import heuristic_approach

def recommend_games(knn_obj, dm_obj, input_string, algo_type_flag, sample_size = 100000, num_of_games_needed = 40):
     if algo_type_flag == 0:
          return knn_obj.knn_recommend(input_string, num_of_games_needed, sample_size )  
     elif algo_type_flag == 1:
          return heuristic_approach(input_string, num_of_games_needed, dm_obj, sample_size)

# -----------------------
# Setup DataManager
# -----------------------
dm = DataManager()
dm.setup(
    main_data_file='preprocessing/data/modified_games.json',
    vector_data_file='preprocessing/data/games_vectors.parquet'
)

# -----------------------
# Setup kNN Recommender
# -----------------------
knn = kNN(
    vectorizer='preprocessing/data/tfidf_vectorizer.pkl',
    svd='preprocessing/data/svd_model.pkl',
    data_man=dm,
    lemmatizer='preprocessing/data/lemmatizer.pkl',
    stop_words='preprocessing/data/stop_words.pkl'
)


app = FastAPI()

# recommend_games(knn, dm, input_string, algo_type_flag, sample_size, num_of_games_needed)


@app.get("/api/")
async def handle(gameName: str, algorithm: int, dataSize: int):
    if dataSize:
        print(f"gameName: {gameName}\nalgorithm: {algorithm}\ndataSize: {dataSize}")

    return recommend_games(knn, dm, gameName, algorithm, dataSize)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
