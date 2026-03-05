print("today is good day to learn python")
print("python is fun")
print("python's strings are easy to use")
print('we can even use "double qoutes" in string')
print("hello" + "world")  # (+) doing this strings gets concatneated

greetings = "hello"
name = "Akhil"
# name = input('please enter you name:')# input is function to store something
print(greetings + name)
# here the return value is whatever the user is inputing
# if we wnat space we can add that too
# print(greetings+' '+name)


age = 20  # int type data type
print(age)

Age = 29.2
print(Age)
# to know what data type it is we use type to find out the data type we are using
print(type(greetings))
print(type(age))
print(type(Age))

age_in_words = "20 years"
print(name + f" is {age} years old")
print(type(age_in_words))

print(f"pi is approximately{22/7:12.50f}")

pi=22/7
print(f"pi is approxmately {pi:12.50f}")