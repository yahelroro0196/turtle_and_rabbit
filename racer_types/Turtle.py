from racer_types.Animal import Animal


class Turtle(Animal):
    def __init__(self, name, steps_per_interval, interval_spacing):
        self.name = name
        self.steps_per_interval = steps_per_interval
        self.interval_spacing = interval_spacing
