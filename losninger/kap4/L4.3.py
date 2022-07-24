from turtle import *
from random import randint

# Tegner omskreven sirkel
shape("circle")
u = randint(0, 180)
print(u)
A = position()

circle(75, u) 
B = position()  
stamp() 

v = randint(0, 180)
print(v)
circle(75, v)
C = position()
stamp()

circle(75, 360 - u - v)

# Tegner tilhørende trekant
goto(B)
goto(C)
goto(A)