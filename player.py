from turtle import Turtle
from constants import STARTING_POSITION, MOVE_DISTANCE, FINISH_LINE_Y

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        # self.goto(STARTING_POSITION)
        self.go_to_start()
        self.setheading(90)

    def go_up(self):

        curr_x = self.xcor()
        curr_y = self.ycor()
        if self.ycor() < FINISH_LINE_Y:
            curr_y += MOVE_DISTANCE
        else:
            print(f"Other side reached: {curr_x}, {curr_y}")
        print(f"Current player location: {curr_x}, {curr_y}")
        self.goto(curr_x, curr_y)
        # print(self.ycor())


    def go_down(self):

        curr_x = self.xcor()
        curr_y = self.ycor()
        if self.ycor() > STARTING_POSITION[1]:
            curr_y -= MOVE_DISTANCE
        else:
            print(f"Starting point reached: {curr_x}, {curr_y}")
        print(f"Current player location: {curr_x}, {curr_y}")
        self.goto(curr_x, curr_y)

    def is_at_finish_line(self):
        if self.ycor() < FINISH_LINE_Y:
            return False
        else:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)