area = 0

def area_square(length: float):
    global area
    area = length * length  
    
area_square(30)
print(f'area is {area}')