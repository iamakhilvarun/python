# reduce() repeatedly applies a function to the elements of an iterable and reduces them to a single value.
import functools

l=[1,2,3,4,5,6,7]

a=functools.reduce(lambda x,y:x+y,l)
print(a)


l1=[12,13,56,11,21,58]
b=functools.reduce(lambda x,y:x if x>y else y,l1)
print(b)

c=functools.reduce(lambda x,y:x if x<y else y,l1)
print(c)