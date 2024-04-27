import pytest

from PetrashchukV.Lesson24_HT19.api import CharactersService


@pytest.fixture
def character_service():
    yield CharactersService()