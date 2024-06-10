import random

def draw_card():
    return random.randint(1, 11)

def get_player_choice():
    while True:
        choice = input("Would you like to hit or stand? ").lower()
        if choice in ['hit', 'stand']:
            return choice
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

def handle_aces(card1, card2):
    if card1 == 11 and card2 == 11:
        while True:
            choice = input("You have 2 Aces! Would you like your total to be 12 or 2? ")
            if choice == "12":
                return 12
            elif choice == "2":
                return 2
            else:
                print("Invalid input. Please enter '12' or '2'.")
    return card1 + card2

# Start the game
def main():
    startcard1 = draw_card()
    startcard2 = draw_card()
    totalcard = handle_aces(startcard1, startcard2)
    
    print(f"Your starting cards are {startcard1} and {startcard2}, totaling {totalcard}")
    
    while True:
        choice = get_player_choice()
        if choice == 'hit':
            new_card = draw_card()
            totalcard += new_card
            print(f"You drew {new_card}. Your total is now {totalcard}.")
            if totalcard > 21:
                print("You lose! Total exceeds 21 :(")
                break
            elif totalcard == 21:
                print("You have 21! Blackjack!")
                break
        else:  # stand
            print("You chose to stand.")
            break

    # Additional logic for house turn would go here...

if __name__ == "__main__":
    main()
