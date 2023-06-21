import logging
import logging.config
import yaml

class LOG:
    def __init__(self, config_file: str):
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f.read())
            logging
