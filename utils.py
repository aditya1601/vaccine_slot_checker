import logging
from logging.handlers import RotatingFileHandler
import config
from playsound import playsound


global logger
logger = logging.getLogger()
logger.handlers.clear()
consoleHandler = logging.StreamHandler()
logFileHandler = RotatingFileHandler("logs/logs.txt", maxBytes=1024)
formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] %(message)s")
consoleHandler.setFormatter(formatter)
logFileHandler.setFormatter(formatter)
logger.setLevel(config.LOGGING_LEVEL)
logger.addHandler(consoleHandler)
logger.addHandler(logFileHandler)


def play_sound():
    for i in range(3):
        playsound("notify.mp3")