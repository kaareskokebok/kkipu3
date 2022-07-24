from turtle import *
speed(0)

A = (-100, -100)
penup()
goto(A)

# Tegn vannrette linjer
for i in range(6):
  pendown()
  setx(100)
  setx(-100)
  penup()
  sety(ycor() + 40)  # Øker y med 40
  
goto(A)  # Gå til (-100, -100)

# Tegn loddrette linjer
for i in range(6):
  pendown()
  sety(100)
  sety(-100)
  penup()
  setx(xcor() + 40)  # Øker x med 40