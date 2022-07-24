summen = 0
for rutenr in range(64):
  ris = 2 ** rutenr
  summen += ris
  # print(ris)
# print(summen)

antall_mennesker = 8 * 10**9
vekt_per_riskorn = 1/64 * 10**-3  # Enhet: kg/riskorn
rismengde = vekt_per_riskorn * summen  # Enhet: kg
rismengde_per_menneske = rismengde / antall_mennesker
svar = f"{rismengde_per_menneske:.1f}"
print(f"Det blir {svar} kilo ris per menneske")  # 36028.8