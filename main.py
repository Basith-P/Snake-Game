from turtle import Screen, Turtle
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

initial_pos = [(0, 0), (-20, 0), (-40, 0)]

blocks = []

for i in initial_pos:
    new_block = Turtle("square")
    new_block.penup()
    new_block.color("white")
    new_block.goto(i)
    blocks.append(new_block)


game_over = False

while not game_over:
    s.update()
    time.sleep(.1)

    for block_index in range(len(blocks)-1, 0, -1):
        new_x = blocks[block_index - 1].xcor()
        new_y = blocks[block_index - 1].ycor()
        blocks[block_index].goto(new_x, new_y)
    blocks[0].forward(20)

s.exitonclick()
