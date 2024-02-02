#HomeTask1
print('Hometask#1')

def check_string(s):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
    return all(char in allowed_chars for char in s)

string = input("Введіть стрічку: ")
if check_string(string):
    print("Стрічка містить лише великі і малі літери, числа та нижнє підкреслення.")
else:
    print("Стрічка містить інші символи, крім великих і малих літер, чисел та нижнього підкреслення.")

'''
#2nd case of hometask1
def check_string(s):
    for char in s:
        if not (char.isalpha() or char.isdigit() or char == '_'):
            return False
    return True

string = input("Введіть стрічку: ")
if check_string(string):
    print("Стрічка містить лише великі і малі літери, числа та нижнє підкреслення.")
else:
    print("Стрічка містить інші символи, крім великих і малих літер, чисел та нижнього підкреслення.")
'''

#HomeTask2
print('Hometask#2')
strings = ["example (.com)", "github (.com)", "stackoverflow (.com)"]
for s in strings:
    start_index = s.find("(")
    end_index = s.find(")")
    if start_index != -1 and end_index != -1:
        print(s[:start_index].strip())
    else:
        print(s.strip())



#HomeTask3
print('Hometask#3')
import re

def insert_space_before_uppercase(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

string = input("Введіть стрічку: ")
print("Результат:", insert_space_before_uppercase(string))
