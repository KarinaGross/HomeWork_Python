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

# from random import randint

# def create_polinominal(k: int) -> str:
    
#     polinom = ''
#     for degree in range(k, -1, -1):
#         if degree == k:
#             coeff = randint(0,3)
#             if coeff == 0:
#                 polinom += f'{coeff + 1}*x^{degree} '
        
#         elif degree > 1:
#             coeff = randint(0, 99)
#             if coeff == 0:
#                 continue
#             else:
#                 if len(polinom) > 0:
#                     polinom += '+ '
#                 polinom += f'{coeff}*x^{degree} '

#         elif degree == 1:
#             coeff = randint(0, 99)
#             if coeff == 0:
#                 continue
#             else:
#                 if len(polinom) > 0:
#                     polinom += '+ '
#                 polinom += f'{coeff}*x '

#         elif degree == 0:
#             coeff = randint(0,99)
#             if len(polinom) > 0:
#                 if coeff == 0:
#                     continue
#                 else:
#                     if len(polinom) > 0:
#                         polinom += '+ '
#                     polinom += f'{coeff} '
#             else:
#                 break

#     polinom += '= 0'
    
#     return polinom


# k = int(input('Введите степень: '))


# with open("Polinominal.txt", 'a') as file:
#     file.write(f'\n{create_polinominal(k)}')

    







# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.




def get_polinom(file_name: str) -> list:
    with open(f'{file_name}') as file:
        while True:
            line = file.readline()
            if not line:
                break
            result = line
    return result
    

def write_to_file(name_file: str, text: str):
    with open(f'{name_file}', 'a') as file:
        file.write(f'{text}\n')


def sum_polinom(lst_pol1: str, lst_pol2: str) -> str:
    pol1 = lst_pol1[:-4].split(' + ')
    pol2 = lst_pol2[:-4].split(' + ')
    general_list = pol1 + pol2
    general_list = [item.split('*') for item in general_list]
    for i in range(len(pol1)):
        for j in range(len(pol1), len(general_list)):
            # if general_list[i].isdigit() and general_list[j].isdigit():
            #     general_list[i] = f'{int(general_list[i]) + int(general_list[j])}'
            #     general_list[j] = 0
            if len(general_list[i]) == len(general_list[j]) == 2:
                if general_list[i][1] == general_list[j][1]:
                    sum_coef = int(general_list[i][0]) + int(general_list[j][0])
                    # result.append(f'{sum_coef}*{general_list[i][1]}')
                    general_list[i] = f'{sum_coef}*{general_list[i][1]}'
                    general_list[j] = ''
                    

            elif len(general_list[i]) == 1:
                if len(general_list[j]) == 1:
                    elem1 = int(general_list[i][0])
                    elem2 = int(general_list[j][0])
                    general_list[i] = f'{elem1 + elem2}'
                    general_list[j] = ''


    result = []
    for i in range(len(general_list)):
        if type(general_list[i]) == list:
            result.append('*'.join(general_list[i]))
        elif general_list[i] != '':
            result.append(general_list[i])
    
    result = ' + '.join(result) + ' = 0'


    return result


pol1 = get_polinom('polinom_4.5.1.txt')
pol2 = get_polinom('polinom_4.5.2.txt')


write_to_file('sum.txt', sum_polinom(pol1, pol2))
            

