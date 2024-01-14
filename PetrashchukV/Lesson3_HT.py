import random

#Hometask_1
print('Hometask_1')
random_number = random.randint(0, 59)
if 0 <= random_number < 15:
    quarter = 1
elif 15 <= random_number < 30:
    quarter = 2
elif 30 <= random_number < 45:
    quarter = 3
else:
    quarter = 4

print(f'Number {random_number} is in {quarter} quarter hour.')

#Hometask_2
print('Hometask_2')
birth_month = int(input("Введіть номер місяця вашого народження (1-12): "))

if 1 <= birth_month <= 12:
    if 3 <= birth_month <= 5:
        season = 'весна'
        characteristic = 'все довкола розцвітало.'
    elif 6 <= birth_month <= 8:
        season = 'літо'
        characteristic = 'діти насолоджувались літніми канікулами.'
    elif 9 <= birth_month <= 11:
        season = 'осінь'
        characteristic = 'все довкола загоралось яскравими фарбами.'
    else:
        season = 'зима'
        characteristic = 'за вікном падав сніг.'

    print(f'Ваш місяць народження {birth_month} це {season}, - {characteristic}')
else:
    print('Введено некоректний номер місяця.')

#Hometask_3
print('Hometask_3')
def is_divisible_by_6(number):
    last_digit = number % 10
    digit_sum = sum(int(digit) for digit in str(number))

    if last_digit % 2 == 0 and digit_sum % 3 == 0:
        return True
    else:
        return False

random_number = random.randint(1, 100)

if is_divisible_by_6(random_number):
    print(f'Число {random_number} ділиться на 6.')
else:
    print(f'Число {random_number} не ділиться на 6.')


#Hometask_4
print('Hometask_4')

x = float(input('Введіть координату x: '))
y = float(input('Введіть координату y: '))


if x == 0 and y == 0:
    quadrant = 'початок координат'
elif x == 0:
    quadrant = 'лежить на осі Y'
elif y == 0:
    quadrant = 'лежить на осі X'
elif x > 0 and y > 0:
    quadrant = 'перша'
elif x < 0 and y > 0:
    quadrant = 'друга'
elif x < 0 and y < 0:
    quadrant = 'третя'
elif x > 0 and y < 0:
    quadrant = 'четверта'
else:
    quadrant = 'невизначена'

print(f'Точка з координатами ({x}, {y}) належить до {quadrant} чверті координат.')