# Higher-Order Functions (HOF) in Python
# 1. What is a Higher-Order Function?
# A Higher-Order Function is a function that does at least one of these:
# 1. Takes another function as an argument
# 2. Returns another function
# That's the entire core idea.
l = [11, 14, 21, 23, 56, 78, 45, 29, 28]

# this is the one method
# def return_sum(l):
#     even_sum=0
#     odd_sum=0
#     div3_sum=0
#     for i in l:
#         if i%2==0:
#             even_sum=even_sum+i
#         if i%2!=0:
#             odd_sum=odd_sum+i

#     return (even_sum),(odd_sum)


# the second method
def return_sum(func, l):
    result=0
    for i in l:
        if func (i):
            result=result+i
    return result


x = lambda x: x % 2 == 0
y = lambda x: x % 2 != 0
z = lambda x: x % 3 == 0

print(return_sum(x,l))
print(return_sum(y,l))
print(return_sum(z,l))
