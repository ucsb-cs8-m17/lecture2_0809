import turtle

twochains = turtle.Turtle()

def drawShape():
  for i in range(3):
    twochains.forward(200)
    twochains.left(120)

drawShape()

twochains.up()

twochains.goto(-200,-200)
twochains.down()

drawShape()
