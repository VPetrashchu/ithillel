from abc import ABC, abstractmethod
from datetime import datetime


class Item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_name(self):
        pass


class Dish(Item):
    def get_name(self):
        return self.name


class Drink(Item):
    def get_name(self):
        return self.name


class ColdDish(Dish):
    pass


class HotDish(Dish):
    pass


class Section(ABC):
    @abstractmethod
    def get_name(self):
        pass


class FoodSection(Section):
    def get_name(self):
        return 'Food'


class DrinkSection(Section):
    def get_name(self):
        return 'Drink'


class Order:
    def __init__(self):
        self.timestamp = datetime.now()
        self.items = []

    def add_item(self, item, quantity=1):
        for _ in range(quantity):
            self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print('Item not found in order.')

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def display_details(self):
        print('Order details:')
        for item in self.items:
            print(f'{item.get_name()}: ${item.price}')
        print(f'Total: ${self.calculate_total()}')
        print('Order placed at:', self.timestamp)


order = Order()
order.add_item(Dish('Risotto', 15), 2)
order.add_item(Dish('Pizza', 20))
order.add_item(Drink('Cola', 3))
order.display_details()
order.remove_item(Dish('Risotto', 15))
order.display_details()
