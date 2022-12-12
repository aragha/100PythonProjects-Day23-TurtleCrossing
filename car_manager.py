from constants import COLORS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from turtle import Turtle
from random import randint
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.carlineup = []
        self.carspeed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(COLORS[randint(0, len(COLORS) - 1)])
            car.setheading(180)
            rand_y= randint(-258, 258)
            self.penup()
            car.goto(300, rand_y)
            self.carlineup.append(car)
            self.pendown()

    def start_traffic(self):
        for i in range(0, len(self.carlineup)):
            self.carlineup[i].forward(self.carspeed)

    def level_up(self):
        # increase the speed of the cars
        self.carspeed += MOVE_INCREMENT