import pytest
from PetrashchukV.Lesson25_HT20.infrastructure import Phone

@pytest.fixture
def phone():
    yield Phone()