from classes.Rabbit import Rabbit
from classes.Turtle import Turtle


def factory(racer_type, racer_name, racer_speed):
    if racer_type == "Rabbit":
        return Rabbit(racer_name, racer_speed)
    if racer_type == "Turtle":
        return Turtle(racer_name, racer_speed)
    else:
        raise NameError("Animal type invalid in racer configuration")
