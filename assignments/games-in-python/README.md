# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. You will practice tracking game state, revealing letters in a hidden word, and handling win and lose conditions.

## 📝 Tasks

### 🛠️ Set Up the Word List and Game State

#### Description
Create the data needed to run the game, including a list of possible secret words, a randomly selected target word, and variables for guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Select a secret word at random from a predefined list
- Store the letters the player has already guessed
- Track how many incorrect guesses remain
- Display the hidden word using underscores for unguessed letters


### 🛠️ Build the Guessing Loop

#### Description
Implement the main game loop that asks the player for letter guesses, checks whether each guess is correct, updates the displayed word, and ends the game when the player wins or loses.

#### Requirements
Completed program should:

- Prompt the player to enter one letter per turn
- Reveal correctly guessed letters in the word display
- Decrease remaining attempts after incorrect guesses
- Handle repeated guesses without breaking the game
- Show a clear win message when the word is guessed
- Show a clear lose message when attempts run out
