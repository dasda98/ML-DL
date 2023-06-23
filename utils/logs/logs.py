import logging
import logging.config
import yaml

from pathlib import Path


CONFIG_FILE = Path(__file__).absolute().parent / 'config.yaml'


class LOG:
    def __init__(self, config_file: str):
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

        self.devLogger = logging.getLogger('devLogger')
        self.userLogger = logging.getLogger('userLogger')


log = LOG(CONFIG_FILE)
