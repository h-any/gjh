import random
import tkinter

wi=400
he=300

canvas=tkinter.Canvas(width=wi, height=he,bg='white')
canvas.pack()

pocet=10
sirka=20
x = 10
list_hodnot=()
minimum=250
maximum=0
y=250

for i in range(pocet):
    hodnota = random.randint(20,200)
    list_hodnot+=hodnota,
    
    if hodnota>maximum:
        maximum=hodnota
        
    if hodnota<minimum:
        minimum=hodnota


for l in range(pocet):
    if list_hodnot[l]==maximum:
        farba='orange'
    elif list_hodnot[l]==minimum:
        farba='green'
    else:
        farba='cyan'
    canvas.create_rectangle(x, y, x+sirka,y-list_hodnot[l], fill=farba)
    canvas.create_text(x+10,y-list_hodnot[l]/2,text=list_hodnot[l])
    x+=sirka*2

canvas.mainloop()