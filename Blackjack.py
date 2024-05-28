start = 0
while start == 0:
  print("--------------------------------------------------")
  print("--------------------------------------------------")
  print("Ready to Start? Yes or No?")
  x = input()
  if x.lower() == "yes":
    print("Okay, let's start!")
    print("")
    start = 1
  elif x.lower() == "no":
    print("Come back any time!")
  else:
    print("Please enter a valid input. Only 'Yes' or 'No' are accepted.")

#put all in an if statement for loop "start"
bust = 0
initial = 0
hit = 0
import random
while initial == 0:
  startcard1 = random.randint(1,11)
  startcard2 = random.randint(1,11)
  housestart1 = random.randint(1,11)
  housestart2 = random.randint(1,11)
  print("Your starting cards are", startcard1, "and", startcard2,", totalling", startcard1+startcard2)
  if startcard1 == 11 and startcard2 == 11:
    print("You have 2 Aces! Would you like your total to be 12 or 2?")
    y = input()
    if y == "12":
      totalcard = 12
    elif y == "2":
      totalcard = 2
  elif startcard1 == 1 and startcard2 == 1:
    print("You have 2 Aces! Would you like your total to be 12 or 2?")
    y = input()
    if y == "12":
      totalcard = 12
    elif y == "2":
      totalcard = 2
  print("The House's starting cards are", housestart1, "and X, totalling", housestart1, "+ X. Remember the House still has one card face down (X).")
  totalcard = startcard1+startcard2
  print("Would you like to hit or stand? Remember anything above 21 is a bust.")
  initial = 1

continuedhit = 0
newtotalcard = 0
#hit or stand
rehit = input("Hit or Stand?")
#if hit, add another card to totalcard, then ask if they want to hit or stand again, create loop
while bust == 0:
  if rehit.lower() == "hit":
      newtotalcard = newtotalcard + totalcard + random.randint(1,11)
      print("Your new total is",newtotalcard)
      if newtotalcard > 21:
        print("You lose! Total exceeds 21 :(")
        bust = 1
        exitcontloop = 1
        break
      elif newtotalcard == 21:
        print("You have 21! Blackjack!")
        continuedhit = 1
        exitcontloop = 1
        break
      exitcontloop = input("Would you like to hit again or stand?")
      if exitcontloop.lower() == "stand":
        continuedhit = 1
        exitcontloop = 1
        break
      elif exitcontloop.lower() == "hit":
        while continuedhit == 0:
          newtotalcard = newtotalcard + random.randint(1,11)
          print("Your new total is",newtotalcard)
          if newtotalcard > 21:
            print("You lose! Total exceeds 21 :(")
            bust = 1
            exitcontloop = 1
            break
          elif newtotalcard == 21:
            print("You have 21! Blackjack!")
            bust = 1
            exitcontloop = 1
            break
          again=input("Would you like to hit again or stand?")
          if again.lower() == "stand":
            continuedhit = 1
            bust = 1
            print("You have chosen to stand.")
          elif again.lower() == "hit":
            continuedhit = 0
  elif rehit.lower() == "stand" or continuedhit == 1:
    bust = 1
  #problem with getting 21 or over 21 and still printing stand
#fix card total when selecting aces






#if stand, add house card 2, then see who won










