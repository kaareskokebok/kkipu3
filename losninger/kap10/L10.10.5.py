from random import choice

antall_like = 0
antall_forsok = 1000

for i in range(antall_forsok):
  nonstop = 5*["r"] + 3*["g"]
  nonstop1 = choice(nonstop)
  nonstop.remove(nonstop1)
  nonstop2 = choice(nonstop)
  nonstop.remove(nonstop2)
  if nonstop1 == nonstop2:
    print("To like!")
    antall_like += 1
  else:
    print("En av hver")

p = antall_like / antall_forsok
print(f"Sannsynlighet for to like: {p}")