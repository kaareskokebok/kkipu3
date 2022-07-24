from turtle import *
speed(9)

def trekant(side):
  for i in range(3):
    forward(side)
    left(120)

lengde = 300
for i in range(7):
  trekant(lengde)
  lengde /= 2  # Halverer lengden
  forward(lengde)
  left(60)