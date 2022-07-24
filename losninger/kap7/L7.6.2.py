tallnummer = 1
kubikktall = tallnummer ** 3
while kubikktall < 1000000:
  print(kubikktall)
  tallnummer += 1
  kubikktall = tallnummer ** 3
print(tallnummer)  # 100