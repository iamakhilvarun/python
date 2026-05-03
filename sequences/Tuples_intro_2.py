albums=[("Welcome to my nightmare", "Alice cooper",1975),
        ("Bad comapany", "Bad company",1974),
        ("Nightflight","Budgie",1981),
        ("More Mayhem" , "Emilda May",2011),
        ("Ride the Lightning","Metallica",1984),
        ]
print(len(albums))

for name,artist,year in albums:
    print("Album: {} ,Artist: {}, Year: {}"
          .format(name,artist,year))

# this is not efficent
for albums in albums:
    name,artist,year=albums
    print("Album: {} ,Artist: {}, Year: {}"
          .format(name,artist,year))