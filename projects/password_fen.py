#TODO=Show previously generated passwrods
import random 
letters ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
saved_password=[]       
def generate_password():
    """
    It generates a random password using letters, numbers, and special charcters

    The user input the password length

    return: NONE
    """ 
    while True:
        choice=input("Do you want to quit: (yes/no)")
        if choice=="yes":
            break
        else:
            pass_len=int(input("Please enter the len of pass: "))
            password=""
            for i in range (pass_len):
                random_string=(random.choice(letters))
                password+=random_string
            saved_password.append(password)
            print("genreated password",password)
        continue
        
       
def history():
    """
    Display the previous passwords

    asks the user if he wants to print the passwords
    """
    user_input=(input("whats the user_input: "))
    if user_input=="nigga":
        print("Your saved passwords : {0}".format(saved_password))
        

while True:
    print("\n=============MENU==============\n")
    print("1. Genrate password\n")
    print("2. previous passwords\n")
    print("3. Quit\n")

    choice=input("What can i do for you?:")
    if choice=="1":
        generate_password()
    elif choice=="2" :
        history()
    elif choice=="3":
        print("Quitting the program.....")
        break
    else:
        print("invalid choice")