from typing import NamedTuple


class Animal(NamedTuple):
    name: str
    steps_per_interval: int
    interval_spacing: float
    starting_position: int
    passed_out_time: float = 0.0
    steps_before_pass_out: int = 0
