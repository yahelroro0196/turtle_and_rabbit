from racer_types.Rabbit import Rabbit
from racer_types.Turtle import Turtle


def factory(racer_type, racer_properties):
    options = _initialize_options()
    try:
        return options[racer_type](*racer_properties)
    except KeyError:
        print("{} not in supported animals".format(racer_type))


def _initialize_options():
    return {
        "Rabbit": Rabbit,
        "Turtle": Turtle
    }
