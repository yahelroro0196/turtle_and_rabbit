from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    steps_per_interval: int
    interval_spacing: int
