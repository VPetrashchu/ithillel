import pytest
import json
import unittest
from PetrashchukV.Lesson24_HT19.api.test_marvel_api.test_data import characters_data
from PetrashchukV.Lesson24_HT19.api.infrastrusture.characters_service import CharactersService


def test_get_200(character_service):
    characters_response = character_service.get_one_characters()
    assert characters_response.status_code == 200, f"Отримано код помилки: {characters_response.status_code}"

def test_get_one_character(character_service):
    character = character_service.get_one_character(1011334).json()
    character_id = character['data']['results'][0]['id']
    character_service.save_one_character(character_id)
    assert 'data' in character
    assert 'results' in character['data']
    results = character['data']['results']
    assert len(results) > 0
    first_character = results[0]
    assert 'id' in first_character
    assert first_character['id'] == 1011334



@pytest.mark.parametrize('id,name', [(char['id'], char['name']) for char in characters_data])
def test_get_characters_with_param2(character_service, id, name):
    characters = character_service.get_all_characters().json()["data"]["results"]
    character_found = False
    for character in characters:
        if character['id'] == id:
            character_found = True
            assert character['name'] == name
            break
    assert character_found, f"Character with id {id} was not found in the API response."

'''
def test_validate_data_consistency_one_character(character_service):
    character = character_service.get_one_character(1011334)
    assert character.status_code == 200
    with open('1011334_character.json', 'r') as data:
        data_converted = json.load(data)
        assert data_converted == character.json()
'''

@pytest.fixture
def character_service():
    return CharactersService()
def test_validate_data_consistency_one_character(character_service):
    character = character_service.get_one_character(1011334)
    assert character.status_code == 200
    with open('1011334_character.json', 'r') as data:
        data_converted = json.load(data)
        assert data_converted == character.json()
