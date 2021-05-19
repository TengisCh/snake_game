from turtle import Screen
from Snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Jazz")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.add_score()
        snake.extend()
        food.refresh()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.refresh()
        snake.reset()

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score.refresh()
            snake.reset()


screen.exitonclick()
