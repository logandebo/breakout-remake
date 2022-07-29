from turtle import Turtle


BLOCK_STRETCH_WIDTH = 3
BLOCK_STRETCH_HEIGHT = 1
PIXELS_BETWEEN_BLOCKS = 4


# class Blocks(Turtle):
#
#     def __init__(self):
#         super().__init__()


class SetupBlocks:

    def __init__(self, blocks_per_row, blocks_per_col, block_amount=None):
        self.block_list = []
        for row in range(0, blocks_per_col - 1):
            if block_amount is not None:
                if len(self.block_list) == block_amount:
                    break

            for col in range(0, blocks_per_row - 1):
                block = Turtle()
                block.penup()
                block.setheading(90)
                block.shape("square")
                block.pencolor("white")
                block.shapesize(stretch_wid=BLOCK_STRETCH_WIDTH, stretch_len=BLOCK_STRETCH_HEIGHT)
                block.goto(x=(-480 + BLOCK_STRETCH_WIDTH * 10), y=(256 - BLOCK_STRETCH_HEIGHT * 10))
                block.goto(x=(block.xcor() + (col * BLOCK_STRETCH_WIDTH * 20) + col * PIXELS_BETWEEN_BLOCKS), y=(block.ycor() - (row * BLOCK_STRETCH_HEIGHT * 20) - row * PIXELS_BETWEEN_BLOCKS))
                self.block_list.append(block)

                if block_amount is not None:
                    if len(self.block_list) == block_amount:
                        break


