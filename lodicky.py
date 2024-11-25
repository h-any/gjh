import random
import tkinter

wi=600
he=500

canvas=tkinter.Canvas(width=wi, height=he,bg='white')
canvas.pack()

x=[15 for _ in range (15)]
krok=random.randint(1,10)
vyhra=''

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def nakresli_lodicky():
    global vyhra
    canvas.delete('all')
    canvas.create_line(wi-50,0,wi-50,500,fill='red',width=2)
    y=-5
    for i in range (15):
        y+=33
        lodicka(x[i],y) 
        print (x[i])
    premen()
    
def premen():
    global x
    new_x=[]
    for i in range(15):
        posun=random.randint(1,10)
        new_x.append(x[i]+posun)
    x=new_x

def plavaj():
    nakresli_lodicky()
    for i in range (15):
        if x[i]>=550:
            text=('Vyhrala lodicka',i)
            canvas.create_text(300,250,text=text, font=("Arial", 24, "bold"))
            canvas.unbind('<Button-1>')
            return
    
    canvas.after(2,plavaj)

def klik(event):    
    plavaj()

canvas.bind('<Button-1>',klik)

nakresli_lodicky()

canvas.mainloop()