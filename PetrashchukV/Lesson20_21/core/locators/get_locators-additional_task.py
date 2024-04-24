from .base_locators import BaseLocators

class Locators:
    @classmethod
    def get_locators(cls):
        locators = {}
        for name, value in BaseLocators.__dict__.items():
            if not name.startswith('__'):
                locators[name] = ('xpath', value)
        return locators