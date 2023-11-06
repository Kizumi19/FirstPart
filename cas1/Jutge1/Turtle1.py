import turtle

def main():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.done()

main()
