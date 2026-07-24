class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area_of_rectangle(self):
        return self.length*self.width

    def perimeter_of_rectangle(self):
        return 2*(self.length+self.width)

r=rectangle(5,8)
print(r.area(area_of_rectangle))