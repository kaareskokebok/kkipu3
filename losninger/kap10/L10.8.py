from turtle import *
from random import random
from time import sleep

treff = 0.6
penup()
hideturtle()

# Tegn blinkene
for i in range(5):
  dot(20)
  forward(40)

home()  # Gå tilbake

# Skyt 5 skudd
for i in range(5):
  sleep(2)
  if random() < treff:
    print("treff")
    dot(10, "white")
  else:
    print("bom")
    dot(10, "red")
  forward(40)