answer = 5
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess  < answer:
        print("please guess higher")
    else: #guess must be greater than answer
        print("please guess lower")
    guess= int(input())
    if guess == answer:
        print("well done you have guessed right")
    else:
        print("sorry you have not guessed correctly")
else :
    print("you got it first time")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())  # we use = to bind something to that variable
#     if guess == answer:  # == means asiggning something
#         print("well done, you guessed it")
#     else:
#         print("sorry, you have  not guessed correctly")

# elif guess > answer:
#     print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("sorry, you have  not guessed correctly")

# else:
#     print("You got it first time")
