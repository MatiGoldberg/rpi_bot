#!/bin/python3
import json
import logger
from bot_config import bot_config
from bot_message import bot_message
import http.client, urllib
import time

log = logger.get_logger()

class bot_server:
    
    base_uri = "api.telegram.org"
    
    def __init__(self, config_file='bot.config.json'):
        self._is_valid = False
        self._load_configuration(config_file)
        if not self._is_valid:
            return
        self.connection = http.client.HTTPSConnection(self.base_uri)
        self._build_in_test()
                
    # -- public mehtods --
    def is_valid(self):
        return self._is_valid
    
    def run(self, run_mode='full'):
        log.info(f'bot starting in {run_mode} mode')
        run_once = run_mode=='test'
        
        last_update = 0
        while True:
            messages = self._get_messages(last_update + 1)
            for msg in messages:
                self._handle_message(msg)
            
            if run_once:
                break
            time.sleep(self.polling_period)
        log.info('bot stopping.')
       
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
        
    def _build_in_test(self):
        log.debug('starting build in test')
        response = self._send_request('getMe')
        if not self._response_is_valid(response):
            log.error('invalid response, BIT failed.')
            self._is_valid = False
            return

        bot_username = response['result']['username']
        log.info(f'connection is valid to bot @{bot_username}')
        
    # -- communication logic --
    def _get_messages(self, offset=None):
        params = None
        if offset is not None:
            params = {'offset' : offset, 'limit' : 10}
        response = self._send_request('getUpdates',params)
        if not self._response_is_valid(response):
            log.error(f"invalid response:\n{bot_server._print_response(response)}")
            return
        
        if len(response['result']) > 0:
            log.debug(f'got [{len(response["result"])}] updates')
        return [bot_message(msg) for msg in response['result']]
    
    def _handle_message(self, msg):
        if not msg.is_valid:
            log.warning('invalid message, skipping')
            return
        log.debug(f'handling message: {msg.update_id}')
        self._send_message(msg.chat_id, f'Hi {msg.from_user_name}, got your message: {msg.text}')
        
    def _send_message(self, chat_id, text):
        if chat_id is None:
            return None
        params = {'chat_id' : chat_id, 'text' : text}
        response = self._send_request('sendMessage', params)
        if not self._response_is_valid(response):
            log.error(f"invalid response:\n{bot_server._print_response(response)}")
    
    # -- communication methods -- 
    def _send_request(self, method, params=None):
        query = ''
        if params is not None:
            query = '?' + urllib.parse.urlencode(params)
        
        self.connection.request('GET',self.path.format(method) + query)
        res = self.connection.getresponse()
        
        data = res.read()
        if res.status is not 200:
            log.error(f'http error ({res.status})')
            return None
        try:
            return json.loads(data)
        except:
            log.error('failed to parse response')
            return None

    def _response_is_valid(self, res):
        return res is not None and 'ok' in res and res['ok'] is True and 'result' in res
    
    # -- static methods --
    @staticmethod
    def _print_response(response_object):
        return json.dumps(response_object, indent=4, sort_keys=True)

