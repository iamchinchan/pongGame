from turtle import Turtle
RIGHTPADDLE={
  "position":(350,0)
}
LEFTPADDLE={
  "position":(-350,0)
}
class Paddle(Turtle):
  def __init__(self,position)->None:
    super().__init__()
    # print("printing")
    self.shape("square")
    self.shapesize(stretch_len=5,stretch_wid=1)
    self.color("white")
    self.setheading(90)
    self.penup()
    if(position=="left"):
      self.goto(LEFTPADDLE["position"])
    elif position=="right":
      self.goto(RIGHTPADDLE["position"])
  
  def up(self):
    self.forward(20)
    
  def down(self):
    self.backward(20)