from random import randint

for i in range(10):
  tallA = randint(0, 10)4
  tallB = randint(0, 10)
  fasitsvar = tallA * tallB
  print(f"{tallA} * {tallB} = ")
  brukersvar = int(input("Svar: "))
    
  if brukersvar == fasitsvar:
    print("Riktig svar")
  else:
    print("Feil svar")