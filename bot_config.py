#!/bin/python3
import os.path
import json
import logger

log = logger.get_logger()

class bot_config:
    
    def __init__(self, filename):
        self.config_file = filename
        self._init_vars()
        
        if not os.path.exists(filename):
            log.error(f'could not find congif file: [{filename}]')
            return
        self.load_config()
        
    def _init_vars(self):
        self.token = None
        self.name = None
        self.polling_period = None
        
    def save_config(self, name='<Bot Name Here>', token ='<Bot Token Here>', polling_period = 0.5):
        config = {'name' : name, \
                  'token' : token, \
                  'polling_period_sec' : str(polling_period)}
            
        with open(self.config_file, 'w') as f:
            f.write(str(json.dumps(config, indent=4, separators=(',', ': '))))

    def load_config(self):
        content = open(self.config_file, 'r').read()
        try:
            self.config = json.loads(content)
        except:
            self.config = None
            log.error('failed to parse config file')
            return

        self.token = self.config['token']
        self.name = self.config['name']
        log.debug(f'found token for [{self.name}]: [{self.token[:5]}...]')
        if 'polling_period_sec' in self.config:
            self.polling_period = self.config['polling_period_sec']
        else:
            self.polling_period = 0.5

    def is_valid(self):
        return self.config is not None and \
               'name' in self.config and 'token' in self.config and \
               self.config['name'] is not None and self.config['token'] is not None

