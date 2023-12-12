import json
import logging
from logging import config

with open('json_config.json') as fh:
    config.dictConfig(json.load(fh))



logging.debug('debug')
logging.critical('critical')