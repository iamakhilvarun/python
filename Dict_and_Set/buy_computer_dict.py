availabale_parts={"1":"computer",
                  "2":"monitor",
                  "3":"keyboard",
                  "4":"mouse",
                  "5":"mouse mat",
                  "6":"hdmi cable",
                  "7":"dvd driver"
                  }

current_choice=None
computer_parts={} # create an empty dictionary
while current_choice!="0":
    if current_choice in availabale_parts:
        chosen_part=availabale_parts(current_choice)

        if current_choice in computer_parts: 
            # it's already in , so remove it
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts(current_choice)=chosen_part
        print(f"Your dict now contains: {computer_parts}")
        
    else:
        print("Please add options from the list:")
        for key,value in availabale_parts.items():
            print(f"{key}: {value}")
        print("0: To finish")
            
    current_choice=input("> ")
