from turtle import *

def tegn_yAkse():
  left(90)
  sety(-120)
  sety(150)
  stamp()

tegn_yAkse()
sety(0)
sety(-120)  # Flytter pilen nederst på y-aksen
setheading(0)  # Setter retning mot høyre

for i in range(13):
  pendown()
  y = ycor()  # Lagrer y-koordinaten i variabelen y
  if y < 0:
    color("red")
  else:  # Blå farge dersom y er positivt
    color("blue")
  forward(y)
  backward(y)
  penup()
  sety(y + 20)  # Øker y-koordinaten med 20

hideturtle()