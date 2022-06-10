import logging
from datetime import datetime
import os


# CREATE LOGGER
logger = logging.getLogger('TD5G Diagnostic')
logger.setLevel(logging.DEBUG)

# *******END LOGGER*******
def init_logger():
    try:
        # CREATE FILE HANDLE
        fh = logging.FileHandler(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics',
                                              'TD5G_diag.log'))
        fh.setLevel(logging.DEBUG)
        # CREATE CONSOLE OUTPUT HANDLER
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # CREATE FORMAT
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # ADD HANDLER
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.debug("DIAGNOSTIC LOG INITIALIZED")
    except NameError as e:
        logger.error(f"NameError: {e}")
        os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics'))
        init_logger()
    except FileNotFoundError as e:
        logger.error(f"FileNotFoundError: {e}")
        os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics'))
        init_logger()


# *******END LOGGER*******


# START LOG
def start_log():
    now = datetime.now()
    formatted_string = now.strftime("%d/%m/%Y %H:%M:%S")
    logger.info(f"---STARTING TD5G DIAGNOSTIC--- {formatted_string}")
    logger.info("                            ")


# END LOG
def end_log():
    now = datetime.now()
    formatted_string = now.strftime("%d/%m/%Y %H:%M:%S")
    logger.info(f"---ENDING TD5G DIAGNOSTIC--- {formatted_string}")
    logger.info("                            ")
