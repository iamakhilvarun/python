generated_list=( '8' ,' ',
                '2''2''2', ' ',
                '4''2'' ', ' ',
                '2''6''7',' ',
                '4''5',' ',
                '8''6''7')
# use for loop to produce list of int not strings
# created a empty list then append it with number 
number_integer =()
for value in generated_list:
    if value != ' ':
       number_integer.append(int(value))
print(number_integer)
