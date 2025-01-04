import turtle
turtle.Screen().bgcolor("Black")
pencil = turtle.Turtle()
color = ['YellowGreen', 'Turquoise', 'Tomato']
for i in range(300):
    pencil.pencolor(color[i%3])
    pencil.forward(i * 4)
    pencil.right(121)
    pencil.speed(0)
turtle.done()