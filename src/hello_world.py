import logging

logger = logging.getLogger(__name__)


def hello():
    print("hello")
    logger.info("hello in logger")
    return "hello"


def world():
    print("world")
    logger.info("world in logger")


def abc():
    return "abc"
