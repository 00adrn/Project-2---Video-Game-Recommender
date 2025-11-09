import numpy as np
import joblib
import re


class kNN:
    def __init__(self, vectorizer, svd, data_man, lemmatizer, stop_words):
        """
        Initialize the kNN recommender with pre-trained vectorizer, SVD, and resources.
        """
        self.vectorizer = joblib.load(vectorizer)
        self.svd = joblib.load(svd)
        self.lemmatizer = joblib.load(lemmatizer)
        self.stop_words = joblib.load(stop_words)

        # Reference to DataManager (contains games, indices, and vector data)
        self.dm = data_man

    def clean_text(self, text):
        """
        Normalize text: lowercase, remove punctuation, lemmatize, and remove stop words.
        Mirrors preprocessing used in training.
        """
        text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
        tokens = text.split()
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words]
        return ' '.join(tokens)

    def preprocess_query(self, query_text):
        """
        Converts raw query text into a reduced-dimensionality vector
        consistent with the trained TF-IDF + SVD pipeline.
        """
        clean_query = self.clean_text(query_text)

        # Build a pseudo-document approximating a game’s structure
        text_parts = [query_text.lower()] * 3
        text_parts.append(clean_query * 3)
        text_parts.extend([clean_query] * 10)
        full_text = ' '.join(text_parts)

        # TF-IDF vectorization
        tfidf_vec = self.vectorizer.transform([full_text])

        # Dimensionality reduction (SVD)
        reduced_vec = self.svd.transform(tfidf_vec)

        return reduced_vec[0]

    @staticmethod
    def cosine_similarity(vec1, vec2):
        """Compute cosine similarity between two vectors."""
        mag1, mag2 = np.linalg.norm(vec1), np.linalg.norm(vec2)
        if mag1 == 0.0 or mag2 == 0.0:
            return 0.0
        return np.dot(vec1, vec2) / (mag1 * mag2)

    def knn_recommend(self, input_word, num_of_games, sample_size=100000):
        """
        Recommend games similar to the input game/query using cosine similarity.
        """
        # Normalize input
        input_name_key = input_word.lower().strip()

        # Check if the input game already exists in the dataset
        in_dataset = input_name_key in self.dm.game_indices

        # Use the existing vector or generate a new one
        if in_dataset:
            idx = self.dm.game_indices[input_name_key]
            query_vector = self.dm.vec_data[idx]
        else:
            query_vector = self.preprocess_query(input_word)

        # Limit to a subset of the dataset for speed
        X_search = self.dm.vec_data[:sample_size]

        # Compute cosine similarities to all games
        similarities = []
        for i in range(X_search.shape[0]):
            sim = self.cosine_similarity(query_vector, X_search[i])
            similarities.append((sim, i))

        # Sort by similarity descending
        similarities.sort(key=lambda x: x[0], reverse=True)

        # Collect top recommendations
        recommendations = []
        for sim, idx in similarities:
            game_name = self.dm.games[idx].name
            # Skip the same game if it exists in dataset
            if in_dataset and game_name.lower().strip() == input_name_key:
                continue
            recommendations.append(game_name)
            if len(recommendations) >= num_of_games:
                break

        return recommendations