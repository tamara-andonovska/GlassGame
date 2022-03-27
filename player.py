import socket
import sys, os
import tkinter

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1245)) # se koristi loopback adresata, zasto i serverot i klientot kje se startuvani na istata masina
data = s.recv(1024).decode() # ova e prvata poraka sto ja objasnuva igrata
print(data)

master=tkinter.Tk()
master.title("Glass game")
master.geometry("850x750")

master.configure(bg='dark grey')

text_box = tkinter.Text(master, width = 99, height = 3)
text_box.grid(row = 17, column = 1, columnspan = 4)

text_box.insert("end-1c", data)
text_box.configure(state='disabled', bg = "#B32727")

left1=tkinter.Button(master, text="L1", command = lambda: clickedBtn("L1"),height=3,width=6)
left1.grid(row=1,column=1,columnspan=2,rowspan=2)

left2=tkinter.Button(master, text="L2", command = lambda: clickedBtn("L2"),height=3,width=6)
left2.grid(row=3,column=1,columnspan=2,rowspan=2)

left3=tkinter.Button(master, text="L3", command = lambda: clickedBtn("L3"),height=3,width=6)
left3.grid(row=5,column=1,columnspan=2,rowspan=2)

left4=tkinter.Button(master, text="L4", command = lambda: clickedBtn("L4"),height=3,width=6)
left4.grid(row=7,column=1,columnspan=2,rowspan=2)

left5=tkinter.Button(master, text="L5", command = lambda: clickedBtn("L5"),height=3,width=6)
left5.grid(row=9,column=1,columnspan=2,rowspan=2)

left6=tkinter.Button(master, text="L6", command = lambda: clickedBtn("L6"),height=3,width=6)
left6.grid(row=11,column=1,columnspan=2,rowspan=2)

left7=tkinter.Button(master, text="L7", command = lambda: clickedBtn("L7"),height=3,width=6)
left7.grid(row=13,column=1,columnspan=2,rowspan=2)

left8=tkinter.Button(master, text="L8", command = lambda: clickedBtn("L8"),height=3,width=6)
left8.grid(row=15,column=1,columnspan=2,rowspan=2)

right1=tkinter.Button(master, text="R1", command = lambda: clickedBtn("R1"),height=3,width=6)
right1.grid(row=1,column=3,columnspan=2,rowspan=2)

right2=tkinter.Button(master, text="R2", command = lambda: clickedBtn("R2"),height=3,width=6)
right2.grid(row=3,column=3,columnspan=2,rowspan=2)

right3=tkinter.Button(master, text="R3", command = lambda: clickedBtn("R3"),height=3,width=6)
right3.grid(row=5,column=3,columnspan=2,rowspan=2)

right4=tkinter.Button(master, text="R4", command = lambda: clickedBtn("R4"),height=3,width=6)
right4.grid(row=7,column=3,columnspan=2,rowspan=2)

right5=tkinter.Button(master, text="R5", command = lambda: clickedBtn("R5"),height=3,width=6)
right5.grid(row=9,column=3,columnspan=2,rowspan=2)

right6=tkinter.Button(master, text="R6", command = lambda: clickedBtn("R6"),height=3,width=6)
right6.grid(row=11,column=3,columnspan=2,rowspan=2)

right7=tkinter.Button(master, text="R7", command = lambda: clickedBtn("R7"),height=3,width=6)
right7.grid(row=13,column=3,columnspan=2,rowspan=2)

right8=tkinter.Button(master, text="R8", command = lambda: clickedBtn("R8"),height=3,width=6)
right8.grid(row=15,column=3,columnspan=2,rowspan=2)

left2['state'] = 'disabled'
left3['state'] = 'disabled'
left4['state'] = 'disabled'
left5['state'] = 'disabled'
left6['state'] = 'disabled'
left7['state'] = 'disabled'
left8['state'] = 'disabled'

right2['state'] = 'disabled'
right3['state'] = 'disabled'
right4['state'] = 'disabled'
right5['state'] = 'disabled'
right6['state'] = 'disabled'
right7['state'] = 'disabled'
right8['state'] = 'disabled'

btnPlayAgain =tkinter.Button(master, text="Play Again", command=restart_program,height=2,width=14)
btnPlayAgain.grid(row=23,column=0, columnspan=2)

btnClose = tkinter.Button(master, text="Close", command = master.destroy,height=2,width=14)
btnClose.grid(row=23,column=4, columnspan=2) 
# so close se zatvara client (i tkinter sekako kako del od klientot)

