import turtle
from yogi import read

def main():
    c = read(int)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(c)
        turtle.left(90)
    turtle.done()

main()
