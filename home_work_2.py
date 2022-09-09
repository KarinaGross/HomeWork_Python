# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*
# - 0,56 -> 11

# n = abs(float(input()))     # нерабочий код, выдает неправильный ответ на числа, состоящие из 0 и 1
# print(n)
# n = int(n * 10**(len(str(n)) - 2))
# print(n)
# sum = 0
# while n > 0:
#     sum += n % 10
#     n //= 10

# print(sum)


n = input().split('.')
sum = 0
for i in range(len(n)):

    n[i] = abs(int(n[i]))

for i in range(len(n)):
    while n[i] > 0:
        sum += n[i] % 10
        n[i] //= 10


print(n)
print(sum)
    




# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input())
# product = 1
# for i in range(1, n + 1):
#     print(product * i, end = ' ')
#     product *= i




# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     print(f'{i}: {round((1 + 1/i) ** i, 2)}', end = '; ')
#     sum += round((1 + 1/i) ** i, 2)
# print()
# print(sum)





# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# from random import randint
# n = int(input('Введите натуральное число: '))
# list = []
# for i in range(n):
#     list.append(randint(-n, n))

# print(list)

# num_pos = input(f'Введите через пробел позиции двух элементов спика (от 0 до {n - 1}): ').split(' ') 

# print(list[int(num_pos[0])] * list[int(num_pos[1])])



# 5. Реализуйте алгоритм перемешивания списка.

# from random import randint

# def mix_list(list_original):
#     list = list_original[:]
#     for i in range(len(list)):
#         index = randint(0, len(list) - 1)

#         temp = list[i]
#         list[i] = list[index]
#         list[index] = temp

#     return list

# elements = input(f'Введите элементы списка через пробел: \n').split()

# print(mix_list(elements))

