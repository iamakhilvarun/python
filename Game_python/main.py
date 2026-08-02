from enemy import Enemy, Troll,Vampire,Vampire_king
ugly_troll = Troll("pug")
print(f"ugly troll - {ugly_troll}")

another_troll = Troll("ug")
print(f"Another troll - {another_troll}")


brother_troll =Troll("nig")
print(brother_troll)

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()


monster=Troll("Basic Enemy")
monster.grunt()

monster.take_damage(10)
print(monster)

vamp=Vampire("Dracula")
print(vamp)

vamp.take_damage(23)
print(vamp)

print("--------------------------")

# while vamp.alive:
#     if not vamp.dodges():
#         vamp.take_damage(1)
        # print(vamp)

vamp._lives=1
vamp._hit_points=1
print(vamp)

Boss=Vampire_king("rimuru")
print(Boss)
while Boss._alive:
    Boss.take_damage(70)
    print(Boss)