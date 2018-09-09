from typing import List
from random import randint,random
import random, sys
import time
import requests

# Utility functions
def print_word_to_guess(letters: List) -> None:
    #Print the current word to guess
    print("Word to guess: {0}".format(" ".join(letters)))

def print_guesses_taken(current: int, total: int) -> None:
    #Print how many chances the player has used
    print("You are on guess {0}/{1}.".format(current, total))

def getword():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    word = (WORDS[randint(0,len(WORDS)-1)])
    word = str(word)
    print(word[2:-1].lower());
    wordLength = len(word[2:-1].lower())

    return(word[2:-1].lower())


#use of a tuple because words will not change
# wordList = (
# "bowl", "power", "window", "computer", "phone", "juice", "macbook", "desktop",
# "laptop", "dog", "cat", "lemon", "cable", "mirror", "hat", "spoon", "spongebob",
# "squidward", "patrick"
#        )

guess_word = []
# randomly choose single word from the list
secret_word = getword();
#make a variable for the length of the chosen word
alphabet = "abcdefghijklmnopqrstuvwxyz"
#form empty mutable list to store guessed letters
letter_storage = []

wordLength = len(secret_word)



def word_description():

    # print blanks for each letter in secret word
    for character in secret_word:
        guess_word.append("_ ")

    print("The word you must guess has", wordLength, "characters")

    print("You may only enter 1 letter from a-z\n\n")

    print_word_to_guess(guess_word)

def guessing():
    #Main game loop to have user guess letters and show results
    guess_taken = 1
    MAX_GUESS = 7
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Pick a letter\n").lower()
        if not guess in alphabet: #check input
            print("Enter a letter from a-z")
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
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 7:
                    print(" Sorry you lost! The secret word was {0}.".format(secret_word))

#main function to call the others
def spaceman():

    word_description();
    guessing();

# run the game
spaceman();
