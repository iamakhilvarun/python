D={"Name":"Akhil","Gender":"Male","Age":"21"}

d1={key:value for key,value in D.items() if len(key)>3}
print(d1)

l=[1,2,3,4,5,6]
d2={item:item**2 for item in l}
print(d2)

d3={item:item**2 for item in l if item %2==0}
print(d3)