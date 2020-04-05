from classes.Rabbit import Rabbit
from classes.Turtle import Turtle


def factory(racer_type, racer_properties):
    if racer_type == "Rabbit":
        return Rabbit(*racer_properties)
    if racer_type == "Turtle":
        return Turtle(*racer_properties)
    else:
        raise NameError("Animal type invalid in racer configuration")
