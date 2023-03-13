"""
Задача 2: Найдите сумму цифр трехзначного числа.
"""
try:
    number = int(input("Введите трехзначное число: "))
except ValueError:
    print("Вы ввели не число")
else:
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    print(f"Сумма всех цифр числа равна {result}")
