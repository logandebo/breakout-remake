import turtle
import paddles
import blocks
import ball
import random

def get_bottom_y(t_object, stretch_height):
    # print(ball.ycor())
    # print(round(t_object.ycor() - 10 * stretch_height), " bottom y")
    return t_object.ycor() - 10 * stretch_height


def get_right_x(t_object, stretch_width):
    # print(round(ball.xcor()))
    # print(round(t_object.xcor() - 10 * stretch_width), " right x")
    return t_object.xcor() - 10 * stretch_width


def get_left_x(t_object, stretch_width):
    # print(round(t_object.xcor() + 10 * stretch_width), "left x")
    return t_object.xcor() + 10 * stretch_width


def get_top_y(t_object, stretch_height):
    return t_object.ycor() + 10 * stretch_height


def ball_hit_block(chosen_ball, block, stretch_width, stretch_height):

    if ball_in_x_range_of_block(block=block, chosen_ball=chosen_ball, stretch_width=stretch_width) and \
            ball_in_y_range_of_block(block=block, chosen_ball=chosen_ball, stretch_height=stretch_height):

        return True
    else:
        return False


def ball_in_x_range_of_block(block, chosen_ball, stretch_width):
    if block.xcor() - 10 * stretch_width <= chosen_ball.xcor() <= block.xcor() + 10 * stretch_width:
        return True
    else:
        return False


def ball_in_y_range_of_block(block, chosen_ball, stretch_height):
    if block.ycor() - 10 * stretch_height <= chosen_ball.ycor() <= block.ycor() + 10 * stretch_height:
        return True
    else:
        return False




def ball_top_contact(chosen_ball, t_object, stretch_height):

    if 0 < chosen_ball.heading() < 180:
        if round(get_bottom_y(t_object=t_object, stretch_height=stretch_height)) - 2 <= round(chosen_ball.ycor()) <= round(get_bottom_y(t_object=t_object, stretch_height=stretch_height)) + 2:
            return True
    else:
        return False


def ball_right_contact(chosen_ball, t_object, stretch_width):
    if -90 < chosen_ball.heading() < 90 or 270 < chosen_ball.heading() < 450:
        if round(get_right_x(t_object=t_object, stretch_width=stretch_width)) - 2 <= round(chosen_ball.xcor()) <= round(get_right_x(t_object=t_object, stretch_width=stretch_width)) + 2:
            return True
    else:
        return False


def ball_left_contact(chosen_ball, t_object, stretch_width):
    if 90 < chosen_ball.heading() < 270 or -270 < chosen_ball.heading() < -90:
        if round(get_left_x(t_object=t_object, stretch_width=stretch_width)) - 2 <= round(chosen_ball.xcor()) <= round(get_left_x(t_object=t_object, stretch_width=stretch_width)) + 2:
            return True
    else:
        return False


def ball_bottom_contact(chosen_ball, t_object, stretch_height):
    if -180 < chosen_ball.heading() < 0 or 180 < chosen_ball.heading() < 360:
        if round(get_top_y(t_object=t_object, stretch_height=stretch_height)) - 2 <= round(chosen_ball.ycor()) <= round(get_top_y(t_object=t_object, stretch_height=stretch_height)) + 2:
            return True
    else:
        return False


def ball_hit_wall(wall_side, chosen_ball):
    if wall_side == "top":
        if chosen_ball.ycor() >= 300:
            return True
        else:
            return False

    elif wall_side == "left":
        if chosen_ball.xcor() <= -480:
            return True
        else:
            return False
    elif wall_side == "right":
        if chosen_ball.xcor() >= 470:
            return True
        else:
            return False

def random_ball_heading():
    right_or_left = random.randint(1, 2)
    if right_or_left == 1:
        return 135
    else:
        return 45




# -------------------- Object Initialization -------------------- #

# ----- Window Setup ----- #
window = turtle.Screen()
window.setup(width=960, height=600)


window.tracer(0)
# ----- Paddle Setup ----- #

paddle = paddles.Paddle()
window.onkeypress(fun=paddle.move_left, key="Left")
window.onkeypress(fun=paddle.move_right, key="Right")

# ----- Block Setup ----- #

setup_blocks = blocks.SetupBlocks(blocks_per_col=8, blocks_per_row=16)


# ----- Ball Setup ----- #
ball = ball.Ball(random_ball_heading())


window.update()
window.listen()


game_is_on = False
reset = False


while not paddle.game_is_on:
    window.update()
# ------------------- Game loop begins -------------------- #

