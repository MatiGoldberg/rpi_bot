#!/bin/python3
import argparse
import logger

VERSION = '1.0'
LOG_FILENAME = 'bot_server.log'

# -- argument parser settings -- #
parser = argparse.ArgumentParser(description="arguments for bot server")
parser.add_argument('-v','--verbose',help='print log to screen', action='store_true')
parser.add_argument('-m','--mode',help='running mode', choices=['test', 'full'], default='test')

# -- main class for a telegram-based dispatch -- #
def main():    
    args = parser.parse_args()
    log = logger.set_logger(LOG_FILENAME,print_to_screen=True)
    log.info(f'booting bot v{VERSION}')
    log.info(f'verbose: {args.verbose}')
    log.info(f'mode: {args.mode}')
    log.info('shutting down.')

main() 
