"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

try:
    number = int(input("Введите целое положительное число: "))
except ValueError:
    print("Вы ввели не целое число")
else:
    result = 0
    concat_number = 0
    for i in range(3):
        concat_number = int(str(concat_number) + str(number))
        result += concat_number
    print(result)
