guessloop = 0

import random
import time
wordbank = ["tech", "computer", "python", "chair", "table", "mouse", "keyboard", "monitor", "mousepad", "printer", "monitor", "cache", "audio", "button", "terminal", "virus", "malware", "motherboard", "bluetooth"] #add more
theword = random.choice(wordbank)
lives = 7
2
print(theword)
print("Welcome to Hangman!")
print("Try to guess the word, you have 7 lives. Choose wisely!")
print("--------------------------------------------------")
print("The word is", len(theword), "letters long.")

board = ["_"] * len(theword)
print(" ".join(board))

while guessloop == 0:
  guess = input("Guess!").lower()
  found = False

  if len(guess) != 1:
      print("Please enter only one letter.")
      continue

  for i in range (len(theword)):
     if guess == theword[i]: 
        board[i] = guess
        found = True

  if found == True:
     print(" ".join(board))
     if "_" not in board:
        print("You guessed the word! You win!")
        guessloop = 1
  else:
      lives -= 1
      print("Letter is not in word. You have", lives, "lives left.")
      print(" ".join(board))

      if lives == 0:
         print("You ran out of lives. Valiant Effort!")
         print("The word was",theword)
         guessloop = 1

time.sleep(0.25)
from subprocess import call
def open_py_file():
      call(["python", "index.py"])
open_py_file()
  