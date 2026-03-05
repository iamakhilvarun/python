parrot="Norwegian blue"

letter =input("Enter a charcter: ")

if  letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("I dont need that letter")