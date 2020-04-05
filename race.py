from animal_factory import factory
from constants import ANIMAL_TYPE, READ, RACERS_CONFIG
import json
import asyncio

TRACK_LENGTH = 20


def race(config):
    racers = _initialize_racers(config)

    loop = asyncio.get_event_loop()
    for racer in racers:
        loop.create_task(track_run(racer))
    loop.run_forever()
    loop.close()


async def track_run(racer):
    progress = 0
    speed = racer.speed
    running = True

    while running:
        print(racer.name + ' progress: ' + str(progress))
        progress += speed
        await asyncio.sleep(1)
        if progress >= TRACK_LENGTH:
            running = False

    print(racer.name + ' finished!')


def _initialize_racers(config) -> list:
    racers_cfg = _racers_config(config)
    racers = []
    for racer_name in racers_cfg:
        racer = racers_cfg[racer_name]
        racer_type = racer[ANIMAL_TYPE]
        racer_properties = [racer_name] + [value for key, value in racer.items() if key != ANIMAL_TYPE]
        racers.append(
            factory(racer_type,
                    racer_properties))
    return racers


def _racers_config(config) -> dict:
    with open(config[RACERS_CONFIG], READ) as cfg_file:
        return json.load(cfg_file)
