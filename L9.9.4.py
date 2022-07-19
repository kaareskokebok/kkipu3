tallA = int(input("Skriv inn et tall:"))
tallB = int(input("Skriv inn tallet du vil dele på:"))

antall = 0  # Antall ganger vi trekker tallB fra tallA
while tallA > 0:
  tallA = tallA - tallB
  antall += 1

if tallA == 0:
  print("Svaret er", antall)
elif tallA < 0:
  print("Divisjonen går ikke opp")