# If map() means "transform every item", then filter() means "keep only the items that satisfy a condition.
# filter() is a built-in Higher-Order Function used to select elements from an iterable based on a condition.
# filter(function, iterable)
l=[1,2,3,4,5,6,7]

a=list(filter(lambda x:x>4,l))
print(a)

fruits=['Apple','Mango','Orange','Grape','Kiwi']

b=list(filter (lambda fruit:'e' in fruit,fruits))
print(b)