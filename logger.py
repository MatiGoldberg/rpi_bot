#!/bin/python3
import logging
logger_set = False

def set_logger(log_filename, debug_mode=False, print_to_screen=False):
    log_formatter = logging.Formatter('[%(asctime)s][%(threadName)s][%(filename)s/%(funcName)s][%(levelname)s] %(message)s')
    log_formatter.default_msec_format = '%s.%03d'
    log = logging.getLogger()
    if debug_mode:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
    
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(log_formatter)
    log.addHandler(file_handler)
    
    if not print_to_screen:
        return log
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    log.addHandler(console_handler)
    return log

def get_logger():
    return logging.getLogger()