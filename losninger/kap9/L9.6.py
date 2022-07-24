def f(x):
  return x**2 - 2*x + 3

# To variabler for koordinatene til bunnpunktet
minst = f(-4)  # y-koordinaten
x_minst = -4  # x-koordinaten

for i in range(-3, 5):
  y = f(i)
  if y < minst:
    minst = y
    x_minst = i

print("Bunnpunktet er:")
print(f"({x_minst}, {minst})")  # (1, 2)