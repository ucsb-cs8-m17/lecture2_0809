import turtle

twochains = turtle.Turtle()

def drawSquare():
  for i in range(4):
    twochains.forward(100)
    twochains.left(90)

drawSquare()

twochains.up()

twochains.goto(-200,-200)
twochains.down()

drawSquare()
