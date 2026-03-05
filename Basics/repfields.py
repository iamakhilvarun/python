age = 24
print("my age is {0} years".format(age))
print("my age is " + str(age) + " years")  # str--> string
# Replacement fields
print(
    "There are {0} days in {1} ,{2} ,{3} ,{4}, {5} ,{6} and {7} ".format(
        31, "jan", "march", "may", "july", "august", "octuber", "december"
    )
)  # we are using format for easy readability and easy to use

# we {} for index the use .format  to replace the things in string just like above

print(
    "There are {0} days in jan , march, may , july, august, octuber and december".format(
        31
    )
)

print(
    "Jan: {2}, feb: {0},mar: {2},apr: {1},may: {2},jun: {1},jul: {2},aug: {2},sep: {1},oct: {2},nov: {1},dec: {2}".format(
        28, 30, 31
    )
)  # index({0},{1},{2})


print("""
       Jan: {2},
       feb: {0}
       mar: {2}
       apr: {1}
       may: {2}
       jun: {1}
       jul: {2}
       aug: {2}
       sep: {1}
       oct: {2}
       nov: {1}
       dec: {2}"""
       .format(28,30,31)
)
