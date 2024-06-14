import random
playercash = 500
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print("Welcome to Makeshift Dice!")
print("In this game you roll dice, and either win or lose money! Simple. :)")
print("")
betamount = input("How much money would you like to bet this round?")
playercash = (playercash)-(int(betamount))
print("You bet",betamount,". Your new total is", playercash)
print("")
print("You can bet on, 1: Wether the dice are even or odd, 2: The Numbers of the Dice, 3: Higher or Lower than certain number")
dicebet = input("Which option would you like(Type the number.).")