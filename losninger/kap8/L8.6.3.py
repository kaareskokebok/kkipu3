from math import sqrt
from turtle import *
speed(0)

print("Oppgi x-koordinaten: ")
x = float(input())
print("Oppgi y-koordinaten: ")
y = float(input())
goto(x, y)

avstand = sqrt(x**2 + y**2)
print("Avstand til punktet: ")
print(avstand)