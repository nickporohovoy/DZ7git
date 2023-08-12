# найти факториал числа N через рекурсию

# def fact(n) :
#     if n == 0 :
#         return 1
#     return fact((n)-1)*n
# num = int(input("Задайте число: "))
# print(fact(num))



# Задача No31. Решение в группах
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21


# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1 or n ==2 :
#         return 1
#     return fibo(n-1)+fibo(n-2)

# num = int(input("zadaite xbckj: "))
# listF1 =[0]
# for i in range(1, num+1):
#     listF1.append(fibo(i))
# print(listF1)

# listF2 =[0,1,1]
# for i in range(3, num+1):
#     listF2.append(listF2[i-1]+listF2[i-2])
# print(listF2)



# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3


def convers(n):
    if n ==0 :
        return "+"
    ss = input("vvedite simvol:" )
    return convers(n-1)+ss

print(convers(5))


# def convers(n) :
#     if n == 0 :
#         return "+"
#     ss = input("введите символ:")
#     return convers(n-1)+ss

# def convers2(n) :
#     if n == 0 :
#         return "%"
#     ss = input("введите символ:")
#     return ss+convers2(n-1)
# print(convers(5))
# print(convers2(5))










# fib1 = 1
# fib2 = 1
 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
 
# print("Значение этого элемента:", fib2)
































