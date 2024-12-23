import random
import tkinter

wi=500
he=300

canvas=tkinter.Canvas(width=wi, height=he,bg='white')
canvas.pack()

y=140
x=25
farby=[]
stvorce=[]
pocet_s=9
pocet_k=0

for i in range (pocet_s):
    f=random.choice(('green','yellow'))
    farby.append(f)
    s=canvas.create_rectangle(x,y,x+50,y+50,fill=f)
    stvorce.append(s)
    x+=50
    
def zmena(color):
    return 'yellow' if color == 'green' else 'green'

def klik(event):
    global pocet_k
    x1,y1=event.x,event.y

    for i in range (pocet_s):
        if (x1>25+i*50) and (x1<75 + i*50):
            if i > 0:
                farby[i - 1] = zmena(farby[i - 1])
                farby[i]=zmena(farby)
                canvas.itemconfig(stvorce[i], fill=farby[i])
                canvas.itemconfig(stvorce[i - 1], fill=farby[i - 1])
            if i < pocet_s - 1:
                farby[i + 1] = zmena(farby[i + 1])
                farby[i]=zmena(farby)
                canvas.itemconfig(stvorce[i], fill=farby[i])
                canvas.itemconfig(stvorce[i + 1], fill=farby[i + 1])

    if event.num==1:
        pocet_k+=1
    canvas.create_rectangle(20,20,30,30, fill='white', outline="")
    canvas.create_text(25,25,text=pocet_k,)

    if all(color == 'green' for color in farby) or all(color == 'yellow' for color in farby) :
        canvas.create_text(250, 210, text='KONIEC', font=('Arial', 20, 'bold'))
        canvas.unbind('<Button-1>')
    
canvas.bind('<Button-1>',klik)
canvas.mainloop()