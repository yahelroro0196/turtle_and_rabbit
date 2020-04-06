import json

from animal_factory import factory
from config import RACERS_CONFIG_PATH
from constants import READ, ORIGIN0_OFFSET

TRACK_LENGTH = 'track_length'
RACERS = 'racers'
ANIMAL_TYPE = 'type'
RACERS_CONFIG = 'racers_config'
RACE_SETTINGS = 'race_settings'
ROUNDS = 'rounds'


def initialize_rounds(race_settings) -> dict:
    rounds = {}
    for i, curr_round in enumerate(race_settings):
        racers = _build_round_racers(curr_round, race_settings)
        rounds = _build_round(curr_round, i, race_settings, racers, rounds)
    return rounds


def load_race_settings() -> dict:
    with open(RACERS_CONFIG_PATH, READ) as cfg_file:
        return json.load(cfg_file)[RACE_SETTINGS]


def unpack_round_settings(curr_round, rounds):
    round_settings = rounds[curr_round]
    return round_settings[RACERS], round_settings[TRACK_LENGTH]


def _build_round(curr_round, i, race_settings, racers, rounds):
    rounds[str(i + ORIGIN0_OFFSET)] = {
        TRACK_LENGTH: race_settings[curr_round][TRACK_LENGTH],
        RACERS: racers
    }
    return rounds


def _build_round_racers(curr_round, race_settings):
    racers_settings = race_settings[curr_round][RACERS]
    racers = [_build_racer(racer_name, racers_settings) for racer_name in racers_settings]
    return racers


def _build_racer(racer_name, racers_settings):
    racer = racers_settings[racer_name]
    racer_type = racer[ANIMAL_TYPE]
    del racer[ANIMAL_TYPE]
    racer_properties = [racer_name] + [*racer.values()]
    return factory(racer_type, racer_properties)
