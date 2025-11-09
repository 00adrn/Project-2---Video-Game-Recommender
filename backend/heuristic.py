from collections import Counter

def heuristic_score(game, input_partial_score_table, freq_table):

    """
    1. have the frequency of each word found, across: name, tags, category and description.

    2. divide precalculated partial score of common word by frquency of the word
    """
    score = 0.0
    game_words = game.words
    for i in range(4):
        for word in game_words[i]:
            score += input_partial_score_table.get(word, 0) / freq_table.get(word, 1)

    return score

def heuristic_approach(input_game, num_games, data_man, sample_size = 100000, in_dataset=True):
    """
    Compare the input game against dataset games using a frequency-based heuristic.
    If two games have equal scores, preserve their original order in the dataset.
    """
    game_list = data_man.games[: sample_size]
    l = len(game_list)

    # Identify input game

    input_name = input_game.lower().strip()

    input_partial_scores = None
    if input_name in data_man.game_indices:
        # game is in dataset
        input_partial_scores = game_list[data_man.game_indices[input_name]].partial_score_table

    else:
        input_partial_scores = Counter()
        words = input_game.lower().split()
        for word in words:
            input_partial_scores[word] += 100.0

    # Compute heuristic score for each game
    for g in game_list:
        g.score = 0 #reset
        g.score = heuristic_score(g, input_partial_scores, data_man.freq_table)    #sum(1 / data_man.freq_table.get(w, 1) for w in overlap)

    ranked_games = sorted(game_list, key=lambda x: x.score, reverse=True)

    # exclude the input game itself
    return [data_man.game_indices[g.name.lower()] for g in ranked_games if g.name.lower() != input_name][:num_games]