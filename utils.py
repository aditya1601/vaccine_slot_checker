import logging
import config
from playsound import playsound

global logger
logger = logging.getLogger()
logger.handlers.clear()
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] [%(filename)s] %(message)s")
consoleHandler.setFormatter(formatter)
logger.setLevel(config.LOGGING_LEVEL)
if not logger.handlers:
    logger.addHandler(consoleHandler)


def play_sound():
    for i in range(config.NUM_TIMES_NOTIFY):
        playsound("notify.mp3")