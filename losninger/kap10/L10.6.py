from random import choice

for i in range(100):
  kuler = 2*["b"] + 3*["r"] + 4*["g"]
  kule1 = choice(kuler)
  kuler.remove(kule1)
  kule2 = choice(kuler)
  kuler.remove(kule2)
  if kule2 != "g":
    print(kule1, kule2)  # 6 forskjellige utfall