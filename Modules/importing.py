import better_code
from better_code import area_square

area = better_code.area_square(40)
area = area_square(40) # for better performance --> as its lookup only once in function
print(area)


print("Global namespace")
namespace=globals().copy()

for name,obj in namespace.items():
    print(name,obj)