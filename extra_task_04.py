"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""

try:
    n = int(input("Введите количество строк в шоколадке: "))
    m = int(input("Введите количество столбцов в шоколадке: "))
    k = int(input("Введите количество долек, которые необходимо отломить: "))
except ValueError:
    print("Вы ввели не целое число")
else:
    if k > n * m or k == 1 and (n < 1 or m < 1):
        print("Невозможно отломить заданное количество долек.")
    else:
        if k % n == 0 or k % m == 0:
            print("Можно отломить заданное количество долек.")
        else:
            print("Невозможно отломить заданное количество долек.")
