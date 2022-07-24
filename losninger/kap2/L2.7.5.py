from turtle import *
speed(0)

# Tegner de liggende rektanglene
fillcolor("brown")
for i in range(5):
# Tegn rektangelet
  begin_fill()
  forward(200)
  left(90)
  forward(30)
  left(90)
  forward(200)
  left(90)
  forward(30)
  end_fill()
  # Snu 180 grader
  left(180)
  penup()
  # Gå til nedre venstre hjørne av neste rektangel
  forward(60)
  pendown()
  right(90)

penup()
home()  # Gå til (0,0) og sett retning mot høyre
forward(15)
# Tegn det svarte rektangelet til venstre
pendown()
fillcolor("black")
begin_fill()
for i in range(2):
  forward(30)
  left(90)
  forward(270)
  left(90)
end_fill()

# Flytt pennen til neste rektangel
penup()
goto(155, 0)
pendown()
# Tegn det andre svarte rektangelet
begin_fill()
for i in range(2):
  forward(30)
  left(90)
  forward(270)
  left(90)
end_fill()