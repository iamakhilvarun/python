# ROCK PAPER SCISSORS
# TODO: 1) user_score and computer_score
        # 2) best of 3 or 5 count 
        # 3) allow uppercase inputs
        # 4) show stats
        # 5) add import os
        # 6) use or for if else condition to make it shorter , efficent

import random
items=("rock","paper","scissors")

user_score=0
computer_score=0

while True:

    user_input= str(input("Throw hand sign: ")).lower()
    computer_choice=random.choice(items)
    print(f"I throw {user_input}")
    print(f"computer throws {computer_choice}")
    if user_input=="0":
        print("-----GAME OVER-----")
        break
    elif user_input not in items:
        print("NOT A VALID CHOICE!!")
        continue
    elif user_input=="paper"and computer_choice=="rock":
        print("YOU WIN!")
        user_score+=1
    elif user_input=="rock" and computer_choice=="paper":
        print("COMPUTER WINS!!")
        computer_score+=1
    elif user_input=="scissors" and computer_choice=="rock":
        print("COMPUTER WINS!!")
        computer_score+=1
    elif user_input=="rock" and computer_choice=="scissors":
        print("YOU WIN!!")
        user_score+=1
    elif user_input=="scissors" and computer_choice=="paper":
        print("YOU WIN!!")
        user_score+=1
    elif user_input=="paper" and computer_choice=="scissors":
        print("COMPUTER WINS!!")
        computer_score+=1
    elif user_input==computer_choice:
        print("its a draw")
    print(f"your_score: {user_score}")
    print(f"computer score: {computer_score}")
    print()