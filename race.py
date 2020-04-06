import asyncio
import time
import operator

from constants import TIME_FORMAT, ORIGIN0_OFFSET
from prerace_setup import initialize_rounds, load_race_settings, unpack_round_settings

RACER_RUNTIME = 0
RACER_NAME = 1


def race():
    race_settings = load_race_settings()
    rounds = initialize_rounds(race_settings)

    loop = asyncio.get_event_loop()
    for curr_round in rounds:
        _run_round(curr_round, loop, rounds)
    loop.close()


def _run_round(curr_round, loop, rounds):
    racers, track_length = unpack_round_settings(curr_round, rounds)
    track_runs = [track_run(racer, track_length) for racer in racers]
    results = loop.run_until_complete(asyncio.gather(*track_runs))
    _display_round_results(results, curr_round)


def _display_round_results(results, curr_round):
    results = sorted(results, key=operator.itemgetter(RACER_RUNTIME))
    print(f'round {curr_round} results:')
    for i, result in enumerate(results):
        racer_runtime, racer_name = result
        print(f'{i + ORIGIN0_OFFSET} place: {racer_name} with a time of {racer_runtime}')


async def track_run(racer, track_length):
    interval_spacing, progress, running, steps_per_interval = await _per_run_unpacking(racer)
    while running:
        print(f'{racer.name} progress: {str(progress)}')
        progress += steps_per_interval
        running = await _check_if_finished_run(progress, track_length)
        await asyncio.sleep(interval_spacing)
    finish_time = await _end_of_run_print(racer)
    return finish_time, racer.name


async def _end_of_run_print(racer):
    print(f'{racer.name} finished!')
    finish_time = time.strftime(TIME_FORMAT)
    return finish_time


async def _check_if_finished_run(progress, track_length):
    return progress < track_length


async def _per_run_unpacking(racer):
    return racer.interval_spacing, 0, True, racer.steps_per_interval
