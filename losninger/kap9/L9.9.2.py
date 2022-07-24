def beregn_pris(antall_venner):
  return 9000 / antall_venner

print("Antall venner Pris per venn")

for venner in range(1, 9):
  pris = beregn_pris(venner)
  print(f"{venner:<13} {pris:.2f}")
