from config import SUPPORTED_ANIMALS


def factory(racer_type, racer_properties):
    options = _initialize_options()
    try:
        return options[racer_type](*racer_properties)
    except KeyError:
        raise KeyError("{} not in supported animals".format(racer_type))


def _initialize_options():
    return SUPPORTED_ANIMALS
