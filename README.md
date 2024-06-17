# GameInt

GameInt is a simple number guessing game implemented in Python. The objective of the game is to correctly guess a sequence of four numbers, each ranging from 1 to 6, within eight attempts. The game provides feedback after each guess, indicating which numbers were correctly guessed in the correct position.

How to Play
Start the Game: Run the script and enter your name when prompted. You will be greeted and given a brief introduction to the game.
Game Rules:
The game randomly generates a sequence of four numbers (each between 1 and 6).
You have up to eight attempts to guess the correct sequence.
After each guess, the game will display feedback to help you improve your next guess.
If you want to quit the game at any time, enter the sequence 0 0 0 0.
Feedback System:
The feedback consists of dots (.) and ones (1).
A 1 indicates that the corresponding number in your guess is correct and in the correct position.
A dot (.) indicates that the corresponding number is incorrect or not in the correct position.
Game Flow
Initialize Variables:

The game generates four random numbers between 1 and 6.
The sequence is stored in the variable numlist.
Prompt for Guesses:

The player is prompted to enter four numbers for each guess.
The input is validated to ensure it is a number between 1 and 6.
Evaluate Guess:

The game compares the player's guess to the generated sequence.
Feedback is provided for each number in the guess.
The player's points decrease with each incorrect guess.
End Game:

The game ends when the player correctly guesses the sequence, uses all eight attempts, or enters 0 0 0 0.
The player is prompted to play again or exit.
