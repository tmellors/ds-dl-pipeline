# app_logger.py
import logging
import sys, os

logs_path = os.path.join(os.getcwd(), "logs")
if not os.path.exists(logs_path):
    os.makedirs(logs_path)

log_format = "%(asctime)s — %(name)s — %(levelname)s - %(funcName)s:line:%(lineno)d — %(message)s"


def get_file_handler(name):
    file_handler = logging.FileHandler(
        os.path.join(os.getcwd() + "/logs/" + name + ".log")
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(log_format))
    return file_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler(name))
    return logger
