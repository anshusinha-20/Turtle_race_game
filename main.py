"""Turtle and Screen class is imported from the turtle module"""
from turtle import Turtle, Screen

"""tim object is created"""
tim = Turtle()

"""function to move forward by 10 paces"""
def timMoveForward():
    tim.forward(10)


"""screen object is created"""
screen = Screen()

"""a method which used to make the turtle screen listen to the keyboard and mouse events"""
screen.listen()

"""triggers an event on a keypress"""
screen.onkey(key="space", fun=timMoveForward)

"""screen will exit on click"""
screen.exitonclick()