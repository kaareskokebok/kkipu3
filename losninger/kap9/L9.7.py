def verdi(aar):
  return 5000*0.85**aar

kjopspris = verdi(0)
print(kjopspris)
print(verdi(5))  # Verdien etter 5 år

x = 0  # x står for antall år
while verdi(x) >= 1000:
  x += 1  # Øker antall år med 1
  print(verdi(x))  # Valgfri kodelinje

print(x)  # 10