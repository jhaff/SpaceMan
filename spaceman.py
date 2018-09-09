import random

#form the list of words and select one randomly
def load_word():
  #use of a tuple because words will not change
  wordList = (
  "bowl", "power", "window", "computer", "phone", "juice", "macbook", "desktop",
  "laptop", "dog", "cat", "lemon", "cable", "mirror", "hat"
           )

  guessWord = []
  # randomly choose single word from the list
  secret_Word = random.choice(wordList)
  #make a variable for the length of the chosen word
  wordLength = len(secret_Word)
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  #form empty mutable list to store guessed letters
  letter_storage = []

def word_description():

    # print blanks for each letter in secret word
    for character in secret_Word:
        guess_word.append("_ ")

    print("The word you must guess has", wordLength, "characters")

    print("You may only enter 1 letter from a-z\n\n")

    print(guess_word)

    # FILL IN YOUR CODE HERE...

def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...




def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''




def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...


#
# secret_word = load_word()
# spaceman(load_word())
