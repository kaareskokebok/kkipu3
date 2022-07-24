from random import randint
from time import sleep

while True:
  prosent = randint(0, 100)  # Tilfeldig tall fra 0 til 100
  vekstfaktor = 1 + prosent / 100
  vekstfaktor = round(vekstfaktor, 2)  # Avrunder til 2 desimaler
  print(f'Bestem vekstfaktoren til {prosent} % økning')
  svar = input().replace(',', '.')  # Erstatter , med .
  svar = float(svar)  # Konverterer til et desimaltall
  if svar == vekstfaktor:
    print('Riktig svar!')
  else:
    print(f'Feil svar. Rett svar var {vekstfaktor}')
  sleep(1)