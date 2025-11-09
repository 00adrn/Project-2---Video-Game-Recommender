<<<<<<< HEAD
import numpy as np
import json
from collections import Counter
import pandas as pd
import re

class TextProcessor:
    """Utility class for cleaning and tokenizing text."""
    # A standard list of common English stop words
    # Added "game" and "is" which are often too frequent to be meaningful features
    STOP_WORDS = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in',
        'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the',
        'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will',
        'with', 'can', 'one', 'use', 'from', 'also', 'game', 'playing', 'you', 'your',
        'like', 'play', 'ever', 'enjoy',

        # Extended common English stop words
        'about', 'above', 'across', 'after', 'against', 'all', 'almost', 'alone',
        'along', 'among', 'around', 'because', 'before', 'behind', 'below',
        'beneath', 'besides', 'between', 'beyond', 'both', 'down', 'during',
        'each', 'either', 'enough', 'every', 'everyone', 'everything', 'everywhere',
        'except', 'few', 'follow', 'following', 'gets', 'go', 'goes', 'had', 'has',
        'have', 'hence', 'here', 'how', 'however', 'i', 'ie', 'into', 'its',
        'just', 'made', 'make', 'may', 'me', 'might', 'more', 'most', 'much',
        'must', 'my', 'myself', 'near', 'next', 'nor', 'now', 'off', 'once',
        'only', 'other', 'otherwise', 'our', 'out', 'over', 'own', 'same', 'say',
        'see', 'seem', 'seems', 'several', 'shall', 'she', 'should', 'since',
        'so', 'some', 'something', 'sometime', 'sometimes', 'somewhere', 'still',
        'such', 'take', 'than', 'thank', 'thanks', 'too', 'under', 'up', 'upon',
        'us', 'very', 'want', 'well', 'what', 'whatever', 'when', 'where', 'whether',
        'which', 'while', 'who', 'whoever', 'whom', 'whose', 'why', 'within',
        'without', 'would', 'yes', 'yet', 'we', 'weve', 'itll', 'id', 'weve',

        # Game/Description specific low-value terms
        'experience', 'adventure', 'world', 'story', 'time', 'new', 'old', 'best',
        'better', 'action', 'explore', 'discover', 'unique', 'epic', 'amazing',
        'simple', 'fun', 'puzzle', 'rpg', 'fps', 'mmo', 'multiplayer', 'singleplayer',
        'mode', 'pc', 'steam', 'official', 'original', 'version', 'free', 'buy',
        'release', 'now', 'today', 'get', 'got', 'look', 'looking', 'find', 'found',
        'come', 'coming', 'features', 'level', 'levels', 'chapter', 'mission',
        'musthave'
    }

    @staticmethod
    def clean_and_tokenize(text, remove_stop_words=True):
        """
        1. Convert to lowercase.
        2. Remove punctuation and split into tokens.
        3. Remove common English stop words.
        """
        # Convert to lowercase and replace all non-word characters (including punctuation) with a space
        text = text.lower()
        # Use re.findall to extract contiguous sequences of letters/numbers (tokens)
        tokens = re.findall(r'[a-z0-9]+', text)

        if remove_stop_words:
            # Filter out stop words
            tokens = [token for token in tokens if token not in TextProcessor.STOP_WORDS]

        return tokens


class Game:
    def __init__(self, game_data):
        self.score = 0

        self.name = game_data.get("name", "")
        self.recs = game_data.get("recommendations", 0)
        self.pos = game_data.get("positive", 0)
        self.neg = game_data.get("negative", 0)

        tags = game_data.get("tags", {})
        self.tags = list(tags.keys()) if isinstance(tags, dict) else tags
        self.cats = game_data.get("categories", [])
        self.desc = game_data.get("short_description", "")

        # Build sets and word collections
        self.partial_score_table = dict()

        name_words = TextProcessor.clean_and_tokenize(self.name, remove_stop_words=True)
        desc_words = TextProcessor.clean_and_tokenize(self.desc, remove_stop_words=True)
        tag_words = [t.lower() for t in self.tags]
        cat_words = [c.lower() for c in self.cats]

        self.words = [
            name_words,      # Cleaned name words
            desc_words,      # Cleaned description words
            tag_words,       # Tag words (lowercase only)
            cat_words        # Category words (lowercase only)
        ]


        self.create_partial_score_table()

    def create_partial_score_table(self):
        """
        the partial(non-frequency weighted) score each word based on this heuristic:
        sum of (handpicked number for category word is in(say name) and an additional
        weight from popularity(say number of recommendations)

        """
        weights = [4, 3, 0.2, 8]
        for i in range(4):
            names = self.words[i]
            for name in names:
                if name not in self.partial_score_table:
                    self.partial_score_table[name] = self.recs / 15
                self.partial_score_table[name] += weights[i]




class DataManager:
    def __init__(self):
        self.games = []
        self.game_indices = {}
        self.freq_table = Counter()

        self.vec_data = None

    def setup(self, main_data_file, vector_data_file):
        """Load dataset and populate games, indices, and frequency table."""
        with open(main_data_file, 'r', encoding='utf-8') as f:
            dataset = json.load(f)

        for i, (app_id, raw_game) in enumerate(dataset.items()):
            game = Game(raw_game)
            name_key = game.name.lower()

            self.games.append(game)
            self.game_indices[name_key] = i

            # update freq
            for s in game.partial_score_table.keys():
              self.freq_table.update([s])


        self.load_vectors(vector_data_file)

    def load_vectors(self, file):
      self.vec_data = pd.read_parquet(file).values
