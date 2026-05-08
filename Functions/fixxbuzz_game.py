# Psedocode -->
#caluclate the computer "number" (which may be like fizz, buzz , fizz buzz)
#print the computer response
#calculate the player's correct answer
#get input from the player
# compare answer to the players input
# Repeat , until the player makes a mistake or we reach 100
#print a suitable  meassage : "congrats" or "wrong"

def fizz_buzz(number:int)->str:
    """ 
    checks if the number is divisble by 3 or 5 or both

    :param int number: user input variable
    """
    if number % 3==0 and number % 5 ==0:
            return "fizz buzz"
    elif number % 5 == 0:
            return "buzz"
    elif number % 3==0:
            return "fizz"
    else:
            return str(number)
    
user_input=fizz_buzz(15)
print(user_input)

input("Play Fizz Buzz.  press ENTER to start")
print()

next_number=0
while next_number <99:
       next_number+=1
       print(fizz_buzz(next_number))
       next_number+=1
       correct_answer=fizz_buzz(next_number)
       players_answer=input("Your go: ")
       if players_answer!=correct_answer:
              print("your lose , the correct answer is {}".format(correct_answer))
              break
else:
       print("well done you reached {}".format(next_number))