from racer_types.Animal import Animal


class Rabbit(Animal):
    def __new__(cls, name, steps_per_interval, interval_spacing):
        self = super(Rabbit, cls).__new__(cls, name, steps_per_interval, interval_spacing)
        return self
