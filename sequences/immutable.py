# result = True

# another_result= result
# print(id(result))# Return the 'identity' of an object ,it is guaranteed to be unique and constant for this object during its lifetime
# print(id(another_result))
# result =False
# print(id(result))

result="correct"
another_result= result
print(id(result))
print(id(another_result))

result+="ish"
print(result)
print(id(result))# here we add string to an another stirng which changes the id 
print(id(another_result))#Because strings are immutable:

# Python creates a NEW string "correctish"

# result is re-bound to this new object

# another_result is left unchanged