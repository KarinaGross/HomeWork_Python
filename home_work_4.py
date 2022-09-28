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
            result = line.split()
        
    # for i in range(len(result)):
    #     result[i] = result[i].split('*')

    # result = sum(result, [])
    return result
    
pol1 = get_polinom('polinom_4.5.1.txt')
pol2 = get_polinom('polinom_4.5.2.txt')
print(pol1)
print(pol2)

# def sum_polinom(lst_pol1: list, lst_pol2: list) -> list:
#     lst_pol1.reverse()
#     lst_pol2.reverse()
#     result = []
#     max_len = max(len(lst_pol1), len(lst_pol2))
#     for i in range(max_len):
#         if i == 1:
#         result.append(int(lst_pol1[i]) + int(lst_pol2[i]))

#         if 
    
#     result.reverse()
#     return result
        
# print(sum_polinom(pol1, pol2))

# def couple_elements(lst_pol1: list, lst_pol2: list) -> list:
#     result = []
#     for i in range(len(lst_pol1)):
#         for j in range(len(lst_pol2)):
#             if lst_pol1[i + 1] == lst_pol2[i + 1]:
#                 if lst_pol1[i].isdigit() and lst_pol2.isdigit():
#                     sum_coef = int(lst_pol1[i]) + int(lst_pol2[i])
#                     result.append(f'{sum_coef}*{lst_pol1[i + 1]}')
#                 else:


# def sum_polinom(lst_pol1: list, lst_pol2: list) -> list:
#     result = []
#     for i in range(len(lst_pol1)):
#         for j in range(len(lst_pol2)):
#             if lst_pol1[i][-1] == lst_pol2[j][-1]:
#                 if lst_pol1[i][-1].isdigit() and lst_pol2[j][-1].isdigit():
#                     lst_pol1[i] = lst_pol1[i].split('*')
#                     lst_pol2[j] = lst_pol2[j].split('*')
#                     sum_coef = int(lst_pol1[i][0]) + int(lst_pol2[j][0])
#                     result.append(f'{sum_coef}*{lst_pol1[i][1]}')
#                     break
#                 else:
#                     result.append(lst_pol1[i])
#                     break
            
#             elif lst_pol1[i] == lst_pol2[j] == '+':
#                 result.append(lst_pol1[i])
#                 break
#     return result


def sum_polinom(lst_pol1: list, lst_pol2: list) -> list:
    general_list = lst_pol1 + lst_pol2
    result = lst_pol1
    for i in range(len(lst_pol1)):
        for j in range(len(lst_pol2)):
            if result[i] == lst_pol2[j]:
                # if not general_list[i].isalnum():
                #     del general_list[j]

                if result[i].isdigit():
                    result[i] = str(int(result[i]) + int(lst_pol2[j]))
                    # del general_list[j]

            elif result[i][-1] == lst_pol2[j][-1]:
                if not result[i][-1].isdigit():
                    elem_i = result[i].split('*')
                    elem_j = lst_pol2[j].split('*')
                    sum_coef = int(elem_i[0]) + int(elem_j[0])
                    result[i] = f'{sum_coef}*{elem_i[1]}'
                # del general_list[j]

    return result

print(sum_polinom(pol1, pol2))
                
            



# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# def sum_of_polynimials(polynomials_1: list[str], polynomials_2: list[str]) ->list:

# def getting_list_functions(file_name: str) ->list:
    
#     with open(f'Homework/Seminar_4/005_sum_of_polynomials/{file_name}', 'r') as file:
#         polynomials = file.read().split('\n')
#     for i in range(len(polynomials)):
#         polynomials[i] = polynomials[i].replace(' = 0', '').split(' + ')
#         for k in range(len(polynomials[i])):
#             polynomials[i][k] = polynomials[i][k].split('*')
    
#     return polynomials

# def write_to_file(name_file: str, text: str):
#     with open(f'Homework/Seminar_4/005_sum_of_polynomials/{name_file}', 'a') as file:
#         file.write(f'{text}\n')

# def sum_polynomials(polynomials_1: list, polynomials_2: list) -> str:

#     polynomials_max_len = polynomials_1
#     polynomials_min_len = polynomials_2
#     if polynomials_1 < polynomials_2:
#         polynomials_max_len = polynomials_2
#         polynomials_min_len = polynomials_1

#     result= ''
#     for i in range(len(polynomials_max_len)):
#         if len(polynomials_max_len[i]) != 1:
#             for k in range(len(polynomials_min_len)):
#                 if len(polynomials_min_len[k]) != 1:
#                     if  polynomials_max_len[i][1] == polynomials_min_len[k][1]:
#                         result += f"{int(polynomials_max_len[i][0]) + int(polynomials_min_len[k][0])}*{polynomials_max_len[i][1]}"
#                         break
#                 elif (k == len(polynomials_min_len) - 1):
#                     result += f'{polynomials_max_len[i][0]}*{polynomials_max_len[i][1]}'
#         else:
#             for k in range(len(polynomials_min_len)):
#                 if len(polynomials_min_len[k]) == 1:
#                     result += f'{int(polynomials_max_len[i][0])+ int(polynomials_min_len[k][0])}'
            
#         if i != (len(polynomials_max_len) -1):
#                 result += ' + ' 
#     return result + ' = 0'


# polynomials_1 = getting_list_functions('polynomial_1.txt')
# polynomials_2 = getting_list_functions('polynomial_2.txt')

# new_polynomials = []
# for i in range(len(polynomials_1)):
#     new_polynomials.append(sum_polynomials(polynomials_1[i], polynomials_2[i]))

# for i in new_polynomials:
#     write_to_file('Sum.txt', i)

