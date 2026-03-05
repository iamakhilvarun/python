#  challenge
import random

highest = 10
answer = random.randint(1, highest) # random is module and .randint is function it contains
                                    # (.) is the dot notation we use for specifing the function in module
print(answer)  # TODO: Remove after the testing
print("please input the number form 1 to {}:".format(highest))
guess = int(input())

if guess == answer:
    print("you got it first time")
else:
    while guess != answer:
        if guess == 0:
            print("you quit the game")
            break
        if guess < answer:
            print("please guess higher")    
        else:
            print("please guess lower")
        guess = int(input())
    else:
        print("you got it")
