from turtle import *
shape("turtle")
speed(5)

# Tegner trapp opp
for i in range(5):
  left(90)
  forward(25)
  right(90)
  forward(50)

# Går litt forover
forward(50)
# Tegner trapp ned
for i in range(5):
  forward(50)
  right(90)
  forward(25)
  left(90)