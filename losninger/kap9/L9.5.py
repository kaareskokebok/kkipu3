def avstand_sara(tid):
  return 400 - 1.4*tid

def avstand_pia(tid):
  return 600 - 4.2*tid

print("Tid(s) Avstand(m)")
for tiden in range(75):
  avstand_mellom = avstand_pia(tiden) - avstand_sara(tiden)
  print(f"{tiden:<6} {avstand_mellom}")
# Leser fra tabell: mellom 71 og 72 sekunder