from contents import pantry

chiken_quantity = pantry.setdefault("chicken",0)
print(f"chicken: {chiken_quantity}")

beans_quantity= pantry.setdefault("beans",0)
print(f"beans: {beans_quantity}")

ketchup_quantity= pantry.get("ketchup",0)
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini","eight")
print(f"zucchini : {z_quantity}")
print()
print("`pantry` is now contains....")

for key ,value in sorted(pantry.items()):
    print(key,value)
