import logging, sys
import time

LOG_PATH = "log.txt"
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"


def setup_logging():

    """
    Configure logging so that messages are printed
    both to the console and to a log file.
    """

    logger = logging.getLogger()
    formatter = logging.Formatter(LOG_FORMAT)

    # Print to console
    printHandler = logging.StreamHandler(sys.stdout)
    printHandler.setFormatter(formatter)
    logger.addHandler(printHandler)

    # Write to log file
    fileHandler = logging.FileHandler(LOG_PATH)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)


def schedule(action, wait_time):

    """
    Update the bike info table at regular
    intervals.

    If an Exception occurs during the
    update, log it and move on.
    """

    setup_logging()

    while True:
        try:
            action()
        except Exception as e:
            logging.error("Failed to update bike data")
            logging.exception(e)

        time.sleep(wait_time)