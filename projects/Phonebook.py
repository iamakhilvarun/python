contacts = {
    "Akhil": "8292820421",
    "Rishu": "8292100377",
    "Tej": "929277191117",
    "Akash": "73282392929",
    "Aditya": "23823291093",
    "Aastha": "81829392001",
    "Ayush": "818191310191",
    "Auro": "188137199991",
    "spam": "182833552888",
}


def menu_system():
    print("1. option 1: Add a contact")
    print("2. option 2: Find contact")
    print("3. option 3: Show all contacts")
    print("4. option 4: Delete a contact")
    print("5. option 5: Update a existing contact")
    print("6. option 6: Total contacts")
    print("7. Exit program")


def option_1():
    print("You have selected option 1")
    name = input("Please enter the name of the person: ").lower()
    number = input("Please enter the number of the person: ")
    contacts[name] = number
    print("contact added")


def option_2():
    name=input("Please enter the name you want to find: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("There is no such name...")
# option_2()


def option_3():
    for name , phone_number in contacts.items():
        print(f"{name}: {phone_number}")

# option_3()

def option_4():
    name=input("Enter the name you want to delete: ")
    del contacts[name]
    print(f"Deleting {name}....")

def option_5():
    name=input("Enter the name you want to update: ")
    new_number=input("Enter the new number: ")
    if name in contacts:
        contacts[name]=new_number
        print("The number is updated!!")
        print(f"{name}: {contacts[name]}")
    else:
        print("There is no such name...")
    
# option_5()
def option_6():
    print(f"Total number of contacts: {len(contacts)}")

while True:
    menu_system()
    choice=input("Choose an option: ")

    if choice=="1":
        option_1()
        print()
    elif choice=="2":
        option_2()
        print()
    elif choice=="3":
        option_3()
        print()
    elif choice=="4":
        option_4()
        print()
    elif choice=="5":
        option_5()
        print()
    elif choice=="6":
        option_6()
        print()
    elif choice=="7":
        print("You have exited the program....")
        break
    else:
        print("Invalid option")
        print()