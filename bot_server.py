#!/bin/python3
import json
import logger
from bot_config import bot_config

log = logger.get_logger()

class bot_server:
    
    base_uri = "api.telegram.org"
    
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
        config = bot_config(config_file)
        if not config.is_valid():
            log.error('failed to load configuration')
            return
        
        self.path = '/bot' + config.token + '/{0}'
        self.me = config.name
        self.polling_period = config.polling_period
        log.info('configuration loaded successfuly')            
        self._is_valid=True


