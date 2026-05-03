# caluclator 

print("Welcome to my first pyhton project")
menu = ["Addition", "subtraction", "multiplication", "division"]

for menu_value in menu:
    value = menu_value

print(value)

while True:
    print("\n---------MENU ITEMS---------\n")
    # displaying the menu
    for i, option in enumerate(menu, start=1):
        print(f"{i}. {option}")

    print("\n----------------------------\n")

    user_choice = input("Enter Y / N: ")

    if user_choice.lower() == "y":
            

        a = int(input("Enter First Input: "))
        b = int(input("Enter Second Input: "))
        chossen_input = input("Enter The Operation You Want To Choose:")

        if chossen_input == "1":
            print("you have choosen {} ".format(menu[0]))
            c = a + b
            print("addtion of {} and {} is : ".format(a, b), c)
        elif chossen_input == "2":
            print("you have choosen {} ".format(menu[1]))
            c = a - b
            print("subtraction of {} and {} is : ".format(a, b), c)
        elif chossen_input == "3":
            print("you have choosen {} ".format(menu[2]))
            c = a * b
            print("multiplication of {} and {} is : ".format(a, b), c)
        elif chossen_input == "4":
            print("you have choosen {} ".format(menu[3]))
            c = a / b
            print("division of {} and {} is : ".format(a, b), c)
        else:
            print("you have chossen invalid operation please select given opreation")
    elif user_choice.lower() == "n":
        break
