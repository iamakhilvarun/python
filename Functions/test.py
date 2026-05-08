def sum_numbers(*args:int)->float:
    """ total sum of all the numbers
    """
    x=0
    for number in args:
        x+=number
    print(x)
    return x
    
sum_numbers(1,2,3)  
sum_numbers(8,20,2)
sum_numbers(12.5,3.147,98.1)  
sum_numbers(1.1, 2.2, 5.5)  