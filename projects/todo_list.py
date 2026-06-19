# TO_DO list
my_list=()

n=int(input("How many do you want to add: "))

for index in range (n):
    user_input=input("Enter what do you want to add :")
    my_list.append(user_input)
    print(my_list)

m=int(input("How many do you want to remove from the list: "))
for index in range (m):
    my_list.remove(input("what do you want to remove from the list : "))
    print(my_list)