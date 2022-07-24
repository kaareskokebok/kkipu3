from turtle import *
speed(9)

side = 70
# Tegner sirkelen
fillcolor("brown")
begin_fill()
circle(side)
end_fill()
penup()
left(90)
forward(side)
pendown()

# Tegner trekant-bena
fillcolor("gold")
begin_fill()
A = position()
for i in range(8):
  forward(side)
  left(45)
  forward(side)
  goto(A)
end_fill()