area = 0
length=30
def area_square(length: float):
    global area
    area = length * length  
    
area_square(length)
print(f'area is {area}')