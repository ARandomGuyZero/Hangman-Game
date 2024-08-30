"""
Hangman Game

Author: Alan
Date: August 25th 2024

This is a simple implementation of the classic Hangman game. 
The player tries to guess the letters in a hidden word, with a limited number of lives. 
The game ends when the player either correctly guesses all the letters or runs out of lives.
"""

import random
import hangman_words
import hangman_art

# Choose a random word from the word list
chosen_word = random.choice(hangman_words.word_list)
lives = 6

# Display the game logo
print(hangman_art.logo)

# Uncomment the line below if you want to see the word for debugging purposes
# print(chosen_word)

# Initialize the placeholder with underscores for each letter in the chosen word
placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)

# Game state variables
game_over = False
correct_letters = []

# Main game loop
while not game_over:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    
    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Display variable to update the guessed word
    display = ""

    # Check if the player has already guessed the letter
    if guess in correct_letters:
        print(f"You have already tried {guess}!")
    else:
        # Update the display with correct guesses
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
    
    # Show the current state of the word
    print("Word to guess: " + display)

    # Check if the guess is incorrect
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        # Check if the player has run out of lives
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # Check if the player has guessed the word
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Display the current hangman art based on remaining lives
    print(hangman_art.stages[lives])
