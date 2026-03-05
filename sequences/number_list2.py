even=[2,4,6,8]
odd= [1,3,5,7,9]

even.extend(odd)#extend() is a list method used to add multiple elements from 
                #another iterable (list, tuple, string, etc.) to the end of an existing list
print(even)
another_even=even
print(another_even)
# we using reverse = True because it will sort first then reverse the order big to small 
# if we use = False then nothing will happen cause by default (reverse = False) so nothing happens
even.sort(reverse=True) #sort() is a list method that arranges the elements of a list in order.
print(even)
print(another_even)