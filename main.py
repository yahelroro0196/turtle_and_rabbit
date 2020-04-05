import json

from config import config_path
from constants import READ
from race import race


def main():
    config = _load_config()
    race(config)


def _load_config():
    with open(config_path, READ) as cfg_file:
        return json.load(cfg_file)


if __name__ == '__main__':
    main()
