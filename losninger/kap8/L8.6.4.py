from turtle import *

Screen().setup(300, 50)
Screen().bgcolor("lightgreen")
shape("turtle")
penup()

fart = 0.5
x = 0  # Skilpadda begynner i (0, 0)

while True:
  x = x + fart  # Øker x med fart
  setx(x)
  if x > 135:  # Kollisjon høyre vegg
    fart = -0.5  # Snur fartsretningen
    setheading(180)
  elif x < -135:  # Kollisjon venstre vegg
    fart = 0.5
    setheading(0)