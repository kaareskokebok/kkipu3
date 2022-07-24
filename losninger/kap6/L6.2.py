aper = 4
aar = 0
print("År Aper")

for i in range(30):  # Alternativ: while-løkke
  aar += 1  # aar øker med 1
  aper *= 2  # aper dobles
  print(aar, aper)
  if aper > 5000000:  # Større enn 5 millioner
    print(f"Det tar {aar} år")  # 21
    break  # Avslutter for-løkka