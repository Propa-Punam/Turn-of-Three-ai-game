from nim_game import NimGame
from minimax_policy import minimaxPolicy

if __name__ == "__main__":
    print("Welcome to the Turn of Three Game.")
    print("Choose a digit from the given number such that the sum of remaining digits is divisible by 3.")
    
    while True:
        ready = input("Let's Play! Press n/N to exit or anything else to continue: ")
        if ready.lower() == 'n':
            break

        game = NimGame()
        state = game.startState()

        turn = ''
        while turn not in ['i', 'c']:
            turn = input("Decide who will go first. Press 'c' for computer or 'i' for human: ")

        if turn == 'c':
            # Computer starts the game
            while game.sum_up(state) % 3 == 0 and state != -1:
                print(f"Current state: {state}")
                val, act = minimaxPolicy(game, state, 1)
                state = game.successor(state, act)
                print(f"Computer chose digit: {act}")
                print(f"Computer moves state to: {state}")
                
                if game.isEnd(state):
                    print("You won!" if game.sum_up(state) % 3 != 0 else "You lost!")
                    break
                
                action = -1
                while str(action) not in str(state):
                    action = int(input(f"Choose a digit from: {state}: "))
                state = game.successor(state, action)
                
                if game.isEnd(state):
                    print("You lost!" if game.sum_up(state) % 3 != 0 else "You won!")
                    break

        elif turn == 'i':
            # Human starts the game
            while game.sum_up(state) % 3 == 0 and state != -1:
                action = -1
                print(f"Current state: {state}")
                while str(action) not in str(state):
                    action = int(input(f"Choose a digit from: {state}: "))
                state = game.successor(state, action)
                
                if game.isEnd(state):
                    print("You lost!" if game.sum_up(state) % 3 != 0 else "You won!")
                    break

                print(f"Current state: {state}")
                val, act = minimaxPolicy(game, state, 1)
                state = game.successor(state, act)
                print(f"Computer chose digit: {act}")
                print(f"Computer moves state to: {state}")

                if game.isEnd(state):
                    print("You won!" if game.sum_up(state) % 3 != 0 else "You lost!")
                    break

    print("Goodbye!")
