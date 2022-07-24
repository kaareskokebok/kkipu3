from turtle import *
shape("turtle")
# Tegner romben
penup()
goto(100, 0)
pendown()
goto(0, 100)
goto(-100, 0)
goto(0, -100)
goto(100, 0)

# Tegner kvadratet
goto(100, 100)
goto(-100, 100)
goto(-100, -100)
goto(100, -100)
goto(100, 0)
hideturtle()