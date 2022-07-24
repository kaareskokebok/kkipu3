def regn_ut_pris(antall_kopper):
  return antall_kopper * pris_per_kopp

pris_per_kopp = 40
print("Kopper Pris(kr)")
for kopper in range(1, 11):
  pris = regn_ut_pris(kopper)
  print(f"{kopper:<6} {pris}")  # 400 kr for 10 kopper