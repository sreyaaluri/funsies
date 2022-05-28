from turtle import *

color("blue")
tracer(5)
bgcolor("black")
for i in range(100):
  circle(i-185)
  right(91)
for i in range(140):
  tracer(70)
  circle(i-185)
  right(91)
for i in range (600):
  penup()
  setpos(0, 0)
  pendown()
  tracer(78)
  color("violet")
  forward(200)
  right(98)