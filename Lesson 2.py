# вивести всі непарні числа в діапазоні від і до
number1 = int(input("enter number from:"))
number2 = int(input("enter number to:"))

for i in range(number1, number2+1 ):
    if i%2==1:
        print(i)




'''
    print(x1 + x2)  # додавання
    print(x1 - x2)  # віднімання
    print(x1 * x2)  # множення
    print(x1 ** x2)  # степінь
    print(x1 / x2)  # ділення з дробом
    print(x1 // x2)  # ділення без дробу
    print(x1 % x2)  # остача від ділення

    print(x1 > x2)  # більше
    print(x1 < x2)  # меньше
    print(x1 >= x2)  # більше включно
    print(x1 <= x2)  # меньше включно
    print(x1 == x2)  # рівне
    print(x1 != x2)  # не рівне
'''