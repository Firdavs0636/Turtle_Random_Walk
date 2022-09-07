import random
from random import randint
import turtle
from turtle import Screen

downy = turtle.Turtle()
turtle.colormode(255)
downy.speed(8)
direction = ["forward", "back", "left", "right"]

screen = Screen()
while True:
    downy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    downy.[random.choice(direction)](10)
    downy.forward(10)
    downy.right(72)
    downy.forward(10)
    downy.left(72)
    downy.back(10)
    downy.forward(10)













