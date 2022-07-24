from random import randint

print("Test deg selv i toerpotenser")
grunntall = 2
antall_riktige = 0

while antall_riktige < 5:
  eksponent = randint(-2, 5)
  print(f"{grunntall} ^ {eksponent} = ", end="")
  svar = float(input())
  fasitsvar = grunntall ** eksponent
  if svar == fasitsvar:
    print("Riktig!")
    antall_riktige += 1
  else:
    print("Ikke riktig.", end=" ")
    print("Riktig svar:", fasitsvar)

print("Gratulerer! Du har nå klart 5 riktige svar!")