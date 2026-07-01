def area_square(length:float)->float:
    area= length * length
    return area

if __name__ == '__main__':
    area= area_square(30)
    print(f'area is {area}')

    print(f'in better_code.py,__name__ is {__name__}')