from turtle import *
speed(0)

def kvadrat(side): 
  for i in range(4):
    forward(side)
    left(90)

sidelengde = 200  # Sidelengden starter på 200
while sidelengde > 10:
  kvadrat(sidelengde)
  endring = sidelengde * 0.03
  sidelengde -= endring
  setheading(45)
  forward(endring * 0.707)  # Faktoren er sqrt(2)/2
  setheading(0)