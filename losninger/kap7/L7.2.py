print("Utforskning av tierpotenser.")
print()  # Lager en blank linje
grunntall = 10
for eksponent in range(-15, 0):
  potens = grunntall ** eksponent
  svar = f"{potens:.15f}"
  #svar = f"{potens:.{-eksponent}f}"  # Gir et vakrere resultat
  svarsetning = f"{grunntall} ^ {eksponent:3d} = {svar}"
  print(svarsetning)
