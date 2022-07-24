from turtle import *
shape("turtle") 
speed(6)

# Tegner pizzabitene
for i in range(8):
  forward(150)
  backward(150)
  left(45)

# Tegner sirkelen
forward(150)
left(90)
circle(150)