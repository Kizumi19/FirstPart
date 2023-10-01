# from turtle import *
# from yogi import read
# a = read(50)
# b = read(50)
# print(a + b)

import turtle

# Posició d'inici
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Dibuixar el quadrat
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# Parar el programa//
turtle.done()
