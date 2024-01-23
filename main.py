from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# creating paddles for the game
leftPaddle = Paddle("left")
rightPaddle = Paddle("right")
ball = Ball()
# ball2 = Ball()
# ball2.penup()
# ball2.goto((330,250))
# starting listening for the 
# screen.update()
# screen.tracer(1)
screen.listen()
# time.sleep(1)
# leftPaddle.forward(20)

# listening to events, these 4 are for moving paddles up and down
screen.onkeypress(key="w",fun=leftPaddle.up)
screen.onkeypress(key="s",fun=leftPaddle.down)
screen.onkeypress(key="Up",fun=rightPaddle.up)
screen.onkeypress(key="Down",fun=rightPaddle.down)


isGameOn = True
while isGameOn:
  time.sleep(.1)
  screen.update()
  # checking collision with upper or lower wall and changing Ydirection
  if ball.ycor()>280 or ball.ycor()<-280:
    ball.bounceY()
    
  # checking collision with right paddle and left paddle
  if ball.xcor()>320 and ball.xcor()<340 and ball.distance(rightPaddle)<61.36 or ball.xcor()<-320 and ball.xcor()>-340 and ball.distance(leftPaddle)<61.36:
      # print(f"xcor is : {ball.xcor()}, ycor is: {ball.ycor()}, distance is {ball.distance(rightPaddle)}")
      # print(f"ball was moving in {ball.xmove} direction")
      ball.bounceX()
      # print(f"now ball is moving in {ball.xmove} direction\n")
      
  # check if right paddle missed the ball
  if ball.xcor()>370:
    ball.resetPosition()
  
  # check if left paddle missed the ball
  if ball.xcor()<-370:
    ball.resetPosition()
  ball.move()
  

    
    
screen.exitonclick()
