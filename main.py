import time
from turtle import Screen
from player import Player

from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
carmanager = CarManager()
scoreboard = Scoreboard()
# for i in carmanager.carlineup:
#     print(carmanager.carlineup)

screen.onkey(key="Up", fun=player.go_up)
screen.onkey(key="Down", fun=player.go_down)
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.start_traffic()
    scoreboard.update_scoreboard()
    for car in carmanager.carlineup:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
#     detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()

screen.exitonclick()