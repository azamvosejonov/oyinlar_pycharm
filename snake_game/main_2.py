# from turtle import  Screen
# import time
# from snace_2 import Snake
# from food_2 import Food
# from scoreboard_2 import Scoreboard
#
#
# screen=Screen()
# screen.title("Snake Game")
# screen.tracer(0)
# screen.setup(600,600)
# screen.bgcolor("black")
#
# #action
# snake=Snake()
# food=Food()
# score=Scoreboard()
#
# screen.listen()
#
# screen.onkey(snake.up,"w")
# screen.onkey(snake.down,"s")
# screen.onkey(snake.right,"d")
# screen.onkey(snake.left,"a")
#
# screen.onkey(snake.up,"Up")
# screen.onkey(snake.down,"Down")
# screen.onkey(snake.right,"Right")
# screen.onkey(snake.left,"Left")
#
#
#
# game_is_on=True
# while game_is_on:
#     screen.update()
#     time.sleep(0.2)
#     snake.move()
#
#     if snake.segments[0].distance(food) < 15:
#         food.random_distance()
#         score.add_score()
#         snake.extend()
#
#     if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or  snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
#         score.game_over()
#         game_is_on=False
#
#
#     for segment in snake.segments[1:]:
#         if snake.segments[0].distance(segment) < 10:
#             score.game_over()
#             game_is_on=False
#
#
#
#
#
#
#
#
#
# screen.exitonclick()