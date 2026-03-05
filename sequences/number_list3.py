empty_list=[]
even=[2,4,6,8]
odd= [1,3,5,7,9]

numbers=even+odd
print(numbers)

sorted_numbers= sorted(numbers)
print(sorted_numbers)
print(numbers)

digits=list("432958617")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()#.copy() is a list method that creates a shallow copy of a list.
print(more_numbers)
print(numbers is more_numbers)# False as numbers(list) != more_numbers{list} so this false 
                             #  if the both list were equal then it would return True 
print(numbers == more_numbers)# True as == contains equal items so it is true