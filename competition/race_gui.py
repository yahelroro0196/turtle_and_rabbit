import operator

from constants import ORIGIN0_OFFSET

RACER_RUNTIME = 0


def _display_round_results(results, curr_round):
    results = sorted(results, key=operator.itemgetter(RACER_RUNTIME))
    print(f'round {curr_round.number} results:')
    for racer_placement, result in enumerate(results):
        racer_runtime, racer_name = result
        print(f'{racer_placement + ORIGIN0_OFFSET} place: {racer_name} with a time of {racer_runtime}')


async def _run_end_print(racer):
    print(f'{racer.name} finished!')
