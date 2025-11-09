from knn import kNN
from heuristic import heuristic_approach

def recommend_games(knn_obj, dm_obj, input_string, algo_type_flag, sample_size = 100000, num_of_games_needed = 20):
     if algo_type_flag == 0:
          return knn_obj.knn_recommend(input_string, input_string, num_of_games_needed, sample_size )  
     elif algo_type_flag == 1:
          return heuristic_approach(input_string, num_of_games_needed, sample_size)