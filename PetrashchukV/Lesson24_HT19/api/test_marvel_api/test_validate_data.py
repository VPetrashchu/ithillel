import unittest
import json
from PetrashchukV.Lesson24_HT19.api.infrastrusture.characters_service import CharactersService

#trying to resolving test validation via class
class TestValidateDataConsistencyOneCharacter(unittest.TestCase):
    def test_validate_data_consistency_one_character(self):
        character_service = CharactersService()
        character = character_service.get_one_character(1011334)
        self.assertEquals(character.status_code, 200)

        with open('1011334_character.json') as data:
            data_converted = json.load(data)
            self.assertEquals(data_converted, character.json())


if __name__ == '__main__':
    unittest.main()
