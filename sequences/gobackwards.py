# Iterate backwards because we are deleting items from the list.
# If we loop forward, deleting an item shifts the remaining elements left,
# which can cause the next element to be skipped.
# Going backwards prevents this problem because the shift happens
# behind the current index.
# backward is reliable than forward in removing form the list items from the end
data=[104,101,4,105,308,103,5,
      107,100,306,106,102,108]

min_vaild=100
max_valid=200

# for index in range(len(data)-1,-1,-1):# range (start, stop ,step)\
#     if data[index]<min_vaild or data[index]>max_valid:
#         print(index,data)
#         del data[index]

top_index=len(data)-1 # len is used tell number of elements in a data
for index, value in enumerate (reversed(data)):
    if value < min_vaild or value > max_valid:
        print(top_index-index,value)# because we have revresed the list the index will not match 
                                    # the original list
        del data[top_index-index]# bascially this index form the list will get deleted 
print(data)