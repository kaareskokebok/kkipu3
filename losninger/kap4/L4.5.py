from time import sleep
from turtle import *
from random import randint
shape("circle")
speed(1)

while True:
  left(randint(0, 359))
  forward(30)
  sleep(randint(0, 3))
  if distance(home) > 140:
    Screen().bgcolor("red")
    print("Kom hjem!")
    home()
    break
  elif distance(home) > 80:
    Screen().bgcolor("yellow")
    print("Mild advarsel")
  else:
    Screen().bgcolor("green")
