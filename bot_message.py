#!/bin/python3
import json
import logger

log = logger.get_logger()

class bot_message:
    
    def __init__(self, msg):
        self.is_valid = False
        try:
            self.update_id = msg['update_id']
            self.message_id = msg['message']['message_id']
            self.text = msg['message']['text']
            self.chat_id = msg['message']['chat']['id']
            self.from_user_name = msg['message']['from']['first_name']
            self.from_user_id = msg['message']['from']['id']
        except Exception as e:
            log.error(f'failed to parse message: {e.args}')
            return
            
        self.is_valid = True
