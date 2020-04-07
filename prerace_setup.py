import json

from Round import Round
from animal_factory import factory
from config import RACERS_CONFIG_PATH
from constants import ORIGIN0_OFFSET

TRACK_LENGTH = 'track_length'
RACERS = 'racers'
ANIMAL_TYPE = 'type'
RACERS_CONFIG = 'racers_config'
RACE_SETTINGS = 'race_settings'
ROUNDS = 'rounds'


def initialize_rounds(race_settings: dict) -> dict:
    rounds = {}
    for round_num, curr_round in enumerate(race_settings):
        round_settings = race_settings[curr_round]
        racers = _build_round_racers(round_settings)
        rounds[round_num] = _build_round(round_num, round_settings, racers)
    return rounds


def load_race_settings() -> dict:
    with open(RACERS_CONFIG_PATH) as cfg_file:
        return json.load(cfg_file)[RACE_SETTINGS]


def unpack_round_settings(curr_round):
    return curr_round.racers, curr_round.track_length


def _build_round(round_num, round_settings: dict, racers):
    return Round(round_num + ORIGIN0_OFFSET, round_settings[TRACK_LENGTH], racers)


def _build_round_racers(round_settings: dict):
    racers_settings = round_settings[RACERS]
    racers = [_build_racer(racer_name, racers_settings) for racer_name in racers_settings]
    return racers


def _build_racer(racer_name: str, racers_settings: dict):
    racer = racers_settings[racer_name]
    racer_type = racer[ANIMAL_TYPE]
    del racer[ANIMAL_TYPE]
    racer_properties = [racer_name] + [*racer.values()]
    return factory(racer_type, racer_properties)
