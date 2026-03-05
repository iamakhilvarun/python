data=[4 , 5 , 104 ,105, 110 ,120 , 130 , 130 , 150 ,
      160 , 170 , 183 , 185 , 187 ,188, 191 , 350 , 360]

# del data[0:2]
# print(data)
# del data[14:] # here we have already removed 4,5(old lenth was 18 ) then postion of elements changes and new length will be 15  
# print(data)

min_valid = 100
max_valid = 200

#process the low values in list
stop= 0
for index , value in enumerate (data):
    if value >= min_valid:
        stop = index #here i find which is not follow ing the rules  
        break

print(stop)# for debugging
del data[:stop]# now that i know the index at which is it not equal to then i will use slice method 
print(data)

# procees the high  values  in the list 
start = 0
for index in range (len (data)-1, -1,-1):
    if  data [index]<= max_valid:
        # We have the index  of the last  item to keep 
        # Set 'start' to the position of the first 
        # item  to delete , which is 1 after 'index'
        start=index+1
        break 
print(start) # for debugging 
del data [start :]
print(data)
