from tkinter import * 
from tkinter import messagebox
 
Player1 = 'X'
stop_game = False
 
def clicked(r,c):
     
    global Player1
    
 
    if Player1 == "X" and states[r][c] == 0 and stop_game == False:
        button[r][c].configure(text = "X")
        states[r][c] = 'X'
        Player1='O'
 
     
    if Player1 == 'O' and states[r][c] == 0 and stop_game == False:
        button[r][c].configure(text = 'O')
        states[r][c] = "O"
        Player1 = "X"
 
    check_if_win()


def check_if_win():
    global stop_game
 
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] !=0:
            stop_game = True
    
            messagebox.showinfo("Winner", f"'{states[i][0]}' победили!")
            break
    
        elif states [0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True
    
            messagebox.showinfo("Winner", f"'{states[0][i]}' победили!")
            break
    
        elif states[0][0] == states[1][1] == states[2][2] !=0:
            stop_game = True
    
            messagebox.showinfo("Winner", f"'{states[0][0]}' победили!")
            break
    
        elif states[0][2] == states[1][1] == states[2][0] !=0:
            stop_game = True
    
            messagebox.showinfo("Winner" , f"'{states[0][2]}' победили!")
            break
    
        elif states[0][0] and states[0][1] and states[0][2] and states[1][0] and states[1][1] and states[1][2] and states[2][0] and states[2][1] and states[2][2] != 0:
            stop_game = True
    
            messagebox.showinfo("tie", "Ничья!")
        


window = Tk()           
window.title('Крестики-нолики') 
window.resizable(0,0)
 
#Button
button = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]
 
#text for buttons
states = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]
 
for i in range(3):
    for j in range(3):
                                          
        button[i][j] = Button(
                        height = 4, width = 8,
                        font = ("Helvetica","20"),
                        bg='SkyBlue1',
                        command = lambda r = i, c = j : clicked(r,c))
        button[i][j].grid(row = i, column = j)
 
 
mainloop()        


