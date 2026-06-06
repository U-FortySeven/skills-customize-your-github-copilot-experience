
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a console-based Hangman game in Python that lets a player guess letters to reveal a hidden word. This assignment focuses on string manipulation, control flow (loops and conditionals), and basic user input/output.

## 📝 Tasks

### 🛠️	Build the Hangman Game

#### Description
Implement a playable Hangman game that runs in the terminal. The program should select a secret word, accept single-letter input from the player, display progress, and track remaining attempts until the game ends.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display current progress using underscores for unknown letters (e.g., _ a _ _ m a n)
- Accept single-letter guesses (case-insensitive) and ignore repeated guesses
- Show letters already guessed
- Deduct an attempt for each incorrect guess and display attempts remaining
- End with a clear win message when the word is guessed or a lose message when attempts reach zero, revealing the secret word

Example interaction:

```
Progress: _ _ _ _ _
Guessed: a, e
Enter a letter: a
Progress: a _ _ _ _
Attempts left: 6
```

### 🛠️	Optional Enhancements

#### Description
Add optional features to improve gameplay and user experience.

#### Requirements
Completed program may include any of the following enhancements:

- Difficulty levels (adjust word length or attempts)
- Load words from a file such as `assignments/games-in-python/words.txt`
- Hint system that reveals a random letter
- Scoring or high-score persistence

