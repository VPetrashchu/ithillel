#task_1
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.species}"

    @staticmethod
    def make_sound(sound):
        return f"The animal makes the sound: {sound}"


animal1 = Animal("Leo", "Lion")
print(animal1)
print(Animal.make_sound("Roar"))

#task_2
class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry

    def __str__(self):
        return f"{self.name} operates in the {self.industry} industry"

    @classmethod
    def change_industry(cls, new_industry):
        return f"The industry has changed to {new_industry}"


company1 = Company("ABC Inc.", "Technology")
print(company1)
print(Company.change_industry("Healthcare"))