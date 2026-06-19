availabale_parts=("computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat",
                  "hdmi cable",
                  "dvd driver"
                  )
# valid_choices=(str(i) for i in range (1,len(availabale_parts)+1))

valid_choices= ()
for i in range(1, len(availabale_parts) + 1 ):
    valid_choices.append(str(i))
print(valid_choices)
current_choice="-"
computer_parts=()#create a empty list

availabale_parts.sort()
while current_choice != '0':
    if current_choice in valid_choices:
        index= int(current_choice) -1
        Chosen_parts = availabale_parts(index)
        if Chosen_parts in computer_parts:
            # it is already in cart so remove them
            computer_parts.remove(Chosen_parts)
        else :
            print("Adding {}".format(current_choice))
            computer_parts.append(Chosen_parts)
        print("You list now contains : {}".format(computer_parts))           
    else:
        print("Please add options from the list below:")
        for number, part in enumerate (availabale_parts):
        #enumerate is a function which returns each item , with its index position
        #use when you have large number of menu items it is fast, clean and safe
            print("{0}: {1}".format(number+1,part)) 

    current_choice = input()

print(computer_parts)
