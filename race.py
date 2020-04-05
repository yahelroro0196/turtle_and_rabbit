from animal_factory import factory
from constants import ANIMAL_TYPE, ANIMAL_SPEED, READ
import json


def race(config):
    racers = _initialize_racers(config)


def _initialize_racers(config):
    racers_cfg = _racers_config(config)
    racers = []
    for racer_name in racers_cfg:
        racer = racers_cfg[racer_name]
        racer_type = racer[ANIMAL_TYPE]
        racer_speed = racer[ANIMAL_SPEED]
        racers.append(
            factory(racer_type,
                    racer_name,
                    racer_speed))
    return racers


def _racers_config(config):
    with open(config['racers_config'], READ) as cfg_file:
        return json.load(cfg_file)
