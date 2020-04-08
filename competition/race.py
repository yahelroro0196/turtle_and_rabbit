import asyncio
import time

from competition.prerace_setup import unpack_round_settings, load_race_settings, initialize_rounds
from competition.race_gui import *
from constants import TIME_FORMAT


def start_competition():
    race_settings = load_race_settings()
    rounds = initialize_rounds(race_settings)

    loop = asyncio.get_event_loop()
    for curr_round in rounds:
        _run_round(curr_round, loop)
    loop.close()


async def _track_run(racer, track_length):
    interval_spacing, progress, running, steps_per_interval = await _per_run_unpacking(racer)
    while running:
        await print_progress(racer, progress)
        progress += steps_per_interval
        running = await _check_if_finished_run(progress, track_length)
        await asyncio.sleep(interval_spacing)
    finish_time = await _end_of_run_time()
    await run_end_print(racer)
    return finish_time, racer.name


def _run_round(curr_round, loop):
    racers, track_length = unpack_round_settings(curr_round)
    track_runs = [_track_run(racer, track_length) for racer in racers]
    results = loop.run_until_complete(asyncio.gather(*track_runs))
    display_round_results(results, curr_round)


async def _end_of_run_time():
    finish_time = time.strftime(TIME_FORMAT)
    return finish_time


async def _check_if_finished_run(progress, track_length):
    return progress < track_length


async def _per_run_unpacking(racer):
    return racer.interval_spacing, 0, True, racer.steps_per_interval
