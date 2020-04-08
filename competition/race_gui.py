import asyncio
import operator

from competition.prerace_setup import load_race_settings, initialize_rounds
from competition.race import run
from constants import ORIGIN0_OFFSET

RACER_RUNTIME = 0


def start_competition():
    race_settings = load_race_settings()
    rounds = initialize_rounds(race_settings)

    loop = asyncio.get_event_loop()
    for curr_round in rounds:
        results = run(curr_round, loop)
        _display_round_results(results, curr_round)
    loop.close()


def _display_round_results(results, curr_round):
    results = sorted(results, key=operator.itemgetter(RACER_RUNTIME))
    print(f'round {curr_round.number} results:')
    for racer_placement, result in enumerate(results):
        racer_runtime, racer_name = result
        print(f'{racer_placement + ORIGIN0_OFFSET} place: {racer_name} with a time of {racer_runtime}')


async def print_progress(racer, progress):
    print(f'{racer.name} progress: {progress}')


async def run_end_print(racer):
    print(f'{racer.name} finished!')
