from art import stages,logo
from words import word_list
import random


print(logo)
word=random.choice(word_list)

curr_word=[]
lives=6
for letter in word:
    curr_word+="_"
    
print(stages[lives])
while lives>0:
    print(f"{' '.join(curr_word) }")
    char=input("Please enter the character you want to check \n")
    if char in curr_word:
        print(f"You have already guessed '{char}' !!!")
        continue
    flag=0
    for x in range(0, len(word)):
        if word[x]==char:
            curr_word[x]=char
            flag=1
        
    if flag==0:
        lives -= 1
        print("Your guess was incorrect. You lose a life")
        print(stages[lives])

if lives==0:
    print("You Lose!!!")
    print(f"The word was {word}")
else:
    print("You win!!!")