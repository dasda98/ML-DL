import logging
import logging.config
import yaml

from pathlib import Path


CONFIG_FILE = Path(__file__).absolute().parent / 'config.yaml'


class RemoveLevelFilter(logging.Filter):
    def __init__(self, levels: list):
        self.levels = levels

    def filter(self, record):
        return self.getLogLevelName(record.levelno) \
               not in self.levels

    def getLogLevelName(self, levelno):
        switcher = {
            10: "DEBUG",
            20: "INFO",
            30: "WARNING",
            40: "ERROR",
            50: "CRITICAL"
        }
        return switcher.get(levelno, "INVALID")


class LOG:
    def __init__(self, config_file: Path):
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

        self.devLogger = logging.getLogger('devLogger')
        self.userLogger = logging.getLogger('userLogger')
        self.userLogger.addFilter(RemoveLevelFilter(["DEBUG", "WARNING", "ERROR", "CRITICAL"]))

    def check_working(self):
        self.devLogger.debug('message')
        self.devLogger.info('message')
        self.devLogger.warning('message')
        self.devLogger.error('message')
        self.devLogger.critical('message')

        self.userLogger.debug('message')
        self.userLogger.info('message')
        self.userLogger.warning('message')
        self.userLogger.error('message')
        self.userLogger.critical('message')


log = LOG(CONFIG_FILE)

if __name__ == '__main__':
    log.check_working()