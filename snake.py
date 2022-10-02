from turtle import Turtle

INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for i in INITIAL_POS:
            new_block = Turtle("square")
            new_block.penup()
            new_block.color("white")
            new_block.goto(i)
            self.blocks.append(new_block)

    def move(self):
        for block_index in range(len(self.blocks)-1, 0, -1):
            new_x = self.blocks[block_index - 1].xcor()
            new_y = self.blocks[block_index - 1].ycor()
            self.blocks[block_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
