from turtle import *
speed(8)

def mangekant(kanter):
  vinkel = 360 / kanter
  for i in range(kanter):
    forward(40)
    left(vinkel)

mangekant(8)