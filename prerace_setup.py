import json

from animal_factory import factory
from config import RACERS_CONFIG_PATH
from constants import *


def _initialize_rounds(race_settings) -> dict:
    rounds = {}
    for i, curr_round in enumerate(race_settings):
        racers = _build_round_racers(curr_round, race_settings)
        _build_round(curr_round, i, race_settings, racers, rounds)
    return rounds


def _build_round(curr_round, i, race_settings, racers, rounds):
    rounds[str(i + ORIGIN0_OFFSET)] = {
        TRACK_LENGTH: race_settings[curr_round][TRACK_LENGTH],
        RACERS: racers
    }


def _build_round_racers(curr_round, race_settings):
    racers_settings = race_settings[curr_round][RACERS]
    racers = []
    for racer_name in racers_settings:
        _build_racer(racer_name, racers, racers_settings)
    return racers


def _build_racer(racer_name, racers, racers_settings):
    racer = racers_settings[racer_name]
    racer_type = racer[ANIMAL_TYPE]
    racer_properties = [racer_name] + [value for key, value in racer.items() if key != ANIMAL_TYPE]
    racers.append(
        factory(racer_type,
                racer_properties))


def _load_race_settings() -> dict:
    with open(RACERS_CONFIG_PATH, READ) as cfg_file:
        return json.load(cfg_file)[RACE_SETTINGS]


def _pre_race_preparation(curr_round, rounds):
    return _unpack_round_settings(curr_round, rounds)


def _unpack_round_settings(curr_round, rounds):
    round_settings = rounds[curr_round]
    racers = round_settings[RACERS]
    track_length = round_settings[TRACK_LENGTH]
    return racers, track_length
