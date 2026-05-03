welcome ="Welcome to my nightmare", "Alice cooper",1975
bad= "Bad comapany", "Bad company",1974
budgie="Nightflight","Budgie",1981
imelda="More Mayhem" , "Emilda May",2011
metallica = "Ride the Lightning","Metallica",1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# # metallica[0]="Master of puppets"# here we cant change it cause tuples are immutable

# metallica2 =list(metallica)
# print(metallica2)

# metallica2[0]="Master of puppets"# here list are mutable so we can change it using index 
# print(metallica2) 

title,artist,year=metallica
print(title,artist,year)

table=("coffee table",200,100,75,34.50)
print(table[1]*table[2])

name,lenght,width,height,price=table
print(lenght*width)