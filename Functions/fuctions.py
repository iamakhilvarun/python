# a fuction starts with the keyword def 
# next, we have the fuction name 
# if the fuctions will take parameteres , they are declared in parenthesiss 
# the parenthesis are required even no parameters are there 
def multiplty(x,y):
    result = x*y
    return result

def is_palindorme(string):
    # backwards=string[::-1]
    # return backwards == string
    return string[::-1].casefold()==string.casefold()

# word = input("please enter a word to check:")
# if is_palindorme(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

def palindrome_sentence(sentence):
    string=""
    for char in sentence:
        if char.isalnum():
            string+=char
    print(string)        
    # return string[::-1].casefold()==string.casefold()
    return is_palindorme(string)

# word= input("Please enter your sentence: ")
# if palindrome_sentence(word):
#     print("'{}'-- is a palindorme sentence".format(word))
# else:
#     print("'{}'-- is not a palindorme sentence".format(word))

answer = multiplty(18,3)
print(answer)