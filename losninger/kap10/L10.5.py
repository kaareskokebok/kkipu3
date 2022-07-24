from random import choice

kuler = 3*["r"] + 2*["b"]
print(kuler)
antall_minst1rod = 0
antall_forsok = 10
print("Kule1 Kule2")

for i in range(antall_forsok):
  kule1 = choice(kuler)  # Velg en kule tilfeldig
  kule2 = choice(kuler)
  print(kule1, "   ", kule2)
  if kule1 == "r" or kule2 == "r":
    antall_minst1rod += 1

print(f"Minst én rød: {antall_minst1rod} ganger")
p = antall_minst1rod / antall_forsok
print(f"Beregnet sannsynlighet: {p}")  # Nær 21/25