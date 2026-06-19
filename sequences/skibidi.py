user_input=input("Enter the values of variables sperated by commas : ")

user_list= user_input.split(",")
calculate=()
for value in user_list:
    calculate.append(int(value))
    
a,b,c=calculate
result=calculate(0)+calculate(1)-calculate(2)
print(result)
if result == 0 :  
    print ("skibidi")