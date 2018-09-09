import random


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

    print(guess_word)


    #user guesses a letters
def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = input("Choose a letter\n").lower()

        if not guess in alphabet: #check input
            print("Enter a letter from a-z")
        elif guess in letter_storage: #check if letter has been already used
            print("You have already guessed that letter!")
        else:

            letter_storage.append(guess)
            if guess in secret_word:
                print("Your guess was correct!")
                #loop through each character in secret_word and compare it to the guess letter
                for x in range(0, wordLength):
                    if secret_word[x] == guess:
                        guess_word[x] = guess
                    print(guess_word)

                #if no dashes left in the guess_word, player has won.
                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                #if the user is out of guesses, the game ends and the secret word is shown
                if guess_taken == 10:
                    print("Sorry, You lost! The secret word was",   secret_word);



# run the game
def spaceman():

    word_description();
    guessing();


spaceman();
