#Hometask#1
print('Hometask#1')

def common_elements(list1, list2):
    common = sorted(set(list1) & set(list2))
    return common

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = common_elements(list1, list2)
print('Common elements:', result)


#Hometask#2
print('Hometask#2')
students = {
    'Alex': 85,
    'John': 90,
    'Simba': 78,
    'Emily': 95
}

average_score = sum(students.values()) / len(students)


above_average = [name for name, score in students.items() if score > average_score]
print('Names of students with above average scores:', above_average)

#Hometask#3
print('Hometask#3')
import random

name = ['Alex', 'John', 'Simba']
surname = ['Smith', 'Doe', 'Johnson']
location = ['New York', 'London', 'Paris']

random_people = []
for _ in range(5):
    person = {
        'name': random.choice(name),
        'surname': random.choice(surname),
        'location': random.choice(location)
    }
    random_people.append(person)

for person in random_people:
    print(person)