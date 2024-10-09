import random

class NimGame:
    """
    A class representing the Nim Game where players remove digits and aim to 
    make the sum of the remaining digits divisible by 3.
    """
    
    def __init__(self):
        """
        Initializes the game with a random number where the sum of the digits is divisible by 3.
        """
        while True:
            num = random.randint(1000, 1000000)
            if self.sum_up(num) % 3 == 0:
                break
        self.n = num

    def startState(self):
        """
        Returns the initial game state.
        """
        return self.n

    def isEnd(self, state):
        """
        Checks if the game is in an end state.
        """
        return self.sum_up(state) % 3 != 0 or state == -1

    def utility(self, state, player):
        """
        Evaluates the utility of the current game state for a given player.
        """
        if self.sum_up(state) % 3 != 0:
            return float('+inf') if player == 1 else float('-inf')
        if state == -1:
            return float('-inf') if player == 1 else float('+inf')

    def actions(self, state):
        """
        Returns the possible actions for a given state (digits that can be removed).
        """
        return list(str(state))

    def successor(self, state, action):
        """
        Returns the next state after applying the given action (digit removal).
        """
        s = str(state).replace(str(action), '', 1)
        return -1 if s == '' else int(s)

    def sum_up(self, state):
        """
        Calculates the sum of the digits of the given state.
        """
        return sum(int(digit) for digit in str(state))
