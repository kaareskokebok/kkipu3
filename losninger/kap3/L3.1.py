from turtle import *

# Oppskriften på et smil
def smil():
  setheading(-90)  # Sett retning nedover (sør)
  circle(50, 180)  # Tegn en halvsirkel med radius 50

def sur():
  setheading(90)
  circle(50, 180)

smil()
smil()
forward(100)
left(90)
forward(400)
left(90)
forward(100)
smil()
smil()