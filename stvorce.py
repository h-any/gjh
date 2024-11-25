import random
import tkinter

wi=400
he=300

canvas=tkinter.Canvas(width=wi, height=he,bg='white')
canvas.pack()

y=140
x=25
farby=[]
stvorce=[]
pocet_s=7

for i in range (pocet_s):
    f=random.choice(('red','blue'))
    farby.append(f)
    s=canvas.create_rectangle(x,y,x+50,y+50,fill=f)
    stvorce.append(s)
    x+=50
    
def zmena(index):
    if farby[index]=='red':
        return 'blue'
    else:
        return 'red'

def klik(event):
    global l,koniec, koniec_b
    x1,y1=event.x,event.y

    for i in range (pocet_s):
        if (x1>25+i*50) and (x1<75 + i*50):

            farby[i]=zmena(i)
            canvas.itemconfig(stvorce[i],fill=farby[i])

    if all(color == 'red' for color in farby):
        canvas.create_text(200, 210, text='RED', font=('Arial', 15, 'bold'))
        canvas.unbind('<Button-1>')

    elif all(color == 'blue' for color in farby):
        canvas.create_text(200, 210, text='BLUE', font=('Arial', 15, 'bold'))
        canvas.unbind('<Button-1>')

canvas.bind('<Button-1>',klik)
canvas.mainloop()