from random import choice

antall_biler = 0
antall_forsok = 1000

for i in range(antall_forsok):
  dorer = ["geit", "geit", "bil"]
  valg = choice(dorer)  # Du velger tilfeldig en dør
  # print(valg)
  dorer.remove("geit")  # Spillverten åpner en geite-dør
  dorer.remove(valg)    # Fjern det opprinnelige valget
  valg = choice(dorer)  # Velg den døra som står igjen
  if valg == "bil":
    antall_biler += 1
  print(f"Du vant en {valg}")

print(f"Antall biler vunnet: {antall_biler}")
p = antall_biler / antall_forsok 
print(f"Vinner-rate: {p}")  # Nært brøken 2/3