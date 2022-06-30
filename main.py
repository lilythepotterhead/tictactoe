from tkinter import *
from tkinter import messagebox
x=Tk()
x.title("tic tac toe")
x.geometry("750x650")
x.resizable(False,False)
frame=Frame(x)
player1=""
player2=""
ifj=False
namescore=0
name1score=0
turn=""
namescorelabel = Label(x, text=namescore, font=("", 15))
name1scorelabel = Label(x, text=name1score, font=("", 15))
cell00=Label(x)
cell01=Label(x)
cell02=Label(x)
cell10=Label(x)
cell11=Label(x)
cell12=Label(x)
cell20=Label(x)
cell21=Label(x)
cell22=Label(x)
name2=Label(x,font=("",45))
def winning():
    if cell00["text"]==cell01["text"]==cell02["text"]=="X" or cell00["text"]==cell01["text"]==cell02["text"]=="O":
        return True
    elif cell00["text"]==cell10["text"]==cell20["text"]=="X" or cell00["text"]==cell10["text"]==cell20["text"]=="O":
        return True
    elif cell00["text"]==cell11["text"]==cell22["text"]=="X" or cell00["text"]==cell11["text"]==cell22["text"]=="O":
        return True
    elif cell10["text"]==cell11["text"]==cell12["text"]=="X" or cell10["text"]==cell11["text"]==cell12["text"]=="O":
        return True
    elif cell20["text"]==cell21["text"]==cell22["text"]=="X" or cell20["text"]==cell21["text"]==cell22["text"]=="O":
        return True
    elif cell02["text"]==cell11["text"]==cell20["text"]=="X" or cell02["text"]==cell11["text"]==cell20["text"]=="O":
        return True
    elif cell01["text"]==cell11["text"]==cell21["text"]=="X" or cell01["text"]==cell11["text"]==cell21["text"]=="O":
        return True
    elif cell02["text"]==cell12["text"]==cell22["text"]=="X" or cell02["text"]==cell12["text"]==cell22["text"]=="O":
        return True
    else:
        return False
def deleting():
    cell00.config(text='')
    cell01.config(text='')
    cell02.config(text='')
    cell10.config(text='')
    cell11.config(text='')
    cell12.config(text='')
    cell20.config(text='')
    cell21.config(text='')
    cell22.config(text='')
    namescorelabel.config(text=namescore)
    name1scorelabel.config(text=name1score)
def tie():
    if cell00["text"]!='' and cell01["text"]!='' and cell02["text"]!='' and cell10["text"]!='' and cell11["text"]!='' and cell12["text"]!='' and cell00["text"]!='' and cell20["text"]!='' and cell21["text"]!='' and cell22["text"]!='':
        messagebox.showinfo("Tie","There is a tie")
        deleting()
