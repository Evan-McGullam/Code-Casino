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

