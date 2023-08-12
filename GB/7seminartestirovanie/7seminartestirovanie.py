# # if True:
# #     print(1)

# #1
# def fun1(x,y):
#     return x+y

# print(fun1(5,3))

# #2
# fun2 = lambda x,y: x+y

# print(fun1(5,3))

# #3
# print((lambda x,y: x+y)(5,3))


str1 = "2 4 2 7 9 1"
print(str1)

lst1 = str1.split()
print(lst1)

lst2 = list(map(int, lst1))
print(lst2)

lst3 = list(map(lambda x: x*3 , lst2))
print(lst3)

lst4 = list(filter(lambda x: x % 3==0, lst2))
print(lst4)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Задача No47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values)) 
# if values == transformed_values:
# print(‘ok’) else:
# print(‘fail’)
# Вывод:
# ok

# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values)) 
# lambda values[i]: values[i] = transformed_values


#~~~~~~~~~~~~~~~~~~~~~~
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values:
#  print('ok')
# else:
#  print('fail')
#~~~~~~~~~~~~~~~~~~~~~~~~~


# с помощью лямбда и фильтра составить список из  двух значных чисел. ввод "2 10 -32 8 1 78", вывод [10, -32, 78] /// ["10", "-32", "78"]

# str1 = "2 10 -32 8 1 78"
# print(str1)

# lst2 = str1.split()
# print(lst2)

# # lst3 = int(lst2)
# # print(lst3)

# lst4 = list(filter(lambda x: x >= "10", lst2))
# print(lst4)

#~~~~~~~~~~~~~~~~~~~~~~~~

# lst2 = "2 10 -32 8 1 78"
# print(lst2)
# lst4 = list(filter(lambda x: 9<abs(x)<100, map(int, lst2.split())))
# print(lst4)

# list3 = list(filter( lambda x: len(str(abs(int(x))))==2, lst2.split()))
# print(list3)




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Задача No49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. 
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Пример ввода и вывода данных представлены на следующем слайде
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
# print(orbits)
# list_of_orbits= str(orbits)
# print(list_of_orbits)
# def find_farthest_orbit(list_of_orbits)

























































# C seminara DZ
# def criterion(candidat, lowLimit, upLimit) :  # возвращает True когда candidat удовлетворяет условию
# # в данном случае не менее lowLimit  и не более upLimit
#     if lowLimit <= candidat < upLimit :
#         return True
#     else :
#         return False

# ml = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# lowB = int(input("задайте нижнюю границу:= "))
# upB = int(input("задайте верхнюю границу:= "))
# ind_res = []
# for i in range(len(ml)) : # привычнее бежать по индексам 
# #    if lowB <= i < upB :
#     if criterion(ml[i], lowB, upB) :
#         ind_res.append(i) # дополняем список индексом, для которого элемент с этим индексом удовлетворяет условию  
# #        print(i, ml[i]) # отладочная печать пары индекс и значение, удовлетворяющее условию 
# print("в списке:")
# print(ml)
# print("в интервале значений больше или равно ",lowB," но менее ", upB," лежат элементы с индексами")
# print(ind_res)







