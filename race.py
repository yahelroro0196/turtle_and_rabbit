from animal_factory import factory
from constants import *
import json
import time
import asyncio

RACER_RUNTIME = 0
RACER_NAME = 1


def race(config):
    race_cfg = _load_race_config(config)
    racers_cfg = race_cfg[RACERS]
    race_cfg = race_cfg[RACE_SETTINGS]
    racers = _initialize_racers(racers_cfg)

    loop = asyncio.get_event_loop()
    total_rounds = race_cfg[ROUNDS]
    for curr_round in range(total_rounds):
        track_runs = []
        for racer in racers:
            track_runs.append(track_run(racer, race_cfg))
        results = loop.run_until_complete(asyncio.gather(*track_runs))
        _display_round_results(results, curr_round)
    loop.close()


def _display_round_results(results, curr_round):
    results = sorted(results, key=lambda res: res[RACER_RUNTIME])
    print('round {} results:'.format(curr_round + 1))
    for i, result in enumerate(results):
        print('{} place: {} with a time of {}'.format(i + 1, result[RACER_NAME], result[RACER_RUNTIME]))


async def track_run(racer, race_cfg: dict):
    progress = 0
    track_length = race_cfg[TRACK_LENGTH]
    speed = racer.speed
    running = True
    while running:
        print(racer.name + ' progress: ' + str(progress))
        progress += speed
        await asyncio.sleep(1)
        if progress >= track_length:
            running = False
    print(racer.name + ' finished!')
    finish_time = time.strftime(TIME_FORMAT)
    return finish_time, racer.name


def _initialize_racers(racers_cfg) -> list:
    racers = []
    for racer_name in racers_cfg:
        racer = racers_cfg[racer_name]
        racer_type = racer[ANIMAL_TYPE]
        racer_properties = [racer_name] + [value for key, value in racer.items() if key != ANIMAL_TYPE]
        racers.append(
            factory(racer_type,
                    racer_properties))
    return racers


def _load_race_config(config) -> dict:
    with open(config[RACERS_CONFIG], READ) as cfg_file:
        return json.load(cfg_file)
