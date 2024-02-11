import random

#Task_1
def log_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Викликано функцію: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function_name
def add(x, y):
    return x + y

@log_function_name
def multiply(x, y):
    return x * y

result_add = add(3, 5)
print("Результат додавання:", result_add)

result_multiply = multiply(4, 6)
print("Результат множення:", result_multiply)

#Task_2
numbers = [random.randint(1, 10) for _ in range(100)]

counts = {num: numbers.count(num) for num in set(numbers)}

for num, count in counts.items():
    print(f"Елемент {num}: {count} разів")