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
            success= False
            for attempts in range (3,0,-1):
              print("You have written wrong password, Please write correct password")
              print("you have {} attempts left".format(attempts-1))
              password=input("Enter your password: ")
              
              if password ==correct_password:
                  print("LOGIN SUCCESSFULLY")
                  success=True
                  break
            if success:#if success == True (else block terminates)
                  break
            else:
                print("QUITING PROGRAM")
                break
    else:
        print("Wrong username")