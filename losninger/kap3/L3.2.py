from turtle import *
speed(9)

def kvadrat():
  for i in range(4):
    forward(50)
    right(90)

for i in range(8):
  kvadrat()
  forward(120)
  left(45)