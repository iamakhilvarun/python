# a fuction starts with the keyword def 
# next, we have the fuction name 
# if the fuctions will take parameteres , they are declared in parenthesiss 
# the parenthesis are required even no parameters are there 
def multiplty(x:float,y:float)->float:
    """Multiply 2 numbers

    :param _type_ x: user input x
    :param _type_ y: user input y
    :return _type_: x*y
    """
    result = x*y
    return result

def is_palindorme(string:str)->bool:
    """ 
    check if the string in plaindrome

    A palindrome is a string which reads the backwards and forwards as same

    :param bool string: the string to check
    :return bool: True if the `string ` is a plaindrome
    """
    # backwards=string(::-1)
    # return backwards == string
    return string(::-1).casefold()==string.casefold()

# word = input("please enter a word to check:")
# if is_palindorme(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

def palindrome_sentence(sentence:str) ->bool:
    """ 
        Get the string check if its alphanumeric

        :param  sentence: It is the string user gives
        :return : read backwards using casefold checks if its palindrome
    """
    string=""
    for char in sentence:
        if char.isalnum():
            string+=char
    print(string)        
    # return string(::-1).casefold()==string.casefold()
    return is_palindorme(string)

# word= input("Please enter your sentence: ")
# if palindrome_sentence(word):
#     print("'{}'-- is a palindorme sentence".format(word))
# else:
#     print("'{}'-- is not a palindorme sentence".format(word))

def fibonacci(n:int)->int:
    """Return the `n` th fibonacci number, for postive `n`"""
    # here if is BASE CASE here where i alredy know the input so the function 
    # can stop immediately insted of doing more work
    if 0<=n<=1:
        return n
    n_minus1,n_minus2=1,0
    result=None
    for f in range (n-1):
        result=n_minus2+n_minus1
        n_minus2=n_minus1
        n_minus1=result

    return result

for i in range(36):
    print(i,fibonacci(i))

p=palindrome_sentence()