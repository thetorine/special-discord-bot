import json
import os

config_dict = None
with open('config.json') as f:
    config_dict = json.load(f)

if os.environ.get('PRODUCTION') is not None:
    config_dict = config_dict['production']
else:
    config_dict = config_dict['debug']

BOT_TOKEN = config_dict['token']
BANNED_WORDS = config_dict['words']
BANNED_MESSAGE = config_dict['message']
