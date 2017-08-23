from turtle import*

color("red")
rt(30)

for j in range(4):
    begin_fill()
    for i in range(2):
        fd(100)
        lt(60)
        fd(100)
        lt(120)
    end_fill()
    lt(90)

