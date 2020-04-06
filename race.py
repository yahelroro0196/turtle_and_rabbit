import asyncio
import json
import time

from animal_factory import factory
from constants import *

RACER_RUNTIME = 0
RACER_NAME = 1


def race(config):
    race_settings = _load_race_config(config)
    rounds = _initialize_rounds(race_settings)

    loop = asyncio.get_event_loop()
    for curr_round in rounds:
        round_settings = rounds[curr_round]
        racers = round_settings[RACERS]
        track_length = round_settings[TRACK_LENGTH]
        track_runs = []
        for racer in racers:
            track_runs.append(track_run(racer, track_length))
        results = loop.run_until_complete(asyncio.gather(*track_runs))
        _display_round_results(results, curr_round)
    loop.close()


def _display_round_results(results, curr_round):
    results = sorted(results, key=lambda res: res[RACER_RUNTIME])
    print('round {} results:'.format(curr_round))
    for i, result in enumerate(results):
        print('{} place: {} with a time of {}'.format(i + ORIGIN0_OFFSET, result[RACER_NAME], result[RACER_RUNTIME]))


async def track_run(racer, track_length):
    progress = 0
    speed = racer.speed
    step_interval = racer.step_interval
    running = True
    while running:
        print(racer.name + ' progress: ' + str(progress))
        progress += speed
        await asyncio.sleep(step_interval)
        if progress >= track_length:
            running = False
    print(racer.name + ' finished!')
    finish_time = time.strftime(TIME_FORMAT)
    return finish_time, racer.name


def _initialize_rounds(race_settings) -> dict:
    rounds = {}
    for i, curr_round in enumerate(race_settings):
        racers_settings = race_settings[curr_round][RACERS]
        racers = []
        for racer_name in racers_settings:
            _build_racer(racer_name, racers, racers_settings)
        rounds[str(i + ORIGIN0_OFFSET)] = {
            TRACK_LENGTH: race_settings[curr_round][TRACK_LENGTH],
            RACERS: racers
        }
    return rounds


def _build_racer(racer_name, racers, racers_settings):
    racer = racers_settings[racer_name]
    racer_type = racer[ANIMAL_TYPE]
    racer_properties = [racer_name] + [value for key, value in racer.items() if key != ANIMAL_TYPE]
    racers.append(
        factory(racer_type,
                racer_properties))


def _load_race_config(config) -> dict:
    with open(config[RACERS_CONFIG], READ) as cfg_file:
        return json.load(cfg_file)[RACE_SETTINGS]
