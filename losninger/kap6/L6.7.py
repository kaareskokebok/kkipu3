from turtle import *
speed(8)
fillcolor("orange")

def rektangel(bredde, lengde):
  begin_fill()  # Start fyllfarge
  for i in range(2):
    forward(bredde)
    left(90)
    forward(lengde)
    left(90)
  end_fill()  # Slutt fyllfarge

lengde = 20
for i in range(8):
  rektangel(10, lengde)
  penup()
  forward(20)
  pendown()
  lengde += 30