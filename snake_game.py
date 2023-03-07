from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time



screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake=Snake()  #this will call the init func which will call the create_snake method
food=Food()
scoreboard=Scoreboard()


screen.listen()  #to start listen to keystrokes

screen.onkey(snake.up,"Up") #keybinding
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




is_game_on=True

#moving_snake

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on=False
        scoreboard.gameover()
    
    # detect collion with tail
    for segment in snake.segments[1:]:  # getting all the segments except head using slicing
        if snake.head.distance(segment) < 10 :
            is_game_on=False
            scoreboard.gameover()  
    







screen.exitonclick()