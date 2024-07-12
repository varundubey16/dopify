# secretreader to secrets_reader.py change name later

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRETS_FILE = os.path.join(BASE_DIR, 'secret.json')

def get_secret(setting_name):
    with open(SECRETS_FILE, 'r') as f:
        secrets = json.load(f)
    return secrets.get(setting_name, None)
