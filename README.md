# NimGame: Turn of Three

Welcome to **Turn of Three**, a number game where players take turns removing digits from a randomly generated number. The goal is to ensure that the sum of the remaining digits is divisible by 3. The game is powered by a Minimax algorithm that evaluates the best move for the computer.

## Table of Contents
* [Introduction](#introduction)
* [Rules](#rules)
* [Game Mechanics](#game-mechanics)
* [Files and Structure](#files-and-structure)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

## Introduction

**Turn of Three** is a simple game where a player or a computer removes digits from a large number. The objective is to make the sum of the remaining digits divisible by 3. If you can no longer do so, you lose!

The game is implemented using Python with a Minimax algorithm for the computer opponent, which ensures that the computer makes optimal moves.

## Rules

* A large number is randomly generated, and players take turns to remove one digit at a time.
* After each removal, the sum of the remaining digits must be divisible by 3.
* If the sum is not divisible by 3 after a player's turn, that player loses the game.

## Game Mechanics

* The computer player uses a **Minimax algorithm** to make optimal moves.
* The game ends when no further moves can be made or when the sum of the digits is no longer divisible by 3.

## Files and Structure

The project is structured into separate modules for better readability and maintainability:

```
/NimGame
│ 
├── nim_game.py          # Contains the core game logic and class definition for NimGame.
├── minimax_policy.py    # Contains the implementation of the Minimax policy with caching.
└── main.py              # Main execution script to run the game.
```

### File Descriptions

* **nim_game.py**: Defines the `NimGame` class, which handles game initialization, state transitions, and game rules.
* **minimax_policy.py**: Implements the Minimax algorithm with caching to improve the efficiency of computer decision-making.
* **main.py**: The entry point for running the game, where the player can interact with the computer and play.

## Installation

### Requirements

To run this game, ensure you have Python installed. You can install the required packages by running:

```bash
pip install -r requirements.txt
```

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/NimGame.git
   ```

2. Navigate to the project directory:
   ```bash
   cd NimGame
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once installed, you can start playing the game by running the `main.py` script:

```bash
python main.py
```

### Game Instructions

* At the start of the game, you will be prompted to decide who plays first, the computer or the human.
* During each turn, you will choose a digit to remove, and the computer will respond.
* The game ends when either the sum of the digits is no longer divisible by 3, or no more digits can be removed.

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for more details.
