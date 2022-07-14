from turtle import Turtle, Screen
import random

x = Turtle()
screen = Screen()

screen.screensize(600, 600)
x.pensize(10)

angles = [0, 90, 180, 270]

def colour_change():
  a = random.randint(0,1.0)
  b = random.randint(0,1.0)
  c = random.randint(0,1.0)
  x.pencolor(a, b, c)
  return

def walk():
  colour_change()
  x.right(random.choice(angles))
  x.forward(30)

for i in range(100):
  walk()