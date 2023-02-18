import random

def printAsciiImage(choice):
    if choice == 0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif choice ==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif choice==2:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

def calculateWinner(user_choice, comp_choice):
    if user_choice == 0:
        if comp_choice == 2:
            print("You Won!!!")
        elif comp_choice == 1:
            print("You Lost!")
        else :
            print("Draw!!!!")
    elif user_choice == 1:
        if comp_choice == 0:
            print("You Won!!!")
        elif comp_choice == 2:
            print("You Lost!")
        else :
            print("Draw!!!!")
    elif user_choice == 2:
        if comp_choice == 1:
            print("You Won!!!")
        elif comp_choice == 0:
            print("You Lost!")
        else :
            print("Draw!!!!")
    else:
        print("Wrong User Input")

user_choice=int(input("Choose your option. 0 for Rock, 1 for Paper and 2 for Scissors "))
comp_choice=random.randint(0,2)
print("You chose ")
printAsciiImage(user_choice)
print("Computer chose ")
printAsciiImage(comp_choice)
calculateWinner(user_choice,comp_choice)

