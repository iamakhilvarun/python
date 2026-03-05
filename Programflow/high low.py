low = 1
high = 1000

print("PLease think of number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high: # logic is run the code until low == high 
    # print("\tGuessing the range of {} to {}".format(low,high))
    guess = low + (high - low) // 2
    high_low = input(
        "My guess is {}.should I guess higher or lower?  "
        "Enter h or l, c if answer is correct "
        .format(guess)).casefold()
    if high_low =="h":
        # Guess higher THe low end  of the range  becomes 1 greater than the guess.
        low = guess+1
    elif high_low == "l":
        # Guess lower THe high end of the range becomes one less than the game
        high =guess -1
    elif high_low =="c":
        print("I got it in {} guesses!".format(guesses))
        break
    else :
        print("please enter h, l,c")
        
    # guesses = guesses + 1 # less effcient
    guesses +=1

#“Run this else only if the loop was NOT stopped by break.”
else :
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))