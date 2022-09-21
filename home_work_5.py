# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".


# f = open('text_for_5.1.txt', encoding='UTF-8')
# file = f.read()
# f.close()

# delete_word = 'абв'
# split_file = file.split()

# filtered_str = ' '.join(list(filter(lambda word: delete_word not in word, split_file)))

# print(file)
# print(filtered_str)





# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все 
# конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from msilib import sequence
import random

def who_is_1(name1: str, name2: str):
    if random.randint(0,1):
        player1 = name1
        player2 = name2
    else:
        player1 = name2
        player2 = name1
    return player1, player2

def victory(players: tuple, first_move: int, k=2021, step=28):
    whose_move = players[0]

    k -= first_move
    while k > 0:
        k -= random.randint(1, step)
        if whose_move == players[0]:
            whose_move = players[1]
        else:
            whose_move = players[0]

    return f'Побеждает {whose_move}!'



def hint_for_player1(k=2021, step=28):
    for i in range(1, step+1):
        if not (k - i) % (step + 1):
            return i


print('Введите свои имена: ')
name1, name2 = input(), input()
order_move = who_is_1(name1, name2)
starter = order_move[0]
second = order_move[1]

print()

print(f'{starter} - ты начинаешь игру')
print(f'Подсказка: {starter}, чтобы победить, возьми на первом ходу {hint_for_player1()} конфет')


step_player1 = int(input('Твой ход: '))

print()

print(victory(order_move, step_player1))







# Создайте программу для игры в ""Крестики-нолики"".

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.






























# from tkinter import *

# window = Tk()
# label = Label(
#     text='Начинаем игру!',
#     foreground='saddle brown',
#     background='peach puff',
#     width=20,
#     height=10
#     )

# label.pack()
# window.mainloop()


# button = Button(
#     text='Начинаем игру!',
#     foreground='saddle brown',
#     background='peach puff',
#     width=20,
#     height=10
#     )

# button.pack()
# window.mainloop()


# label = Label(text='Сколько конфет вы возьмете?')
# entry = Entry()
# count = entry.get()

# label.pack()
# entry.pack()
# window.mainloop()
