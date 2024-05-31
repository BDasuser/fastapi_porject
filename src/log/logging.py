import logging

def get_logger():

    logging.basicConfig(filename='app.log', filemode="a", format='%(asctime)s %(message)s')

    logger = logging.getLogger("App-log")

    logger.setLevel("INFO")

    return logger


applog = get_logger()