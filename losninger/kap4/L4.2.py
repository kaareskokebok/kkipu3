from turtle import *
from random import randint
speed(2)

# Tegner vinkel v
vinkel_v = randint(20, 130) 
print(vinkel_v)
forward(100)
backward(100)
left(vinkel_v)
forward(100)

# Tegner vinkel u
backward(100)
vinkel_u = 180 - vinkel_v
print(vinkel_u)
left(vinkel_u)
forward(100)