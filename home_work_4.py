# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141
# Вычислить число c заданной точностью d Пример: при d = 0.001, 
# π = 3.141.d=0.001,π=3.141.﻿﻿ 10^{-1} ≤ d ≤10^{-10}10 −1 ≤d≤10 −10

# import math 
# def rounding_pi(num: float) -> float:
#     i = 2
#     while num < 1:
#         i += 1
#         num *= 10
#     return str(math.pi)[:i]

# d = float(input('Введите число с плавающей точкой: '))
# print(rounding_pi(d))






# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

# def simpl_numbers(n: int) -> list:
#     result = []
#     k = 0
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 k += 1
#         if k == 0:
#             result.append(i)
#         else:
#             k = 0
#     return result


# def simple_factors(N: int) -> list:
#     result = []
#     for i in simpl_numbers(N):
#             while N % i == 0:
#                 result.append(i)
#                 N //= i
#     return result

# number = int(input('Введите число: '))
# print(f'Список простых множителей числа {number}: {simple_factors(number)}')








# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# def unique_elem(new_list: list) -> list:
#     result = []
#     count = 0
#     for el in new_list:
#         if new_list.count(el) == 1:
#             result.append(el)
            
#     return result


# user_list = [int(el) for el in input('Введите числа через пробел: ').split()]

# print(unique_elem(user_list))






# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools

def coeff_polinom(k: int):
    coeff = [randint(0, 10) for _ in range(k + 1)]
    if coeff[0] == 0:
        coeff[0] = randint(1, 10)
    return coeff

def polinominal(k: int):
    polinom = []
    result = []
    coeff = coeff_polinom(k)
    for i in range(k, -1, -1):
        polinom.append(f'x^{i}')
    for i in range(polinom):
        result.append(f'{coeff[i]}*{polinom[i]}')
    return result

print(polinominal(2))

    





# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.



