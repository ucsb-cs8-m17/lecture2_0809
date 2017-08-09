import turtle

twochains = turtle.Turtle()

def drawShape(sides):
  for i in range(sides):
    twochains.forward(50)
    twochains.left(360/sides)

def upMoveDown(x,y):
  twochains.up()
  twochains.goto(x,y)
  twochains.down()

drawShape(3)

upMoveDown(-200,200)

drawShape(5)

upMoveDown(-200,-200)

drawShape(27)

upMoveDown(200,-200)


