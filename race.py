import asyncio
import time

from constants import *
from prerace_setup import _initialize_rounds, _load_race_settings, _pre_round_preparation

RACER_RUNTIME = 0
RACER_NAME = 1


def race():
    race_settings = _load_race_settings()
    rounds = _initialize_rounds(race_settings)

    loop = asyncio.get_event_loop()
    for curr_round in rounds:
        track_runs = []
        racers, track_length = _pre_round_preparation(curr_round, rounds)
        _list_track_run_tasks(racers, track_length, track_runs)
        results = loop.run_until_complete(asyncio.gather(*track_runs))
        _display_round_results(results, curr_round)
    loop.close()


async def track_run(racer, track_length):
    interval_spacing, progress, running, steps_per_interval = await _per_run_unpacking(racer)
    while running:
        print(racer.name + ' progress: ' + str(progress))
        progress += steps_per_interval
        running = await _check_if_finished_run(progress, track_length)
        await asyncio.sleep(interval_spacing)
    finish_time = await _end_of_run_print(racer)
    return finish_time, racer.name


async def _end_of_run_print(racer):
    print(racer.name + ' finished!')
    finish_time = time.strftime(TIME_FORMAT)
    return finish_time


async def _check_if_finished_run(progress, track_length):
    if progress >= track_length:
        return False
    return True


async def _per_run_unpacking(racer):
    progress = 0
    steps_per_interval = racer.steps_per_interval
    interval_spacing = racer.interval_spacing
    running = True
    return interval_spacing, progress, running, steps_per_interval


def _list_track_run_tasks(racers, track_length, track_runs):
    for racer in racers:
        track_runs.append(track_run(racer, track_length))


def _display_round_results(results, curr_round):
    results = sorted(results, key=lambda res: res[RACER_RUNTIME])
    print('round {} results:'.format(curr_round))
    for i, result in enumerate(results):
        racer_name, racer_runtime = result[RACER_NAME], result[RACER_RUNTIME]
        print('{} place: {} with a time of {}'.format(i + ORIGIN0_OFFSET, racer_name, racer_runtime))