while paddle.game_is_on:

    if ball.ycor() < -300:
        ball.reset_ball()
        paddle.goto(x=0, y=-200)
        paddle.reset = True
        ball.setheading(random_ball_heading())

        while paddle.reset:
            window.update()

    window.update()
    ball.move()

    # Tests for ball contact with block
    for block in setup_blocks.block_list:
        if ball_hit_block(chosen_ball=ball, block=block, stretch_width=blocks.BLOCK_STRETCH_WIDTH, stretch_height=blocks.BLOCK_STRETCH_HEIGHT):
            block.hideturtle()
            setup_blocks.block_list.remove(block)

            if ball_top_contact(chosen_ball=ball, t_object=block, stretch_height=blocks.BLOCK_STRETCH_HEIGHT):
                if -90 < ball.heading() < 90 or 270 < ball.heading() < 450:  # Checks if ball is moving right
                    ball.bounce(ball_dir="right", ball_side_hit="top", object_type="block")

                elif 90 < ball.heading() < 270 or -270 < ball.heading() < -90:  # Checks if ball is moving left
                    ball.bounce(ball_dir="left", ball_side_hit="top", object_type="block")

            elif ball_right_contact(chosen_ball=ball, t_object=block, stretch_width=blocks.BLOCK_STRETCH_WIDTH):
                if 0 < ball.heading() < 180:  # Moving Up
                    ball.bounce(ball_dir="up", ball_side_hit="right", object_type="block")
                elif -180 < ball.heading() < 0 or 180 < ball.heading() < 360:  # Moving Down
                    ball.bounce(ball_dir="down", ball_side_hit="right", object_type="block")

            elif ball_left_contact(chosen_ball=ball, t_object=block, stretch_width=blocks.BLOCK_STRETCH_WIDTH):
                if 0 < ball.heading() < 180:  # Moving Up
                    ball.bounce(ball_dir="up", ball_side_hit="left", object_type="block")
                elif -180 < ball.heading() < 0 or 180 < ball.heading() < 360:  # Moving Down
                    ball.bounce(ball_dir="down",ball_side_hit="left", object_type="block")

            elif ball_bottom_contact(chosen_ball=ball, t_object=block, stretch_height=blocks.BLOCK_STRETCH_HEIGHT):
                if -90 < ball.heading() < 90 or 270 < ball.heading() < 450:  # Checks if ball is moving right
                    ball.bounce(ball_dir="right", ball_side_hit="bottom", object_type="block")
                elif 90 < ball.heading() < 270 or -270 < ball.heading() < -90:  # Checks if ball is moving left
                    ball.bounce(ball_dir="left", ball_side_hit="bottom", object_type="block")

            else:
                print("Not detected")

    # Tests for ball contact with wall
    if ball_hit_wall(wall_side="top", chosen_ball=ball):  # Top wall
        if 90 < ball.heading() < 270:  # Moving Left
            ball.bounce(ball_dir="left", ball_side_hit="top", object_type="wall")
        elif -90 < ball.heading() < 90 or 270 < ball.heading() < 450:  # Moving Right
            ball.bounce(ball_dir="right", ball_side_hit="top", object_type="wall")
    elif ball_hit_wall(wall_side="left", chosen_ball=ball):  # Left wall
        if 0 < ball.heading() < 180:  # Moving Up
            ball.bounce(ball_dir="up", ball_side_hit="left", object_type="wall")
        elif -180 < ball.heading() < 0 or 180 < ball.heading() < 360:  # Moving Down
            ball.bounce(ball_dir="down", ball_side_hit="left", object_type="wall")
    elif ball_hit_wall(wall_side="right", chosen_ball=ball):  # Right wall
        if 0 < ball.heading() < 180:  # Moving Up
            ball.bounce(ball_dir="up", ball_side_hit="right", object_type="wall")
        elif -180 < ball.heading() < 0 or 180 < ball.heading() < 360:  # Moving Down
            ball.bounce(ball_dir="down", ball_side_hit="right", object_type="wall")




    # Tests for ball contact with paddle
    if ball_hit_block(chosen_ball=ball, block=paddle, stretch_width=paddles.PADDLE_STRETCH_WIDTH, stretch_height=paddles.PADDLE_STRETCH_HEIGHT):
        if 90 < ball.heading() < 270:  # Moving Left
            ball.bounce(ball_dir="left", ball_side_hit="bottom", object_type="paddle", paddle=paddle)
        elif -90 < ball.heading() < 90 or 270 < ball.heading() < 450:  # Moving Right
            ball.bounce(ball_dir="right", ball_side_hit="bottom", object_type="paddle", paddle=paddle)

    # Checks for ball out of bounds






window.exitonclick()


