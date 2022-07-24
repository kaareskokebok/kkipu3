from random import randint

antall_kast = 0
antall_seksere = 0

while antall_kast < 5000:
  kast = randint(1, 6)
  antall_kast += 1
  if kast == 6:
    antall_seksere += 1
  print(antall_seksere / antall_kast)

print(f"Antall kast: {antall_kast}")
print(f"Antall seksere: {antall_seksere}")