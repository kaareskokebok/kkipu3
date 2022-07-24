from turtle import *

def tegn_xAkse():
  dot(10)  # Tegner et punkt der x = 0
  setx(-220)
  setx(220)
  stamp()  # Plasserer pilen til x-aksen
  home()

# Setter opp skjermen
Screen().setup(500, 50)  # Bredde 500 og høyde 50
Screen().bgcolor("pink")

tegn_xAkse()  # Utfører kodelinjene 4 til 8
penup()  # Prøv uten penup() for å se effekten

for i in range(5):
  print("Oppgi x-koordinat (-200 til 200):")
  x_koord = int(input())
  setx(x_koord)
  if x_koord < 0:
    dot(10, "red")
  else:  # Tegn blå sirkel dersom x er positiv
    dot(10, "blue")

hideturtle()