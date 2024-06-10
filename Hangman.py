guessloop = 0

import random
wordbank = ["tech", "computer", "python", "chair", "table", "mouse", "keyboard", "monitor", "mousepad", "printer", "monitor"] #add more
theword = random.choice(wordbank)
lives = 7
2
#while lives > 0:
print("Welcome to Hangman!")
print("Try to guess the word, you have 7 lives. Choose wisely!")
print("--------------------------------------------------")
print("The word is", len(theword), "letters long.")

board = ["_"] * len(theword)
print(" ".join(board))
print(theword)

while guessloop == 0:
  guess = input("Beging guessing!").lower()
  found = False

  for i in range (len(theword)):
     if guess[i] == theword[i]: #need to fix index string error
        board[i] = guess
        found = True

  if found == True:
     print(" ".join(board))
     if "_" not in board:
        print("You guessed the word! You win!")
        guessloop = 1
     else:
        lives = -1
        print("Letter is not in word. You have", lives, "left.")
        print(" ".join(board))

if lives == 0:
   print=("You ran out of lives. Valiant Effort!")
   guessloop = 1