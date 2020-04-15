import asyncio
import time

from competition import race_gui
from competition.prerace_setup import unpack_round_settings
from constants import TIME_FORMAT

NO_PASS_OUT = 0


def run(curr_round, loop):
    racers, track_length = unpack_round_settings(curr_round)
    track_runs = [_track_run(racer, track_length) for racer in racers]
    results = loop.run_until_complete(asyncio.gather(*track_runs))
    return results


async def _track_run(racer, track_length):
    interval_spacing, progress, running, steps_per_interval = await _per_run_unpacking(racer)
    while running:
        await race_gui.racer_progress_print(racer, progress)
        progress = await _update_progress(racer, progress,
                                          steps_per_interval)
        running = await _check_if_finished_run(progress, track_length)
        await asyncio.sleep(interval_spacing)
    finish_time = await _end_of_run_time()
    await race_gui.end_of_run_print(racer)
    return finish_time, racer.name


async def _update_progress(racer, progress, steps_per_interval):
    if racer.passed_out_time != NO_PASS_OUT:
        progress += racer.steps_before_pass_out
        await race_gui.passed_out_print(racer)
        await asyncio.sleep(racer.passed_out_time)
        step_difference = steps_per_interval - racer.steps_before_pass_out
        progress += step_difference
    else:
        progress += steps_per_interval
    return progress


async def _end_of_run_time():
    return time.strftime(TIME_FORMAT)


async def _check_if_finished_run(progress, track_length):
    return progress < track_length


async def _per_run_unpacking(racer):
    return racer.interval_spacing, racer.starting_position, True, racer.steps_per_interval
