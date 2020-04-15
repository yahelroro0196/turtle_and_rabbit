from racer_types.Animal import Animal


class Snail(Animal):
    name: str
    steps_per_interval: int
    interval_spacing: float
    starting_position: int
    passed_out_time: float
    steps_before_pass_out: int
