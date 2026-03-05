numbers= [1,45,31,16,60]
# In a [for-else] loop the ese block excutes only inf the loop completes without encountring a break
for number in numbers:
    if number % 8 == 0:
        #reject the list 
        print ("numbers are unaccpectable")
        break

else :
    print("ALL the numbers are fine")