# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = 3
# b = 5

# def stepen(a, b):
#     if b == 0:
#         return 1
#     return a * stepen(a, b - 1)

# a = int(input('Введите число(a): '))
# b = int(input('Введите степень(b): '))
# print(stepen(a, b))

#``````````````````````````````````````````````````````````
# def f(a, b):
#     if b == 0:
#         return 1
#     return a * f(a, b-1)
#``````````````````````````````````````````````````````````

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 2 2
# 4

# def reksum(a, b):
#     if b == 0:
#         return a
#     return reksum(a + 1, b - 1)

# a = int(input('Введите 1 число(a): '))
# b = int(input('Введите 2 число(b): '))
# print(reksum(a, b))

#``````````````````````````````````````````````````````````
# def sum(a, b):
#     return b
#``````````````````````````````````````````````````````````