def seter(rad):
  return 4*rad - 1

# Skriver ut seter på rad 1
print(seter(1))  # 3
# Antall seter flere på rad 11 enn på rad 10
print(seter(11) - seter(10))  # 4

radnr = 1
while seter(radnr) != 219:
  radnr += 1

print(radnr)  # 55