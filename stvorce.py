import random
import tkinter

wi=400
he=300

canvas=tkinter.Canvas(width=wi, height=he,bg='white')
canvas.pack()

y=140
x=25
farby=()
for i in range (7):
    f=random.choice(('red','blue'))
    farby+=f,
    stvorec=canvas.create_rectangle(x,y,x+50,y+50,fill=f)
    x+=50

def klik(event):
    x1,y1=event.x,event.y
    hranica=25
    hranica1=75
    if x1<hranica1 and x1>hranica and y1>140 and y1<190:
        if f=='red':
            canvas.itemconfig(stvorec,fill='blue')
        else:
            canvas.itemconfig(stvorec,fill='red')
    

canvas.bind('<Button-1>',klik)
