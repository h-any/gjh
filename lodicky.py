import random
import tkinter

wi=600
he=500

canvas=tkinter.Canvas(width=wi, height=he,bg='white')
canvas.pack()

y=-5
x=()+15*(0,)
krok=random.randint(1,10)

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def nakresli_lodicky():
    global y
    canvas.delete('all')
    canvas.create_line(wi-50,0,wi-50,500,fill='red',width=2)
    premen()
    for i in range (15):
        y+=33
        lodicka(x,y) 
    
def premen():
    global x
    list_x=()
    for i in range(15):
        posun=random.randint(1,10)
        rast=x[i]+posun
        list_x+=(rast,)
    x=list_x[i]
    
    canvas.after(200,nakresli_lodicky)

def klik(event):
    nakresli_lodicky()

canvas.bind('<Button-1>',klik)
