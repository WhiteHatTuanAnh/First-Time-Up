from turtle import*

for j in range(6,2,-1):
    if j%2 == 0:
        color("red")
    else:
        color("blue")

    for i in range(j):
        fd(100)
        lt(360/j)
