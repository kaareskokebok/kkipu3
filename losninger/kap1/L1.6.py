from turtle import *
shape("turtle")
# Tegner det største øyet først
fillcolor("lightgray")
begin_fill()
circle(75)
end_fill()
# Tegner så det lyseblå øyet
fillcolor("lightblue")
begin_fill()
circle(50)
end_fill()
# Tegner deretter det lille, svarte øyet
fillcolor("black")
begin_fill()
circle(25)
end_fill()
hideturtle()