#A list is an ordered, mutable collection of elements enclosed in square brackets [].
computer_parts=["computer",
                "keyboard",
                "monitor",
                "mouse",
                "mouse mat"
                ]
print (computer_parts)

# computer_parts[3]= "Trackball"# here we are reaplacing mouse with Trackball
print(computer_parts[3:])

computer_parts[3:]=["Trackball"]# Here Trackball is string which is itreable thats why ouput is ajeeb
                                # Trackball is pushed inside coumputer_parts and mouse and mouse mat is removed (since [3:] removes the element after the 3 rd index) 
print(computer_parts)