import random
from art import logo
rules = """
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    
def calculateWinner(final_hand,user_score,computer_score):
    print(f"Your final hand: {final_hand['user']}, final score: {user_score}")
    print(f"Computer's final hand: {final_hand['computer']}, final score: {computer_score}")
    
    if user_score > 21:
        print("You went over. You lose")
    elif computer_score >21:
        print("Computer went over. You win")
    elif user_score==computer_score:
        print("Score is even. It's a draw")
    elif user_score> computer_score:
        print("You win")
    else:
        print("You lose")
    
    
def play():
    print("-----------------------------------------------------------")
    print(rules)
    bid=input("Do you want to play Blackjack? 'y' to yes, 'n' to no\n")
    if bid=="y":    
        user_cards=[]
        computer_cards=[]
        user_score=0
        computer_score=0
        
        final_hand={
        "user":user_cards,
        "computer":computer_cards
        }
        
        for x in range(0,2):
            card=random.choice(cards)
            user_score+=card
            final_hand["user"].append(card)
            
        for x in range(0,2):
            card=random.choice(cards)
            computer_score+=card
            final_hand["computer"].append(card)
            
        print(logo)
        print(f"Your cards: {final_hand['user']}, current score: {user_score}")
        print(f"Computer's first hand: {final_hand['computer'][0]}")
        if user_score==21:
            print("You got Blackjack. You win!!!")
        elif computer_score==21:
            print("Computer got a Blackjack. You lose!!!")
        else:
            passorplay=input("How do you wish to continue? 'y' to play, 'n' to pass: ")
            while passorplay=="y":
                card=random.choice(cards)
                user_score+=card
                final_hand["user"].append(card)
                print(f"Your cards: {final_hand['user']}, current score: {user_score}")
                print(f"Computer's first hand: {final_hand['computer'][0]}")
                        
                if user_score>=21:
                    passorplay="n"
                else:
                    passorplay=input("\nHow do you wish to continue? 'y' to play, 'n' to pass: ")
            
            while computer_score<user_score or computer_score<21:
                card=random.choice(cards)
                computer_score+=card
                final_hand["computer"].append(card)
            
            calculateWinner(final_hand,user_score,computer_score)
    elif bid=="n":
        print("Goodbye. Please visit soon!!!")
        return
    else:
        print("Please enter a valid input")
    play()
    
play()