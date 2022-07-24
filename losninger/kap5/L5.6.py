print("Hei! Hva heter du?")
navn = input()  # La brukeren skrive inn navnet sitt
kjonn = input("Oppgi kjønn (mann/kvinne): ")

if kjonn == "kvinne":
  print("Hei, fru", navn)
else:  # Kjønnet er mann
  print("Hei, herr", navn)
