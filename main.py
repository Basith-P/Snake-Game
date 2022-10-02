from turtle import Screen
import time

from snake import Snake

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()

game_over = False

while not game_over:
    s.update()
    time.sleep(.1)

    snake.move()

s.exitonclick()
