from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self)->None:
    super().__init__()
    self.leftScore=0
    self.rightScore=0
    self.color("white")
    self.penup()
    self.hideturtle()
    self.goto((0,220))
    self.updateScoreboard()
    
  def updateScoreboard(self):
    self.clear()
    self.write(f"{self.leftScore} : {self.rightScore}", align="center",font=("Courier",60,"normal"))
  
  def lPoint(self):
    self.leftScore+=1
    self.updateScoreboard()

  def rPoint(self):
    self.rightScore+=1
    self.updateScoreboard()
    