def act00(r):
    global turn,name,namescore,name1score
    if cell00["text"]=="X" or cell00["text"]=="O":
        return
    if turn==player1:
        cell00.config(text="X",fg="#c785ed",font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="X won!"+player1)
            namescore+=1
            deleting()
        turn=player2
    elif turn==player2:
        cell00.config(text="O", fg="#ed85da", font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning", message="O won!" + player2)
            name1score += 1
            deleting()
        turn=player1
    name2.config(text=turn,fg="black")
    tie()
def act01(r):
    global turn,namescore,name1score
    if cell01["text"]=="X" or cell01["text"]=="O":
        return
    if turn==player1:
        cell01.config(text="X",fg="#c785ed",font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="X won!"+player1)
            namescore += 1
            deleting()
        turn=player2
    elif turn==player2:
        cell01.config(text="O", fg="#ed85da", font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="O won!"+player2)
            name1score += 1
            deleting()
        turn=player1
    name2.config(text=turn,fg="black")
    tie()
def act02(r):
    global turn,namescore,name1score
    if cell02["text"]=="X" or cell02["text"]=="O":
        return
    if turn==player1:
        cell02.config(text="X",fg="#c785ed",font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="X won!"+player1)
            namescore += 1
            deleting()
        turn=player2
    elif turn==player2:
        cell02.config(text="O", fg="#ed85da", font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="O won!"+player2)
            name1score += 1
            deleting()
        turn=player1
    name2.config(text=turn,fg="black")
    tie()
def act10(r):
    global turn,namescore,name1score
    if cell10["text"]=="X" or cell10["text"]=="O":
        return
    if turn==player1:
        cell10.config(text="X",fg="#c785ed",font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="X won!"+player1)
            namescore += 1
            deleting()
        turn=player2
    elif turn==player2:
        cell10.config(text="O", fg="#ed85da", font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="O won!"+player2)
            name1score += 1
            deleting()
        turn=player1
    name2.config(text=turn, fg="black")
    tie()
def act11(r):
    global turn,namescore,name1score
    if cell11["text"]=="X" or cell11["text"]=="O":
        return
    if turn==player1:
        cell11.config(text="X",fg="#c785ed",font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="X won!"+player1)
            namescore += 1
            deleting()
        turn=player2
    elif turn==player2:
        cell11.config(text="O", fg="#ed85da", font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="O won!"+player2)
            name1score += 1
            deleting()
        turn=player1
    name2.config(text=turn,fg="black")
    tie()
def act12(r):
    global turn,namescore,name1score
    if cell12["text"]=="X" or cell12["text"]=="O":
        return
    if turn==player1:
        cell12.config(text="X",fg="#c785ed",font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="X won!"+player1)
            namescore += 1
            deleting()
        turn=player2
    elif turn==player2:
        cell12.config(text="O", fg="#ed85da", font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="O won!"+player2)
            name1score += 1
            deleting()
        turn=player1
    name2.config(text=turn,fg="black")
    tie()
def act20(r):
    global turn,namescore,name1score
    if cell20["text"]=="X" or cell20["text"]=="O":
        return
    if turn==player1:
        cell20.config(text="X",fg="#c785ed",font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="X won!"+player1)
            namescore += 1
            deleting()
        turn=player2
    elif turn==player2:
        cell20.config(text="O", fg="#ed85da", font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="O won!"+player2)
            name1score += 1
            deleting()
        turn=player1
    name2.config(text=turn,fg="black")
    tie()
def act21(r):
    global turn,namescore,name1score
    if cell21["text"]=="X" or cell21["text"]=="O":
        return
    if turn==player1:
        cell21.config(text="X",fg="#c785ed",font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="X won!"+player1)
            namescore += 1
            deleting()
        turn=player2
    elif turn==player2:
        cell21.config(text="O", fg="#ed85da",font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="O won!"+player2)
            name1score += 1
            deleting()
        turn=player1
    name2.config(text=turn,fg="black")
    tie()
def act22(r):
    global turn,namescore,name1score
    if cell22["text"]=="X" or cell22["text"]=="O":
        return
    if turn==player1:
        cell22.config(text="X",fg="#c785ed",font=("",50))
        if winning()==True:
            namescore += 1
            deleting()
        turn=player2
    elif turn==player2:
        cell22.config(text="O", fg="#ed85da", font=("",50))
        if winning()==True:
            messagebox.showinfo(title="Winning",message="O won!"+player2)
            name1score += 1
            deleting()
        turn=player1
    name2.config(text=turn,fg="black")
    tie()
def fwehh(e):
    global player1,player2,ifj,namescore,name1score,turn,name
    if ifj == True:
        return
    player1=player1entry.get()
    player2=player2entry.get()
    if player1=="" or player2=="":
        return
    frame.destroy()
    turn=player1
    ifj=True
    name=Label(x,text=player1,font=("",15))
    name1=Label(x,text=player2,font=("",15))
    name.place(relx=0, rely=0)
    name1.place(relx=0.85, rely=0)
    #lines
    vline1=Frame(x,bg="black",height=500,width=5)
    vline2=Frame(x,bg="black",height=500,width=5)
    hline1=Frame(x,bg="black",height=5,width=600)
    hline2=Frame(x,bg="black",height=5,width=600)
    vline1.place(relx=0.35,rely=0.1)
    vline2.place(relx=0.65,rely=0.1)
    hline1.place(relx=0.1,rely=0.35)
    hline2.place(relx=0.1,rely=0.63)
    #score

    namescorelabel.place(relx=0.04,rely=0.04)
    name1scorelabel.place(relx=0.9,rely=0.04)

    #cells
    cell00.place(relx=0.1,rely=0.1,relheight=0.24,relwidth=0.24)
    cell01.place(relx=0.36, rely=0.1, relheight=0.24, relwidth=0.28)
    cell02.place(relx=0.66, rely=0.1, relheight=0.24, relwidth=0.24)
    cell10.place(relx=0.1, rely=0.36, relheight=0.26, relwidth=0.24)
    cell11.place(relx=0.36, rely=0.36, relheight=0.26, relwidth=0.28)
    cell12.place(relx=0.66, rely=0.36, relheight=0.26, relwidth=0.24)
    cell20.place(relx=0.1, rely=0.64, relheight=0.23, relwidth=0.24)
    cell21.place(relx=0.36, rely=0.64, relheight=0.23, relwidth=0.28)
    cell22.place(relx=0.66, rely=0.64, relheight=0.23, relwidth=0.24)
    cell00.bind("<Button-1>",act00)
    cell01.bind("<Button-1>", act01)
    cell02.bind("<Button-1>", act02)
    cell10.bind("<Button-1>", act10)
    cell11.bind("<Button-1>", act11)
    cell12.bind("<Button-1>", act12)
    cell20.bind("<Button-1>", act20)
    cell21.bind("<Button-1>", act21)
    cell22.bind("<Button-1>", act22)
    #turns
    name2.place(relx=0.3, rely=0.9)
player1entry=Entry(frame,font=("",15))
player1label=Label(frame,text="Player 1's name:",font=("",15))
player2entry=Entry(frame,font=("",15))
player2label=Label(frame,text="Player 2's name:",font=("",15))
x.bind("<Return>",fwehh)
frame.pack()
player1label.grid(row=0,column=0)
player1entry.grid(row=0,column=1)
player2label.grid(row=1,column=0)
player2entry.grid(row=1,column=1)
x.mainloop()