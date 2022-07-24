pris_per_kopp = 40
print("Hvor mange kopper kaffe ønsker du?")
kopper = int(input())  # Vi konverterer inndata til et heltall
pris = pris_per_kopp * kopper
print(f"Pris: {pris} kr")