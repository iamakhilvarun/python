shopping_list= ("milk",
                "pasta",
                "eggs",
                "spam",
                "bread",
                "rice"
                )
another_list=shopping_list
print(id(shopping_list))
print(id(another_list)) 

shopping_list +=("cookies")
print(shopping_list)
print(id(shopping_list))#here we see the id same we add objects to the list but it doesnt change the id so it is mutable
print(another_list)

a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream")# appending means to add here b which we are adding to 
                # (.) is the symbol for dot notation and aftere append which is a method then (parenthesis)--> the thing we are adding
print(c)
print(d)