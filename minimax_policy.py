cache = {}

def minimaxPolicy(game, state, player):
    """
    Implements the Minimax policy for the Nim Game with caching for improved performance.
    """

    def recurse(state, player):
        if game.isEnd(state):
            return (game.utility(state, player), None)
        if (state, player) in cache:
            return cache[(state, player)]

        # Evaluate all possible actions and their corresponding values
        choices = [(recurse(game.successor(state, action), -player)[0], action) 
                   for action in game.actions(state)]

        # Choose the best option based on the current player
        val = max(choices) if player == 1 else min(choices)
        cache[(state, player)] = val
        return val

    value, action = recurse(state, player)
    return value, action
