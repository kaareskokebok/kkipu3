from random import randint

kast1 = randint(1, 6)
kast2 = randint(1, 6)
print(kast1, kast2)

if kast1 == kast2:
  print("To like!")
else:
  print(f"{kast1} og {kast2}, to ulike.")