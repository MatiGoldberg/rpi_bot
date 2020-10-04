#!/bin/python3
import argparse
import logger
from bot_server import bot_server
from sys import platform

VERSION = '1.0'
LOG_FILENAME = 'bot_server.log'

# -- argument parser settings -- #
parser = argparse.ArgumentParser(description="arguments for bot server")
parser.add_argument('-v','--verbose',help='print log to screen', action='store_true')
parser.add_argument('-m','--mode',help='running mode', choices=['test', 'full'], default='test')
parser.add_argument('-c','--config-file',help='configuration filename', default='bot.config.json')
parser.add_argument('-l','--log-level',help='log level', choices=['info', 'debug'], default='info')

# -- main class for a telegram-based dispatch -- #
def main():    
    args = parser.parse_args()
    log = logger.set_logger(LOG_FILENAME, debug_mode=args.log_level, print_to_screen=args.verbose)
    log.info(f'booting bot v{VERSION} on {platform}')
    log.info('\n\t'.join(['arguments:', f'log-level: {args.log_level}', f'verbose: {args.verbose}', f'mode: {args.mode}',f'configuration filename: {args.config_file}']))
    bot = bot_server(config_file=args.config_file)
    if not bot.is_valid():
        log.error('could not create bot server, aborting')
    else:
        log.info('server created successfuly')
        bot.run(args.mode)
    log.info('shutting down.')

main() 
