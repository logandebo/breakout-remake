from turtle import Turtle
from paddles import PADDLE_STRETCH_WIDTH, PADDLE_STRETCH_HEIGHT

BALL_SPEED = 1

BALL_STRETCH_WIDTH = 0.5
BALL_STRETCH_HEIGHT = 0.5
BALL_START_X = 0
BALL_START_Y = -160

PADDLE_LEFT_HEADING = 145
PADDLE_RIGHT_HEADING = 35
PADDLE_CENTER_LEFT_HEADING = 135
PADDLE_CENTER_RIGHT_HEADING = 45


class Ball(Turtle):

    def __init__(self, init_heading):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_STRETCH_WIDTH, stretch_len=BALL_STRETCH_HEIGHT)
        self.goto(x=BALL_START_X, y=BALL_START_Y)
        self.setheading(init_heading)

    def move(self):
        self.forward(BALL_SPEED)
        # if round(self.ycor()) % 2 != 0:
        #     self.goto(x=round(self.xcor()), y=round(self.ycor()))
        # if round(self.xcor()) % 2 == 0:
        #     self.goto(x=round(self.xcor()), y=round(self.ycor()))

    def bounce(self, ball_dir, ball_side_hit, object_type, paddle=None):

        if object_type == "block" or object_type == "wall":

            if ball_side_hit == "top":
                if ball_dir == "right":
                    self.setheading(self.heading() - self.heading() * 2)
                elif ball_dir == "left":
                    self.setheading(self.heading() + (180 - self.heading()) * 2)

            elif ball_side_hit == "left":
                if ball_dir == "up":
                    self.setheading(180 - self.heading())
                elif ball_dir == "down":
                    self.setheading(360 - (self.heading() - 180))

            elif ball_side_hit == "right":
                if ball_dir == "up":
                    self.setheading(180 - self.heading())
                elif ball_dir == "down":
                    self.setheading(-180 + self.heading() * -1)

            elif ball_side_hit == "bottom":
                if ball_dir == "right":
                    self.setheading(self.heading() + (360 - self.heading()) * 2)  # TODO: Test
                elif ball_dir == "left":
                    self.setheading(self.heading() - (self.heading() - 180) * 2)

        elif object_type == "paddle":
            if paddle.xcor() - PADDLE_STRETCH_WIDTH * 5 < self.xcor() < paddle.xcor():  # Paddle hits center left
                self.setheading(PADDLE_CENTER_LEFT_HEADING)
            elif paddle.xcor() < self.xcor() < paddle.xcor() + PADDLE_STRETCH_WIDTH * 5:  # Paddle hits Center Right
                self.setheading(PADDLE_CENTER_RIGHT_HEADING)
            elif paddle.xcor() - PADDLE_STRETCH_WIDTH * 10 < self.xcor() < paddle.xcor():
                self.setheading(PADDLE_LEFT_HEADING)
            elif paddle.xcor() < self.xcor() < paddle.xcor() + PADDLE_STRETCH_WIDTH * 10:
                self.setheading(PADDLE_RIGHT_HEADING)

    def reset_ball(self):
        self.goto(x=BALL_START_X, y=BALL_START_Y)

