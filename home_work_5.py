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

# from msilib import sequence
# import random

# def who_is_1(name1: str, name2: str):
#     if random.randint(0,1):
#         player1 = name1
#         player2 = name2
#     else:
#         player1 = name2
#         player2 = name1
#     return player1, player2

# def victory(players: tuple, first_move: int, k=2021, step=28):
#     whose_move = players[0]

#     k -= first_move
#     while k > 0:
#         k -= random.randint(1, step)
#         if whose_move == players[0]:
#             whose_move = players[1]
#         else:
#             whose_move = players[0]

#     return f'Побеждает {whose_move}!'



# def hint_for_player1(k=2021, step=28):
#     for i in range(1, step+1):
#         if not (k - i) % (step + 1):
#             return i


# print('Введите свои имена: ')
# name1, name2 = input(), input()
# order_move = who_is_1(name1, name2)
# starter = order_move[0]
# second = order_move[1]

# print()

# print(f'{starter} - ты начинаешь игру')
# print(f'Подсказка: {starter}, чтобы победить, возьми на первом ходу {hint_for_player1()} конфет')


# step_player1 = int(input('Твой ход: '))

# print()

# print(victory(order_move, step_player1))














# 3. Создайте программу для игры в ""Крестики-нолики"".


# from tkinter import * 
# from tkinter import messagebox
 
# Player1 = 'X'
# stop_game = False
 
# def clicked(r,c):
     
#     global Player1
    
 
#     if Player1 == "X" and states[r][c] == 0 and stop_game == False:
#         button[r][c].configure(text = "X")
#         states[r][c] = 'X'
#         Player1='O'
 
     
#     if Player1 == 'O' and states[r][c] == 0 and stop_game == False:
#         button[r][c].configure(text = 'O')
#         states[r][c] = "O"
#         Player1 = "X"
 
#     check_if_win()


# def check_if_win():
#     global stop_game
 
#     for i in range(3):
#         if states[i][0] == states[i][1] == states[i][2] !=0:
#             stop_game = True
    
#             messagebox.showinfo("Winner", f"'{states[i][0]}' победили!")
#             break
    
#         elif states [0][i] == states[1][i] == states[2][i] != 0:
#             stop_game = True
    
#             messagebox.showinfo("Winner", f"'{states[0][i]}' победили!")
#             break
    
#         elif states[0][0] == states[1][1] == states[2][2] !=0:
#             stop_game = True
    
#             messagebox.showinfo("Winner", f"'{states[0][0]}' победили!")
#             break
    
#         elif states[0][2] == states[1][1] == states[2][0] !=0:
#             stop_game = True
    
#             messagebox.showinfo("Winner" , f"'{states[0][2]}' победили!")
#             break
    
#         elif states[0][0] and states[0][1] and states[0][2] and states[1][0] and states[1][1] and states[1][2] and states[2][0] and states[2][1] and states[2][2] != 0:
#             stop_game = True
    
#             messagebox.showinfo("tie", "Ничья!")
        


# window = Tk()           
# window.title('Крестики-нолики') 
# window.resizable(0,0)
 
# #Button
# button = [
#      [0,0,0],
#      [0,0,0],
#      [0,0,0]]
 
# #text for buttons
# states = [
#      [0,0,0],
#      [0,0,0],
#      [0,0,0]]
 
# for i in range(3):
#     for j in range(3):
                                          
#         button[i][j] = Button(
#                         height = 4, width = 8,
#                         font = ("Helvetica","20"),
#                         bg='SkyBlue1',
#                         command = lambda r = i, c = j : clicked(r,c))
#         button[i][j].grid(row = i, column = j)
 
 
# mainloop()           








# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from base64 import decode


f = open('text_for_5.4.txt', encoding='UTF-8')
file = f.read()
f.close()


def rle_encode(text):
    if text.isalpha():
        encoding = ''
        prev_char = ''
        count = 1

        for char in text:
            if char != prev_char:
                if prev_char:
                    encoding += str(count) + prev_char
                count = 1
                prev_char = char
            else:
                count += 1
        else:
            encoding += str(count) + prev_char
            return encoding
    else:
        return 'Строка не должна содержать цифры'

def rle_decode(text):
    if not text.isalpha():
        decoding = ''
        count = ''
        for char in text:
            if char.isdigit():
                count += char
            else:
                decoding += char * int(count)
                count = ''
        return decoding
    
    else:
        return 'Строка должна содержать цифры'


print(f'Первоначальная строка: "{file}"')

encoding_data = rle_encode(file)
print(f'Сжатая строка: "{encoding_data}"')

decoding_data = rle_decode(encoding_data)
print(f'Распакованая строка: "{decoding_data}"')

