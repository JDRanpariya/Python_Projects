import turtle


def draw_bag():
    turtle.shape('turtle')
    turtle.pen(pencolor='green', pensize=3)
    turtle.penup()
    turtle.goto(-35, -35)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)


if __name__ == "__main__":
    turtle.setworldcoordinates(-70, -70, 70, 70)
    draw_bag()
    turtle.mainloop()
