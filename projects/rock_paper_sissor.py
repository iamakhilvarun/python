# ROCK PAPER SCISSORS
import random
items=["rock","paper","scissors"]

while True:
    user_input= str(input("Throw hand sign: "))
    computer_choice=random.choice(items)
    print(f"I throw {user_input}")
    print(f"computer throw {computer_choice}")
    if user_input=="0":
        print("-----GAME OVER-----")
        break
    elif user_input not in items:
        print("NOT A VALID CHOICE!!")
        break
    elif user_input=="paper"and computer_choice=="rock":
        print("YOU WIN!")
    elif user_input=="rock" and computer_choice=="paper":
        print("COMPUTER WINS!!")
    elif user_input=="scissors" and computer_choice=="rock":
        print("COMPUTER WINS!!")
    elif user_input=="rock" and computer_choice=="scissors":
        print("YOU WINS!!")
    elif user_input=="scissors" and computer_choice=="paper":
        print("YOU WINS!!")
    elif user_input=="paper" and computer_choice=="scissors":
        print("COMPUTER WINS!!")
    elif user_input==computer_choice:
        print("its a draw")
    print()
    
    
