a= 12
b=3

print(a+b)  #15
print(a-b)  #9
print(a*b)  #36
print(a/b)  #4.0
print(a//b) #4 integer division, rounded down to minus infinity
print(a%b)  #0 modulo: the remainder after integer division 

print()

for i in range(1, a//b):
 print (i)

print(a + b / 3 - 4 * 12)#-35

#just with brackets (*) --> (/) --> (+) --> (-)
print(a + (b / 3) - (4 * 12))#-35 

 # Because many parentheses are used, the precedence doesn’t matter
print( ( ( ( a + b ) / 3 ) - 4 ) * 12 )# so we get 12

 #Since parentheses control the order, Python evaluates it from inside → outside:
print( ( ( a + b ) / 3 - 4 ) * 12 )

#here i am using variables to make it clean
c=a+b
d=c/3 
e=d-4
print(e*12)

print()
print(a /(a*b) / b)