from turtle import Turtle

PADDLE_STRETCH_WIDTH = 8
PADDLE_STRETCH_HEIGHT = 1


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_STRETCH_WIDTH, stretch_len=PADDLE_STRETCH_HEIGHT)
        self.goto(x=0, y=-200)

        self.game_is_on = False
        self.reset = False





    def move_left(self):
        if self.xcor() > -400:
            self.setx(self.xcor() - 20)
            self.game_is_on = True
            self.ball_start_heading = 135
            self.reset = False

    def move_right(self):
        if self.xcor() < 400:
            self.setx(self.xcor() + 20)
            self.game_is_on = True
            self.ball_start_heading = 45
            self.reset = False
