import requests
import hashlib
from Lesson24.api import config
from requests import get
import json

class CharactersService:
    def __init__(self):
        pass

    def authenticate(self):
        public_key = 'b6ea02eb93ee348631f2e9eedc702a62'
        private_key = '8574a0b853f03948529f3d7ac8a931f448cd95d5'
        ts = '1'
        hash_value = hashlib.md5(f'{ts}{private_key}{public_key}'.encode()).hexdigest()
        return {
            'apikey': public_key,
            'ts': ts,
            'hash': hash_value
        }

    def get_one_character(self, id=1011334):
        url = config['host1'] + f"characters/{id}"
        params = self.authenticate()
        response = requests.get(url, params=params)
        return response

    def get_all_characters(self):
        url = config['host1'] + f"characters"
        params = self.authenticate()
        response = requests.get(url, params=params)
        return response

    def save_one_character(self, character_id):
        response = self.get_one_character(character_id)
        character_data = response.json()['data']['results'][0]
        with open(f'{character_data["id"]}_character.json', 'w') as character_file:
            json.dump(character_data, character_file, indent=4)
