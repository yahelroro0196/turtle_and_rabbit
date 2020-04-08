from dataclasses import dataclass


@dataclass
class Round:
    number: int
    track_length: int
    racers: list
