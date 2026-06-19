Number = input("Please enter a series of numbers, using a seprators you like: ")
seperators=""

for char in Number:
    if not char.isnumeric():#.isnumeric is a string method in python used to check wheather a string contains only numeric charcters
                            #if it is a number then true else false then that would appended to seperators
        seperators=seperators+char 
# print(seperators)

values = "".join(char if char not in seperators else " " for char in Number).split()
print(sum((int(val) for val in values)))