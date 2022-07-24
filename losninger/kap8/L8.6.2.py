from turtle import *
speed(0)

# Tegner et parallellogram
print("Oppgi x-koordinaten: ")
x = float(input())
print("Oppgi y-koordinaten: ")
y = float(input())
goto(x, y)
sety(-y)
goto(0, -2 * y)
goto(0, 0)