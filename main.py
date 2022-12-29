from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Score,Border

screen = Screen()
screen.bgcolor("#42f5e0")
screen.setup(width=650, height=650)

screen.title("Harsh's snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
border = Border()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_movement()
    for segment in snake.segments:
        segment.speed("fastest")


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_scoreboard()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

        # is_game_on = False
        # score.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # is_game_on = False
            # score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()