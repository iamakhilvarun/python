import random

# this fuction tells to take the input until the user gives vaild input 
def get_integer(prompt):
    """ Get an integer from the standard Input (stdin).

    The function will continue looping , and prompting
    the user , until a valid `int` is entered.

    :param prompt: The String that the user will see , when
                    they're prompted to enter the value.    
    :return _type_: The integer that the users enters.
    """
    while True:
        temp=input(prompt)
        if temp.isnumeric(): # Takes user input as a string
            return int(temp)
        else:
            print("The {0} is invalid. Please enter valid input".format(temp))   

help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing

guess = 0  # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")