from turtle import *
from random import randint
speed(0)

circle(95)
for i in range(100):
  circle(95, randint(0, 180))
  A = position()
  circle(95, randint(0, 180))
  B = position()
  goto(A)
  goto(B)