from datetime import datetime, timedelta

#Task_1
print('Task_1')
def add_or_subtract_days(date_time, days, sign):
    if sign:
        return date_time + timedelta(days=days)
    else:
        return date_time - timedelta(days=days)

input_date = datetime(2024, 2, 10, 12, 0, 0)
new_date = add_or_subtract_days(input_date, 5, True)
print("Нова дата після додавання 5 днів:", new_date)

new_date_sub = add_or_subtract_days(input_date, 3, False)
print("Нова дата після віднімання 3 днів:", new_date_sub)

#Task_2
print('Task_2')
def calculate_age(birth_date):
    current_date = datetime.now()
    age_delta = current_date - birth_date
    age_timestamp = age_delta.total_seconds()

    birth_date_formatted = birth_date.strftime("%y-%d-%m %I:%M:%S %p")

    return age_delta, age_timestamp, birth_date_formatted


birth_date = datetime(1990, 5, 15, 8, 30, 0)
age_delta, age_timestamp, birth_date_formatted = calculate_age(birth_date)

print("Ваш вік:", age_delta)
print("Прожите життя в секундах:", age_timestamp)
print("Дата народження:", birth_date_formatted)

#Task_3
print('Task_3')
def divide(x, y):
    try:
        result = x / y
        print("Результат ділення:", result)
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль!")
    except TypeError:
        print("Помилка: Недопустимий тип даних для операції ділення!")
    except Exception as e:
        print("Отримано інший виняток:", e)

divide(10, 2)
divide(10, 0)
divide("10", 2)