# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_elem(new_list: list) -> int:
#     count = 0
#     for i in range(1, len(new_list), 2):
#         count += int(new_list[i])
#     return count


# my_list = input('Введите числа через пробел: ').split()

# print(sum_elem(my_list))







# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

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

# def string_to_int(new_list: list) -> list:
#     for i in range(len(new_list)):
#         new_list[i] = int(new_list[i])
#     return new_list


# my_list = input('Введите числа через пробел: ').split()

# string_to_int(my_list)
# print(product_of_num(my_list))









# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

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
#     return round(max(new_list) - min(new_list), 4)



# my_list = input('Введите через пробел вещественные числа (с точкой): ').split()

# string_to_float(my_list)

# print(max_minus_min(fractional_part(my_list)))







# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def dec_to_bin(number: int):
#     bin_num = ''
#     while number > 0:
#         bin_num += str(number % 2)
#         number //= 2
#     return bin_num[::-1]

# dec_num = int(input('Введите десятичное число: '))

# print(f'Число {dec_num} в двоичной системе равно {dec_to_bin(dec_num)}')






# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


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
