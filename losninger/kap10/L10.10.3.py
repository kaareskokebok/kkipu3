from random import randint

antall_barn = 0

for i in range(9999):
  gravid = randint(1, 100)
  antall_barn += 1
  if gravid == 100:  # Tvillinger, 1 av 100
    antall_barn += 1  # Teller det ekstra barnet
    break

print(f"Antall barn: {antall_barn}")