# numbers={*""}
# numbers={*{}}
numbers=set()

# numbers.add(1)
# print(numbers,type(numbers))

# At start of loop len(numbers)==0 contuniue till it reaches 3 break 
# while len(numbers)<4:
#     next_value=int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

data=["blue","red","blue","green","red","blue","white"]
# Create a set form the list , to remove the duplicates
unique_data=sorted(set(data))
print(unique_data)

# Create a list unique colors , keeping the order the apperead
unique_data=list(dict.fromkeys(data))
print(unique_data)
print()
print(dict.fromkeys(data))