from turtle import Screen, Turtle

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")

initial_pos = [(0, 0), (-20, 0), (-40, 0)]


for i in initial_pos:
    new_block = Turtle("square")
    new_block.penup()
    new_block.color("white")
    new_block.goto(i)


s.exitonclick()
