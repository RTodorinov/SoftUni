import turtle

t = turtle.Pen()
turtle.bgcolor('black')

COLOR_COUNT = 6

for x in range(360):
    if x % COLOR_COUNT == 0:
        t.pencolor("red")
    elif x % COLOR_COUNT == 1:
        t.pencolor("purple")
    elif x % COLOR_COUNT == 2:
        t.pencolor("blue")
    elif x % COLOR_COUNT == 3:
        t.pencolor("green")
    elif x % COLOR_COUNT == 4:
        t.pencolor("orange")
    elif x % COLOR_COUNT == 5:
        t.pencolor("yellow")

    t.width(x // 100 + 1)  # прави размера на химикала по-дебел
    t.forward(x)
    t.left(59)
