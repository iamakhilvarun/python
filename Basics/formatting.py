#String formatting = controlling HOW text and values appear when printed.
# Width in Python is the number of character spaces reserved for displaying a value in formatted output.
for i in range(1, 13):
    print(
        "No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3)
    )  # {:1}--> width

    print()
# algin in pyhton is used to align left or right
# < is used for left align and > is used for right align
#default is left align < 
for i in range(1, 13):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))

    print()
    # ^ is centered align
for i in range(1, 13):
    print("No. {0:2} squared is {1:<4} and cubed is {2:^4}".format(i, i**2, i**3))

print()

print("Pi is approximately {0:12}".format(22/7))
#{index:width.precisionformat_specifier}
print("Pi is approximately {0:12f}".format(22/7))#f converts the number to 6 decimal places (default value)
print("Pi is approximately {0:12.50f}".format(22/7))# here python ignores the field width for precision
                                                    # .50 tells the after decimal numbers 
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))# here the width is considered >50
print("Pi is approximately {0:<72.50f}".format(22/7))# here Only about 15–16 digits are correct (precise)
#                                                    Digits printed after that are NOT reliable
print("Pi is approximately {0:<72.54f}".format(22/7))

print()

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
