from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        snake = Turtle("square")
        snake.penup()
        snake.goto(pos)
        snake.color("white")
        self.snake_body.append(snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            front_pos = self.snake_body[segment - 1].pos()
            self.snake_body[segment].goto(front_pos)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