=======
import numpy as np
import json
from collections import Counter
import pandas as pd
import re

class TextProcessor:
    """Utility class for cleaning and tokenizing text."""
    # A standard list of common English stop words
    # Added "game" and "is" which are often too frequent to be meaningful features
    STOP_WORDS = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in',
        'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the',
        'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will',
        'with', 'can', 'one', 'use', 'from', 'also', 'game', 'playing', 'you', 'your',
        'like', 'play', 'ever', 'enjoy',

        # Extended common English stop words
        'about', 'above', 'across', 'after', 'against', 'all', 'almost', 'alone',
        'along', 'among', 'around', 'because', 'before', 'behind', 'below',
        'beneath', 'besides', 'between', 'beyond', 'both', 'down', 'during',
        'each', 'either', 'enough', 'every', 'everyone', 'everything', 'everywhere',
        'except', 'few', 'follow', 'following', 'gets', 'go', 'goes', 'had', 'has',
        'have', 'hence', 'here', 'how', 'however', 'i', 'ie', 'into', 'its',
        'just', 'made', 'make', 'may', 'me', 'might', 'more', 'most', 'much',
        'must', 'my', 'myself', 'near', 'next', 'nor', 'now', 'off', 'once',
        'only', 'other', 'otherwise', 'our', 'out', 'over', 'own', 'same', 'say',
        'see', 'seem', 'seems', 'several', 'shall', 'she', 'should', 'since',
        'so', 'some', 'something', 'sometime', 'sometimes', 'somewhere', 'still',
        'such', 'take', 'than', 'thank', 'thanks', 'too', 'under', 'up', 'upon',
        'us', 'very', 'want', 'well', 'what', 'whatever', 'when', 'where', 'whether',
        'which', 'while', 'who', 'whoever', 'whom', 'whose', 'why', 'within',
        'without', 'would', 'yes', 'yet', 'we', 'weve', 'itll', 'id', 'weve',

        # Game/Description specific low-value terms
        'experience', 'adventure', 'world', 'story', 'time', 'new', 'old', 'best',
        'better', 'action', 'explore', 'discover', 'unique', 'epic', 'amazing',
        'simple', 'fun', 'puzzle', 'rpg', 'fps', 'mmo', 'multiplayer', 'singleplayer',
        'mode', 'pc', 'steam', 'official', 'original', 'version', 'free', 'buy',
        'release', 'now', 'today', 'get', 'got', 'look', 'looking', 'find', 'found',
        'come', 'coming', 'features', 'level', 'levels', 'chapter', 'mission',
        'musthave'
    }

    @staticmethod
    def clean_and_tokenize(text, remove_stop_words=True):
        """
        1. Convert to lowercase.
        2. Remove punctuation and split into tokens.
        3. Remove common English stop words.
        """
        # Convert to lowercase and replace all non-word characters (including punctuation) with a space
        text = text.lower()
        # Use re.findall to extract contiguous sequences of letters/numbers (tokens)
        tokens = re.findall(r'[a-z0-9]+', text)

        if remove_stop_words:
            # Filter out stop words
            tokens = [token for token in tokens if token not in TextProcessor.STOP_WORDS]

        return tokens


class Game:
    def __init__(self, game_data):
        self.score = 0

        self.name = game_data.get("name", "")
        self.recs = game_data.get("recommendations", 0)
        self.pos = game_data.get("positive", 0)
        self.neg = game_data.get("negative", 0)

        tags = game_data.get("tags", {})
        self.tags = list(tags.keys()) if isinstance(tags, dict) else tags
        self.cats = game_data.get("categories", [])
        self.desc = game_data.get("short_description", "")

        # Build sets and word collections
        self.partial_score_table = dict()

        name_words = TextProcessor.clean_and_tokenize(self.name, remove_stop_words=True)
        desc_words = TextProcessor.clean_and_tokenize(self.desc, remove_stop_words=True)
        tag_words = [t.lower() for t in self.tags]
        cat_words = [c.lower() for c in self.cats]

        self.words = [
            name_words,      # Cleaned name words
            desc_words,      # Cleaned description words
            tag_words,       # Tag words (lowercase only)
            cat_words        # Category words (lowercase only)
        ]


        self.create_partial_score_table()

    def create_partial_score_table(self):
        """
        the partial(non-frequency weighted) score each word based on this heuristic:
        sum of (handpicked number for category word is in(say name) and an additional
        weight from popularity(say number of recommendations)

        """
        weights = [4, 3, 0.2, 8]
        for i in range(4):
            names = self.words[i]
            for name in names:
                if name not in self.partial_score_table:
                    self.partial_score_table[name] = self.recs / 15
                self.partial_score_table[name] += weights[i]




class DataManager:
    def __init__(self):
        self.games = []
        self.game_indices = {}
        self.freq_table = Counter()

        self.vec_data = None

    def setup(self, main_data_file, vector_data_file):
        """Load dataset and populate games, indices, and frequency table."""
        with open(main_data_file, 'r', encoding='utf-8') as f:
            dataset = json.load(f)

        for i, (app_id, raw_game) in enumerate(dataset.items()):
            game = Game(raw_game)
            name_key = game.name.lower().strip()

            self.games.append(game)
            self.game_indices[name_key] = i

            # update freq
            for s in game.partial_score_table.keys():
              self.freq_table.update([s])


        self.load_vectors(vector_data_file)

    def load_vectors(self, file):
      self.vec_data = pd.read_parquet(file).values
>>>>>>> 8fadc3d401e1997f8886fca67a99cb8509280cdb
