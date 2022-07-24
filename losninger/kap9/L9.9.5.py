# h er høyde over bakken i m
# x er antall sekunder
def h(x):
  return -4.9*x**2 + 40*x + 1.2

tid = 0
hoyde = h(0)  # Høyden i begynnelsen

while hoyde > 0:  # Så lenge ballen er i lufta
  tid += 0.1  # Øker tiden med 0,1 sekunder
  hoyde = h(tid)  # Regn ut høyden på nytt
  # print(f"{tid}\t\t {hoyde}")  # Valgfri kodelinje

print(f"Ballen treffer bakken etter {tid:.2f} sekunder.")
# tid:.2f runder av til 2 desimaler