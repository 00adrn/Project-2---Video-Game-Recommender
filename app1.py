import sys
import os
import json

# --- Module and Path Setup ---
# 1. Determine the project root directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Add the 'backend' directory to the system path for module imports
backend_path = os.path.join(current_dir, 'backend')
if backend_path not in sys.path:
    sys.path.append(backend_path)

# 3. Define the path to the data and models
DATA_DIR = os.path.join(current_dir, "preprocessing", "data")

# 4. Import necessary modules
try:
    from backend.recommend import recommend_games
    from backend.utils import DataManager, Game # Game is needed to retrieve the name attribute
    from backend.knn import kNN
    
    # These external libraries are needed for data loading
    import pandas as pd
    import joblib
except ImportError as e:
    print(f"Error: Failed to import a module. Make sure your virtual environment is active and all libraries (pandas, joblib) are installed: {e}")
    sys.exit(1)


def setup_recommender():
    """
    Initializes the DataManager and kNN objects by loading all necessary files
    from the 'preprocessing/data' directory.
    """
    print("--- Initializing Recommender System (Loading data and models)...")
    
    # Data Files
    MAIN_DATA_FILE = os.path.join(DATA_DIR, "modified_games.json")
    VECTOR_DATA_FILE = os.path.join(DATA_DIR, "games_vectors.parquet") 
    
    # Model/Resource Files
    VECTORIZER_PATH = os.path.join(DATA_DIR, "tfidf_vectorizer.pkl")
    SVD_PATH = os.path.join(DATA_DIR, "svd_model.pkl")
    LEMMATIZER_PATH = os.path.join(DATA_DIR, "lemmatizer.pkl")
    STOP_WORDS_PATH = os.path.join(DATA_DIR, "stop_words.pkl")

    # 1. Initialize DataManager and load main data
    data_manager = DataManager()
    
    try:
        data_manager.setup(MAIN_DATA_FILE, VECTOR_DATA_FILE)
        print(f"DataManager loaded {len(data_manager.games)} games.")

        # Load Vector Data
        df_vectors = pd.read_parquet(VECTOR_DATA_FILE)
        data_manager.vec_data = df_vectors.values 
        print(f"Vector data loaded: Shape {data_manager.vec_data.shape}")

    except FileNotFoundError as e:
        print(f"ERROR: Data file not found. Please check the path and file: {e.filename}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: An error occurred during DataManager setup or vector loading: {e}")
        sys.exit(1)

    # 2. Initialize kNN Recommender
    knn_obj = None
    try:
        knn_obj = kNN(
            VECTORIZER_PATH, 
            SVD_PATH, 
            data_manager, 
            LEMMATIZER_PATH, 
            STOP_WORDS_PATH
        )
        print("kNN model initialized successfully.")
        
    except FileNotFoundError as e:
        print(f"ERROR: Model file not found. Please check the path and file: {e.filename}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: An error occurred initializing kNN model: {e}")
        sys.exit(1)

    print("--- Initialization complete. Ready for recommendations. ---")
    return knn_obj, data_manager


def get_user_input():
    """Prompts the user for all four inputs and validates them."""
    
    # 1. Input String (Game Name/Query)
    input_string = input("\nEnter game name or query (type 'exit' to quit): ").strip()
    if input_string.lower() == 'exit':
        return None, None, None, None
    if not input_string:
        print("Input cannot be empty. Please try again.")
        return get_user_input()

    # 2. Algorithm Choice (with validation)
    while True:
        algo_choice = input("Enter algorithm ('knn' or 'heuristic') [default: knn]: ").strip().lower()
        if not algo_choice:
            algo_choice = 'knn'
        if algo_choice in ['knn', 'heuristic']:
            algo_flag = 0 if algo_choice == 'knn' else 1
            break
        else:
            print("Invalid algorithm. Please enter 'knn' or 'heuristic'.")

    # 3. Number of Games (with default and validation)
    num_games = 20
    while True:
        num_games_input = input(f"Enter number of games to recommend [default: {num_games}]: ").strip()
        if not num_games_input:
            break
        try:
            num_games = int(num_games_input)
            if num_games > 0:
                break
            else:
                print("Number of games must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # 4. Sample Size (with default and validation)
    sample_size = 100000
    while True:
        sample_size_input = input(f"Enter sample size [default: {sample_size}]: ").strip()
        if not sample_size_input:
            break
        try:
            sample_size = int(sample_size_input)
            if sample_size > 0:
                break
            else:
                print("Sample size must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    return input_string, algo_flag, num_games, sample_size


def run_interactive_recommender():
    """
    Main function to initialize and run the interactive recommendation loop.
    """
    knn_obj, dm_obj = setup_recommender()

    # Main recommendation loop
    while True:
        input_string, algo_flag, num_games, sample_size = get_user_input()

        if input_string is None:
            print("\nExiting the recommender. Goodbye!")
            break

        print("\n" + "="*50)
        print(f"Running Recommendation:")
        print(f"Query: '{input_string}'")
        print(f"Algorithm: {'kNN' if algo_flag == 0 else 'Heuristic'} | Games: {num_games} | Sample Size: {sample_size}")
        print("="*50)
        
        try:
            # Call the main recommendation logic
            recommendation_indices = recommend_games(
                knn_obj=knn_obj,
                dm_obj=dm_obj,
                input_string=input_string,
                algo_type_flag=algo_flag,
                sample_size=sample_size,
                num_of_games_needed=num_games
            )
        except Exception as e:
            print(f"\nAn error occurred during recommendation: {e}")
            continue

        # Display Results
        if recommendation_indices:
            print(f"\n✅ Found {len(recommendation_indices)} Recommendations:")
            
            # Convert indices back to game names for a user-friendly output
            for i, index in enumerate(recommendation_indices):
                try:
                    # Assuming dm_obj.games is a list of Game objects with a 'name' attribute
                    game_name = dm_obj.games[index].name
                    print(f"  {i+1}. {game_name}")
                except (IndexError, AttributeError):
                    print(f"  {i+1}. [Error: Could not retrieve game name for index {index}]")
                
        else:
            print("❌ No recommendations found.")
        
        print("\n" + "-"*50)


if __name__ == "__main__":  
    run_interactive_recommender()