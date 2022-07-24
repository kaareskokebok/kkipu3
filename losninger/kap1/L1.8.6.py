from turtle import *
shape("turtle")

# Tegner det ytre kvadratet
fillcolor("red")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

# Tegner sirkelen
fillcolor("black")
goto(50, 0)
begin_fill()
circle(50)
end_fill()

# Tegner det indre kvadratet
fillcolor("gold")
goto(50, 0)
begin_fill()
goto(100, 50)
goto(50, 100)
goto(0, 50)
goto(50, 0)
end_fill()
hideturtle()
done()