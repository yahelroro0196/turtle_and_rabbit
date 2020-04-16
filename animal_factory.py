from config import supported_animals


def factory(racer_type, racer_properties):
    try:
        return supported_animals[racer_type](**racer_properties)
    except KeyError:
        raise KeyError("{} not in supported animals".format(racer_type))
