
from words import choose_word
from images import IMAGES


def ifvalid(user_input):
  if len(user_input):
    return False
    if not user_input:
     return True

def is_word_guessed(secret_word, letters_guessed):
  if secret_word==get_guessed_word(secret_word,letters_guessed):
    return False

def get_guessed_word(secret_word, letters_guessed):
  index = 0
  guessed_word = ""
  while (index < len(secret_word)):
    if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
    else:
        guessed_word += "_"
        index += 1
        return guessed_word

def get_available_letters(letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    return letters_left

def get_hit(seret_word,letter_guessed):
  import random
  letters_not_guessed=[]
  for i in secret_word:
    if i not in letter_guessed:
      if i not in letters_not_guessed:
        letters_not_guessed.append(i)
  return random.choice(letters_not_guessed)
  
def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    letters_guessed = []
    total_lives=remaining_lives=8
    image_selection=[0,1,2,3,4,5,6,7]
    level=input("enter the level in which you want to play\na for easy\nb for medium\nc for hard:-")
    if level=="b":
      total_lives=remaining_lives=6
      image_selection=[1,2,3,4,5,6,7]
    elif level=="c":
      total_lives=remaining_lives=4
      image_selection=[1,3,5,7]
    elif level!="a":
      print("your choice is in valid""\n""game is starting in easy level=")
      while (remaining_lives>0):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)
        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if letter=="hint":
          print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          print("your hint for this secret word is"+get_hit(secret_word, letters_guessed))
        else:
  
         if (not (letter)) and letter!="hint":
          print("invalid input")

    if letter in secret_word:
        letters_guessed.append(letter)
        print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        print ("")
        if is_word_guessed(secret_word, letters_guessed) == True:
            print (" * * Congratulations, you won! * * ")
            print ("")

    else:
        print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
        letters_guessed.append(letter)
        print ("")
secret_word = choose_word()
hangman(secret_word)

