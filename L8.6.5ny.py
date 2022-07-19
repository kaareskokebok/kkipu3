from turtle import *

sety(100)
setheading(90)  # Retning oppover
stamp()  # Lager pilen
sety(-50)

for i in range(6):
  setx(5)
  setx(-5)
  setx(0)
  sety(ycor() + 25)  # Går oppover til neste markering