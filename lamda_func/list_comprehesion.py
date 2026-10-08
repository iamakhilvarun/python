l = [1, 2, 3, 4, 5, 6, 7]

l1 = [item * 2 for item in l]
print(l1)


l2=[i**2 for i in range(10)]
print(l2)

l3=[i**2 for i in range(10) if i%2!=0]
print(l3)

fruits=['Apple','Mango','Orange','Grape','Kiwi']
l4=[fruit for fruit in fruits if fruit[0]=='O']
print(l4)