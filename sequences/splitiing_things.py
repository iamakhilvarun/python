panagram="""The quick brown
 fox jumps\tover
 the lazy dog"""

words= panagram.split()
print(words)

number = "8,222,42,267,45,867"
print(number.split(","))

generated_list=( '8' ,' ',
                '2''2''2', ' ',
                '4''2'' ', ' ',
                '2''6''7',' ',
                '4''5',' ',
                '8''6''7')

value = " ".join(generated_list)
print(value)

value_list=value.split()
print(value_list)