left1.grid(pady=(10,5))
left2.grid(pady=(5,5))
left3.grid(pady=(5,5))
left4.grid(pady=(5,5))
left5.grid(pady=(5,5))
left6.grid(pady=(5,5))
left7.grid(pady=(5,5))
left8.grid(pady=(5,5))

right1.grid(pady=(10,5))
right2.grid(pady=(5,5))
right3.grid(pady=(5,5))
right4.grid(pady=(5,5))
right5.grid(pady=(5,5))
right6.grid(pady=(5,5))
right7.grid(pady=(5,5))
right8.grid(pady=(5,5))

btnPlayAgain.grid(padx=(20,20),pady=(20,20))
btnClose.grid(padx=(20,20),pady=(20,20))
text_box.grid(padx=(20,20),pady=(20,20))

lefts = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"]
rights = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]

def clickedBtn(btnText):
    if btnText == "R1" or btnText == "L1":
        left2['state'] = 'normal'
        right2['state'] = 'normal'
        left1['state'] = 'disabled'
        right1['state'] = 'disabled'
        
    if btnText == "R2" or btnText == "L2":
        left3['state'] = 'normal'
        right3['state'] = 'normal'
        left2['state'] = 'disabled'
        right2['state'] = 'disabled'
        
    if btnText == "R3" or btnText == "L3":
        left4['state'] = 'normal'
        right4['state'] = 'normal'
        left3['state'] = 'disabled'
        right3['state'] = 'disabled'
        
    if btnText == "R4" or btnText == "L4":
        left5['state'] = 'normal'
        right5['state'] = 'normal'
        left4['state'] = 'disabled'
        right4['state'] = 'disabled'
        
    if btnText == "R5" or btnText == "L5":
        left6['state'] = 'normal'
        right6['state'] = 'normal'
        left5['state'] = 'disabled'
        right5['state'] = 'disabled'
        
    if btnText == "R6" or btnText == "L6":
        left7['state'] = 'normal'
        right7['state'] = 'normal'
        left6['state'] = 'disabled'
        right6['state'] = 'disabled'
        
    if btnText == "R7" or btnText == "L7":
        left8['state'] = 'normal'
        right8['state'] = 'normal'
        left7['state'] = 'disabled'
        right7['state'] = 'disabled'
        
    if btnText == "R8" or btnText == "L8":
        left8['state'] = 'disabled'
        right8['state'] = 'disabled'

    if btnText in lefts:
        print("l")
        pole = "l"
        s.send(pole.encode())

    if btnText in rights:
        print("r")
        pole = "r"
        s.send(pole.encode())
        
    data = s.recv(1024).decode()
    print(data)
    
   
    if btnText == "L1": 
        left1['bg'] = '#B32727'
    if btnText == "L2": 
        left2['bg'] = '#B32727'
    if btnText == "L3": 
        left3['bg'] = '#B32727'
    if btnText == "L4": 
        left4['bg'] = '#B32727'
    if btnText == "L5": 
        left5['bg'] = '#B32727'
    if btnText == "L6": 
        left6['bg'] = '#B32727'
    if btnText == "L7": 
        left7['bg'] = '#B32727'
    if btnText == "L8": 
        left8['bg'] = '#B32727'
    if btnText == "R1": 
        right1['bg'] = '#B32727'
    if btnText == "R2": 
        right2['bg'] = '#B32727'
    if btnText == "R3": 
        right3['bg'] = '#B32727'
    if btnText == "R4": 
        right4['bg'] = '#B32727'
    if btnText == "R5": 
        right5['bg'] = '#B32727'
    if btnText == "R6": 
        right6['bg'] = '#B32727'
    if btnText == "R7": 
        right7['bg'] = '#B32727'
    if btnText == "R8": 
        right8['bg'] = '#B32727'
    
    if data == "No more lives left.": #  or data == "You have successfully reached the end." - nemam potreba od ova, sekako at that point site kje se disabled
        left1['state'] = 'disabled'
        left2['state'] = 'disabled'
        left3['state'] = 'disabled'
        left4['state'] = 'disabled'
        left5['state'] = 'disabled'
        left6['state'] = 'disabled'
        left7['state'] = 'disabled'
        left8['state'] = 'disabled'
        right1['state'] = 'disabled'
        right2['state'] = 'disabled'
        right3['state'] = 'disabled'
        right4['state'] = 'disabled'
        right5['state'] = 'disabled'
        right6['state'] = 'disabled'
        right7['state'] = 'disabled'
        right8['state'] = 'disabled'
        
    text_box.configure(state='normal')
    text_box.delete(1.0, "end-1c") 
    text_box.insert("end-1c", data) 
    text_box.configure(state='disabled')

master.mainloop()