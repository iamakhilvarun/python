while True:
    username=str(input("Enter your username: "))
    password=input("Enter your password: ")

    correct_username="Akhilvarun@123"
    correct_password="1akv0#98@*23"
    if username == correct_username:
        if password==correct_password:
            print("LOGIN SUCCESSFULLY......")
            break
        else:
            i=3
            for i in range (3,0,-1):
              print("You have written worng password, Please write correct password")
              print("you have {} attempts left".format(i-1))
              break

    else:
        print("Wrong username")