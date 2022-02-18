import logging
import os
import utils
import datetime


class Logger:
    """Class to create logger object"""
    def __init__(self):
        pass

    @staticmethod
    def create_logger():
        """Create logger object for the test to use."""
        log_dir_name = utils.DEFAULT_LOG_DIR
        log_file_name = os.path.join(log_dir_name, f"bmi_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}.log")

        if not os.path.exists(log_dir_name):
            os.makedirs(log_dir_name)

        logger = logging.getLogger(log_file_name)
        logger.setLevel(logging.INFO)

        # Define message format
        bmi_log_fmt = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s")

        # define file handler and set formatter
        file_handler = logging.FileHandler(log_file_name)
        file_handler.setFormatter(bmi_log_fmt)
        file_handler.setLevel(logging.DEBUG)

        # define console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(bmi_log_fmt)
        console_handler.setLevel(logging.INFO)

        # add file and console handler to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.info("Results are saved in %s", log_dir_name)
        # Return log object
        return logger
