from random import randint
from math import sqrt

tall = randint(1, 101)
fasit = sqrt(tall)
fasit = round(fasit, 1)
print(f"Gjett på kvadratroten til {tall}: ")

while True:
  gjett = float(input())
  #print(f"Du gjettet {gjett} og fasit var {fasit}.")
  if gjett < fasit:
    print("Du gjettet for lavt. Prøv igjen.")
  elif gjett > fasit:
    print("Du gjettet for høyt. Prøv igjen.")
  else:
    print("Du gjettet helt riktig.")
    break