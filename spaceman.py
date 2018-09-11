from typing import List
from random import randint,random
import random, sys
import time
import requests

# this will shuffle random the same way each time so the word is the same with each run
# random.seed(3)

# Utility functions
def print_word_to_guess(letters: List) -> None:
    #Print the current word to guess
    print("Word to guess: {0}".format(" ".join(letters)))

def print_guesses_taken(current: int, total: int) -> None:
    #Print how many chances the player has used
    print("You are on guess {0}/{1}.".format(current, total))

def get_word():

    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    #pull down content from website
    response = requests.get(word_site)

    #split word list up for other functions
    WORDS = response.content.splitlines()

    #randomly select word
    word = (WORDS[randint(0,len(WORDS)-1)])
    word = str(word)
    # wordLength = len(word[2:-1].lower())

    return(word[2:-1].lower())


#give user info about the word and the game rules
def word_description(guess_word,secret_word):

    # print blanks for each letter in secret word
    for character in secret_word:
        guess_word.append("_ ")

    print("The word you must guess has", len(secret_word), "characters")
    print("You may only enter 1 letter from a-z\n\n")

    print_word_to_guess(guess_word)

#Main game loop to have user guess letters and show results
def guessing(guess_word,secret_word):

    #Declare Variables
    #form empty mutable list to store guessed letters
    letter_storage = []

    guess_taken = 1
    MAX_GUESS = 7

    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Pick a letter\n").lower()
        if not guess.isalpha(): #check input
            print("Enter a letter from a-z")

        elif guess in letter_storage: #check if letter has been already used
            print("You have already guessed that letter!")

        else:
            letter_storage.append(guess)
            if guess in secret_word:
                print("You guessed correctly!")
                #iterate through the secret word to fill in correctly guessed letters
                for i in range(0, len(secret_word)):
                    if secret_word[i] == guess:
                        guess_word[i] = guess

                #print to show the user their progress
                print_word_to_guess(guess_word)
                print_guesses_taken(guess_taken, MAX_GUESS)

                #see if there are no more underscores to see if user has guessed whole word
                if not '_ ' in guess_word:
                    print("You won!")
                    break

            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1

                #print to show the user their progress
                print_guesses_taken(guess_taken, MAX_GUESS)
                print_word_to_guess(guess_word)

                #check guess count to see if user has lost
                if guess_taken == 7:
                    print(" Sorry you lost! The secret word was {0}.".format(secret_word))

#main function to call the others
def spaceman():
    #initialize variables
    guess_word = []
    # randomly choose single word from the list

    secret_word = get_word();
    #make a variable for the length of the chosen word

    word_description(guess_word,secret_word);
    guessing(guess_word,secret_word);

# run the game
spaceman();
