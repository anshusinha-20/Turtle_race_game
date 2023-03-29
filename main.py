"""Turtle and Screen class is imported from the turtle module"""
import turtle
from turtle import Turtle, Screen

##### ----- #####
"""tim object is created"""
tim = Turtle()
tim.shape("turtle")

"""screen object is created"""
screen = Screen()

"""a method which used to make the turtle screen listen to the keyboard and mouse events"""
screen.listen()

##### ----- #####

##### ----- #####

# """function to move forward by 10 paces"""
# def timMoveForward():
#     tim.forward(10)
#
# """triggers an event on a keypress"""
# screen.onkey(key="space", fun=timMoveForward)
# screen.exitonclick()

##### ----- #####

##### ----- #####

"""function to draw a sketch"""

def timMakeSketch(x, y):
    def moveForward():
        tim.forward(10)

    def moveBackward():
        tim.backward(10)

    def turnRight():
        tim.right(5)

    def turnLeft():
        tim.left(5)

    def clearScreen():
        tim.clear()
        tim.penup()
        tim.home()

    screen.onkey(key="w", fun=moveForward)
    screen.onkey(key="s", fun=moveBackward)
    screen.onkey(key="a", fun=turnLeft)
    screen.onkey(key="d", fun=turnRight)
    screen.onkey(key="c", fun=clearScreen)

    screen.exitonclick()

"""function called on click"""
screen.onscreenclick(timMakeSketch, 1)
turtle.mainloop()

##### ----- #####






