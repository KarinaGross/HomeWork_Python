# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Было:

# def sum_elem(new_list: list) -> int:
#     count = 0
#     for i in range(1, len(new_list), 2):
#         count += int(new_list[i])
#     return count


# my_list = input('Введите числа через пробел: ').split()

# print(sum_elem(my_list))


# Стало:

# my_list = [int(item) for item in input('Введите числа через пробел: ').split()]
# uneven_index_list = list(filter((lambda x: my_list.index(x) % 2), my_list))

# print(sum(uneven_index_list))












# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Было:

# def product_of_num(new_list: list) -> list:
#     res = []
#     size = len(new_list)
#     if size % 2 == 0:
#         for i in range(size // 2):
#             res.append(new_list[i] * new_list[size - 1 - i])

#     else:
#         for i in range(size // 2):
#             res.append(new_list[i] * new_list[size - 1 - i])
#         res.append(new_list[size // 2] ** 2)
#     return res


# my_list = [int(el) for el in input('Введите числа через пробел: ').split()]

# print(product_of_num(my_list))


# Стало:
# from math import ceil

# my_list = list(map(int, input('Введите числа через пробел: ').split()))
# new_list = [my_list[i] * my_list[-i - 1] for i in range(ceil(len(my_list)/2))]

# print(new_list)









# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Было:

# def string_to_float(new_list: list) -> list:
#     for i in range(len(new_list)):
#         new_list[i] = float(new_list[i])
#     return new_list

# def fractional_part(new_list: list) -> list:
#     result = []
#     for i in range(len(new_list)):
#         result.append(new_list[i] - int(new_list[i]))
#     return result

# def max_minus_min(new_list: list) -> float:
#     return round(max(new_list) - min(new_list), 2)


# my_list = input('Введите через пробел вещественные числа (с точкой): ').split()

# string_to_float(my_list)

# print(max_minus_min(fractional_part(my_list)))


# Стало: 

# def fractional_part(n):
#     return n - int(n)

# my_list = list(map(float, input('Введите через пробел вещественные числа (с точкой): ').split()))
# fract_part_list = list(map(fractional_part, my_list))

# print(round(max(fract_part_list) - min(fract_part_list), 2))






# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# Было:

# from random import randint
# n = int(input('Введите натуральное число: '))
# list = []
# for i in range(n):
#     list.append(randint(-n, n))

# print(list)

# num_pos = input(f'Введите через пробел позиции двух элементов спика (от 0 до {n - 1}): ').split(' ') 

# print(list[int(num_pos[0])] * list[int(num_pos[1])])


# Стало:

# from random import randint
# from functools import reduce

# n = int(input('Введите число: '))
# num_list = [randint(-n, n) for _ in range(n)]

# print(num_list)

# num_pos = list(map(int, input(f'Введите через пробел позиции двух элементов спика (от 0 до {n - 1}): ').split(' ')))

# print(reduce(lambda x, y: x * y, [num_list[num_pos[0]], num_list[num_pos[1]]]))










# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

# Было:
# def fibonachi(n: int) -> list:
#     fib = []
#     f1 = 1
#     f2 = 1
#     fn = 0
#     for _ in range(n):
#         f1 = f2
#         f2 = fn
#         fn = f1 + f2
#         fib.append(fn)
#     return fib

# def nega_fibonachi(n: int) -> list:
#     fib_list = fibonachi(n)
#     result = []
#     result.insert(0, 0)
#     for i in range(n):
#         result.insert(0, fib_list[i] * (-1)**i)
    
#     result.extend(fib_list)
#     return result

    
# number = int(input('Введите число: '))

# print(nega_fibonachi(number))


# Стало: 

# def fibonachi(n: int) -> list:
#     fib = []
#     f1 = 1
#     f2 = 1
#     fn = 0
#     for _ in range(n):
#         f1 = f2
#         f2 = fn
#         fn = f1 + f2
#         fib.append(fn)
#     return fib

# num = int(input('Введите число: '))
# fib_list = fibonachi(num)

# nega_fib_list = [fib_list[i] * (-1)**i for i in range(num)]
# nega_fib_list.reverse()
# print(nega_fib_list + [0] + fib_list)



