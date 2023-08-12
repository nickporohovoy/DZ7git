# поределить простое число или составное

# def celchislo(a):
#     if a == int(a/a) and int(a/1):
#         return print(f"chislo {a} prostoe")
#     return print(f"chislo {a} sostavnoe")

# a = int(input('Введите число(a): '))
# print(celchislo(a))

#````````````````````````````````````````````````````

# def simple(n, del1 = 2):
#     if n == 2 or del1*del1 > n:
#         return print('{} - prostoe chislo'.format(n))
#     elif n % del1 == 0:
#         return print('{} -sostavnoe chislo'.format(n))
#     return simple(n, del1 + 1)
# simple(11)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# определить является ли слово палиндромом

# def polindrom(n):
#     if len(n) < 1:
#         return print('ne dostatochno simvolov: ')
#     else:
#         if n[0] == n[-1]:
#             return polindrom(n[1:-1])
#         else:
#             return print(f'{n} ne polindrom') 
        
# n = str(input('Введите число(a): '))
# polindrom(n)

#````````````````````````````````````````````````````

# def is_palindrome(s):
#     if len(s) < 1:
#         return True
#     else:
#         if s[0] == s[-1]:
#             return is_palindrome(s[1:-1])
#         else:
#             return False
# a = str(input("Введите строку:"))
# if (is_palindrome(a) == True):
#     print("Данная строка палиндром!")
# else:
#     print("Данная строка не палиндром!")

#````````````````````````````````````````````````````

# def isP(s) :
#     if len(s) <=1 :
#         return True
#     return isP(s[1:len(s)-1]) and (s[0] == s[len(s)-1])

# ss = input("введите слово:=")
# print(isP(ss))

#````````````````````````````````````````````````````

# def isP(s):
#     if len(s) <= 1:
#         return True
#     elif s[0]==s[-1]:
#         return isP(s[1:-1])
#         12321
#     else:
#         return False
# ss = input("vvedite:=")
# print(isP(ss))

#````````````````````````````````````````````````````

# print(list(range(3,10)))

# a = '123456789'

# print(a[1:-1])
# print(a[:-1])

#````````````````````````````````````````````````````

# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод: Вывод:
# 300   220 284

# n = 300
# def druzh(n)
    
# for i in range(n):
#     summa = 0
#     for j in range(1, i // 2 + 1):
#         if i % j == 0:









