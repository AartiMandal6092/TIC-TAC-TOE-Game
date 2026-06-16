from tkinter import *

#-------- WINDOW SETUP --------#
root = Tk()
root.title("TIC TAC TOE GAME")
root.geometry("600x650")
root.configure(bg="#1E1E2F")
root.grid_columnconfigure(0, weight=1)

#-------- GAME VARIABLES --------#
current_player = "X"
board=[["","",""],["","",""],["","",""]]

#-------- HANDLE MOVE --------#
def handle_move(btn,row,col):
    if winner_label["text"] != "":
       return
    global current_player
    global board 

    if btn["text"] != "":
         return
    if current_player == "X":
        btn.config(text=current_player, fg="#00C2FF")
    else:
        btn.config(text=current_player, fg="#FF4C60")
    board[row][col]=current_player
    check_winner()

    if current_player == "X":
          current_player = "O"
    else:
        current_player = "X"    


#-------- CHECKING WINNER --------#
def check_winner():
    if board[0][0]==board[0][1]==board[0][2] !="":                    #row check
          winner_label.config(text=current_player + " Wins! 🎉")
          return
    if board[1][0]==board[1][1]==board[1][2] !="":
          winner_label.config(text=current_player + " Wins! 🎉")
          return
    if board[2][0]==board[2][1]==board[2][2] !="":
          winner_label.config(text=current_player + " Wins! 🎉")
          return  
    if board[0][0]==board[1][1]==board[2][2] !="":                    # diagonal check
          winner_label.config(text=current_player + " Wins! 🎉")
          return
    if board[0][2]==board[1][1]==board[2][0] !="":
          winner_label.config(text=current_player + " Wins! 🎉")
          return
    if board[0][0]==board[1][0]==board[2][0] !="":                     #column check
          winner_label.config(text=current_player + " Wins! 🎉")
          return  
    if board[0][1]==board[1][1]==board[2][1] !="":
          winner_label.config(text=current_player + " Wins! 🎉")
          return
    if board[0][2]==board[1][2]==board[2][2] !="":
          winner_label.config(text=current_player + " Wins! 🎉")
          return  
              
    filled =True
    for row in board:
         if "" in row:
              filled = False

    if filled == True and winner_label["text"]=="":
              winner_label.config(text="Match Draw")


#-------- Restart --------#
def restart():
    global board 
    global current_player
    board = [["","",""],["","",""],["","",""]]
    button=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
    for btn in button:
         btn.config(text="",fg="white")
    winner_label.config(text="",fg="white")
    current_player="X"


#-------- DISPLAY/ UI --------#    
button_frame = Frame(root, bg="#1E1E2F")
button_frame.grid(row=1, column=0,pady=15)

title_label = Label(root,text=" 🎮 TIC TAC TOE",font=("Arial",30,"bold"),bg="#1E1E2F",fg="white")
title_label.grid(row=0,column=0,pady=20)

btn1 = Button(button_frame,command= lambda : handle_move(btn1,0,0),font=("Arial", 25, "bold"),bg="#2D2D44",width=6,activebackground="#444466",relief=FLAT,bd=0,fg="white",height=3)
btn1.grid(row=0, column=0,padx=5,pady=5)
btn2 = Button(button_frame,command= lambda : handle_move(btn2,0,1),font=("Arial", 25, "bold"),bg="#2D2D44",width=6,activebackground="#444466",relief=FLAT,bd=0,fg="white",height=3)
btn2.grid(row=0, column=1,padx=5,pady=5)
btn3 = Button(button_frame,command= lambda : handle_move(btn3,0,2),font=("Arial", 25, "bold"),bg="#2D2D44",width=6,activebackground="#444466",relief=FLAT,bd=0,fg="white",height=3)
btn3.grid(row=0, column=2,padx=5,pady=5)

btn4 = Button(button_frame,command= lambda : handle_move(btn4,1,0),font=("Arial", 25, "bold"),bg="#2D2D44",width=6,activebackground="#444466",relief=FLAT,bd=0,fg="white",height=3)
btn4.grid(row=1, column=0,padx=5,pady=5)
btn5 = Button(button_frame,command= lambda : handle_move(btn5,1,1),font=("Arial", 25, "bold"),bg="#2D2D44",width=6,activebackground="#444466",relief=FLAT,bd=0,fg="white",height=3)
btn5.grid(row=1, column=1,padx=5,pady=5)
btn6 = Button(button_frame,command= lambda : handle_move(btn6,1,2),font=("Arial", 25, "bold"),bg="#2D2D44",width=6,activebackground="#444466",relief=FLAT,bd=0,fg="white",height=3)
btn6.grid(row=1, column=2,padx=5,pady=5)

btn7 = Button(button_frame,command= lambda : handle_move(btn7,2,0),font=("Arial", 25, "bold"),bg="#2D2D44",width=6,activebackground="#444466",relief=FLAT,bd=0,fg="white",height=3)
btn7.grid(row=2, column=0,padx=5,pady=5)
btn8 = Button(button_frame,command= lambda : handle_move(btn8,2,1),font=("Arial", 25, "bold"),bg="#2D2D44",width=6,activebackground="#444466",relief=FLAT,bd=0,fg="white",height=3)
btn8.grid(row=2, column=1,padx=5,pady=5)
btn9 = Button(button_frame,command= lambda : handle_move(btn9,2,2),font=("Arial", 25, "bold"),bg="#2D2D44",width=6,activebackground="#444466",relief=FLAT,bd=0,fg="white",height=3)
btn9.grid(row=2, column=2,padx=5,pady=5)

winner_label = Label(root,text="",font=("Arial",20,"bold"),bg="#1E1E2F",fg="white")
winner_label.grid(row=2,column=0,pady=20 )

restart_btn = Button(root,text="Restart",command = restart,font=("Arial",16,"bold"),bg="#FF4C60",fg="white",bd=0,padx=10,pady=5)
restart_btn.grid(row =3,column=0,pady=10)

root.mainloop()
