#Zuzana Orihelová, Oktáva A

import tkinter
import random

X=400
Y=400
pocet=20
posun_x=Y/pocet
sirka=10

canvas=tkinter.Canvas(wi=X, he=Y, bg="white")
canvas.pack()

suradnice=()+pocet*(0,)

def zmena():
    canvas.delete("all")
    uprav()
    for k in range(pocet):
        kvapeľ=canvas.create_line(posun_x*k+sirka, 0, posun_x*k+sirka, suradnice[k], width=sirka, fill="light blue")   
    canvas.after(200, zmena)

def uprav():
    global suradnice
    posun=()
    for a in range(pocet):
        nahodne_predlzenie=random.randint(0, 10)
        if suradnice[a]>=100:
            sanca=random.randint(0, 100)
            if sanca>=0 and sanca<=25:
                p=random.randint(30, 50)
            else:
                p=nahodne_predlzenie
        else:
            p=suradnice[a]+nahodne_predlzenie
        posun+=(p,)
    suradnice=posun


zmena()



tkinter.mainloop()
