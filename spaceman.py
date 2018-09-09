import random, sys
from typing import List


# Utility functions
def print_word_to_guess(letters: List) -> None:
    #Print the current word to guess
    print("Word to guess: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int) -> None:
    #Print how many chances the player has used
    print("You are on guess {0}/{1}.".format(current, total))


#use of a tuple because words will not change
wordList = (
"bowl", "power", "window", "computer", "phone", "juice", "macbook", "desktop",
"laptop", "dog", "cat", "lemon", "cable", "mirror", "hat"
       )

guess_word = []
# randomly choose single word from the list
secret_word = random.choice(wordList)
#make a variable for the length of the chosen word
wordLength = len(secret_word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
#form empty mutable list to store guessed letters
letter_storage = []

def word_description():

    # print blanks for each letter in secret word
    for character in secret_word:
        guess_word.append("_ ")

    print("The word you must guess has", wordLength, "characters")

    print("You may only enter 1 letter from a-z\n\n")

    print_word_to_guess(guess_word)


    #user guesses a letters

def guessing():

    #Main game loop to have user guess letters and show results

    guess_taken = 1
    MAX_GUESS = 7
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Pick a letter\n").lower()
        if not guess in alphabet: #check input
            print("Enter a letter from a-z ALPHABET")
        elif guess in letter_storage: #checkif letter has been already used
            print("You have already guessed that letter!")
        else:
            letter_storage.append(guess)
            if guess in secret_word:
                print("You guessed correctly!")
                for i in range(0, wordLength):
                    if secret_word[i] == guess:
                        guess_word[i] = guess
                print_word_to_guess(guess_word)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if not '_ ' in guess_word:
                    print("You won!")
                    print("Game Over!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 10:
                    print(" Sorry you lost! The secret word was {0}".format(SECRET_WORD))

# run the game
def spaceman():

    word_description();
    guessing();


spaceman();
