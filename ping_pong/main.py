from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from hisob import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)
screen.title("Ping Pong game")


screen.listen()
l_paddle=Paddle((-380,0))
r_paddle=Paddle((380,0))
ball=Ball()
scoreboard=Scoreboard()

screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')


screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
scoreboard.update_socreboard()






game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()






    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.xcor()>405 or ball.xcor()<-405:
        ball.bounce_x()
    if ball.xcor()>400:
        scoreboard.add_score1()

    if ball.xcor()<-400:
        scoreboard.add_score2()






    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()









screen.exitonclick()
