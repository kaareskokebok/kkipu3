print("Beløp i NOK: ")
nokbelop = float(input())
kurs = 9.83
usdbelop = nokbelop / kurs
usdbelop = round(usdbelop, 2)
print(f"Beløp i USD: {usdbelop}")