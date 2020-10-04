#!/bin/python3
import json
import logger

log = logger.get_logger()

class bot_server:
    
    def __init__(self, config_file='bot.config.json'):
        self._is_valid = False
        self._load_configuration(config_file)
        
    # -- public mehtods --
    def is_valid(self):
        return self._is_valid
    
    def run(self, run_mode='full'):
        log.info(f'bot starting in {run_mode} mode')
        
    # -- private methods --
    def _load_configuration(self, config_file):
        log.debug(f'loading configuration from [{config_file}]')
        self._is_valid=True
