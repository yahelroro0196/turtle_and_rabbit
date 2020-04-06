from classes.Animal import Animal


class Turtle(Animal):
    def __init__(self, name, speed, step_interval):
        super().__init__(name, speed, step_interval)
