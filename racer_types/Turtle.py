from racer_types.Animal import Animal


class Turtle(Animal):
    def __new__(cls, name, steps_per_interval, interval_spacing):
        self = super(Turtle, cls).__new__(cls, name, steps_per_interval, interval_spacing)
        return self
