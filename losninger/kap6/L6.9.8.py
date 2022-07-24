from turtle import *
speed(6)
# Tegner det store rektangelet
for i in range(2):
  forward(100)
  left(90)
  forward(60)
  left(90)

forward(25)
# Tegner trekantene
fillcolor("red")
begin_fill()
y = 0
x = 25
for i in range(5):
  y += 6
  x += 15
  goto(x, y)
  y += 6
  x -= 15
  goto(x, y)

# Fullfører den røde delen av flagget
forward(75)
right(90)
forward(60)
right(90)
forward(75)
end_fill()
hideturtle()