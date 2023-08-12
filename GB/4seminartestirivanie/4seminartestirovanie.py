# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# s = "a a a b c a a d c d d" .split()
# print(s)
# my_dict = {n: s.count(n) for n in s}
# print (my_dict)

# s = "a a a b c a a d c d d" .split()
# print(s)
# my_dict = {}
# print (my_dict)
# for v in s:
#     if v not in my_dict:
#         print(v, end = " ")
#         my_dict[v] = 1
#     else:
#         print(f"{v}_{my_dict[v]}", end = " ")
#         my_dict[v] += 1
#     my_dict[v] = my_dict.get(v, 0) +1

# stroka = 'a a b c'.split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#         result[i] += 1
#     else:
#         print(i, end=' ')
#         result[i] = 1


# a = input()
# b = input()
# m = {камень-ножницы-бумага и тд}
# c = a + '-' + bprint(m[c])


tel = '+79619338810 +79934990997 +77051067224'.split()
a = {}
for i in tel:
    key = i[:2]
    print(key)
    if key not in a:
        a[key] = [i] # i записываем в значение
    else:
        a[key] += [i] # [a] = [a] + i
print(a)


























