age= int(input("How old are you? "))

# if age >=16 and age<=65:#both expressions need to be true (correct one )
#if 16 <= age <= 65
# if  age <= 16  <=65:
    #this is worng practice as it interpret as age >=16 then 16<=65 which skips the condition
    #see here age is not checked second time
if age in range (16,66):      
    print("Have good day at work")
else:
    print("Enjoy your free time")

print("-"*80)

if age <16 or age >65:#any one condition can be true9
    print("Enjoy your free time")
else:
    print("Have a good day at work")