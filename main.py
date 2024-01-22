from turtle import Screen
from paddle import Paddle
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# creating paddles for the game
leftPaddle = Paddle("left")
rightPaddle = Paddle("right")

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
  screen.update()
screen.exitonclick()
