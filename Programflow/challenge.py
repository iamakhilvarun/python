#make menu of 1 to 6 or something choose a thing from it and put it in loop so we can use again and again
choice="-"#putting choice value "-" as choice should have value beofre i intialise it 
while choice != 0:      
    if choice in "12345":
        print("you choose {}".format(choice))
    else:
        print("please choose something form the menu 1 to 6")
        print("1:\tLearn pyhthon")
        print("2:\tLearn java")
        print("3:\tLearn calculas")
        print("4:\tgo outside")
        print("5:\thave dinner")
        print("0:\tEXIT")

    choice = input()
