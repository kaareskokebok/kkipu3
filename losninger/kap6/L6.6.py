from turtle import *
speed(9)
penup()
backward(200)
pendown()

areal_sum = 0
for tall in range(101):
  print(tall)
  # Arealet av ett av rektanglene er tall * 1 = tall
  areal_sum += tall  # Arealet øker med høyden til søylen
  sety(tall)  # Tegner søylen
  sety(0)  # Går tilbake til x-aksen
  forward(1)
  
print("Arealet er: ")
print(areal_sum)