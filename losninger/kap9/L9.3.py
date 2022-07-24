def y(x):
  return 500 / x 

okter = 1
pris = y(okter)

while pris >= 15:
  okter += 1
  pris = y(okter)
  print(pris)

print(okter)  # 34 treningsøkter