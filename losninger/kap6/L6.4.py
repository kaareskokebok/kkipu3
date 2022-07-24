nevner = 2  # Den første nevneren er 2
summen = 0
for i in range(60):
  figurtall = 1 / nevner
  summen += figurtall
  print(summen)  # Summen nærmer seg 1
  nevner *= 2