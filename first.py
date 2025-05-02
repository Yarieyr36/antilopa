import random

# Завдання 1: Запит ім'я та вік
name = input("Введіть своє ім'я: ")
age = input("Введіть свій вік: ")
print(f"Привіт {name}, тобі {age}!")

# Завдання 2: Перевірка віку для доступу
age = int(input("Введіть свій вік: "))
if age >= 14:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

# Завдання 3: Гра "Вгадай число"
secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Вгадайте число від 1 до 10: "))
    if guess == secret_number:
        print("Вітаємо! Ви вгадали!")
        break
    elif guess > secret_number:
        print("Менше!")
    else:
        print("Більше!")
    attempts -= 1
if attempts == 0:
    print(f"Ви програли! Загадане число було {secret_number}.")

# Завдання 4: Виведення чисел в діапазоні
start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))
for num in range(start, end + 1):
    print(num, end=" ")

print("\n")

# Завдання 5: Виведення парних чисел у зворотному порядку
n = int(input("Введіть число n: "))
for num in range(n, 0, -1):
    if num % 2 == 0:
        print(num, end=" ")

print("\n")

# Завдання 6: Обчислення факторіалу
n = int(input("Введіть число для обчислення факторіалу: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факторіал {n} = {factorial}")

# Завдання 7: Визначення оцінки за балами
score = int(input("Введіть кількість отриманих балів: "))
if score < 50:
    print("Оцінка: Незадовільно.")
elif 50 <= score <= 69:
    print("Оцінка: Задовільно.")
elif 70 <= score <= 89:
    print("Оцінка: Добре.")
else:
    print("Оцінка: Відмінно.")

# Завдання 8: Калькулятор
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть математичну дію (+, -, *, /): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b == 0:
        result = "Помилка: Ділення на нуль!"
    else:
        result = a / b
else:
    result = "Невідома операція!"

print(f"Результат: {result}")
