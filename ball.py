from turtle import Turtle
# import math
class Ball(Turtle):
  def __init__(self)->None:
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.xmove = 10
    self.ymove = 10
    
    
  def move(self):
    newXcor = self.xcor()+self.xmove
    newYcor = self.ycor()+self.ymove
    
    self.goto((newXcor,newYcor))
    
  def bounceY(self):
    self.ymove*=-1
  
  def bounceX(self):
    self.xmove*=-1
    
  def resetPosition(self):
    self.goto((0,0))
    self.bounceX()