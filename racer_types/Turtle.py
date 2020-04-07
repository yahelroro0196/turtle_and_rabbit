from dataclasses import dataclass
from racer_types.Animal import Animal


@dataclass
class Turtle(Animal):
    name: str
    steps_per_interval: int
    interval_spacing: float
