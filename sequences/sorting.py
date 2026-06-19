pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers=(2.3,4.5,8.7,3.1,9.2,1.6)
# You use sorted when you take some data
# Python creates a new sorted list
# You usually assign it to a variable
# works on list , str , tuple   
sorted_numbers=sorted(numbers)
print(sorted_numbers)
print(numbers)

# we use sort when You already have a list
# You sort that same list
# Nothing new is created
# works on list 
another_sorted_numbers=numbers.sort()

# Here i am using direct string literal which means i am not assinging it to another varaible 
# Like in line 1 to 4 using it directly as a string then sorting it then assigning it to variable 
missing_letter=sorted("The quick brown fox jumps over the lazy dog",
                      key=str.casefold )# syntax -->sorted(iterable, key=some_function)
                                        # a key is A function that tells Python how to compare items before sorting.
print(missing_letter)

name = ("Graham",
       "John",
       "terry",
       "eric",
       "Terry",
       "michael"
       )

name.sort(key=str.casefold)
print(name )