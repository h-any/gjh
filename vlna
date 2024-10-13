import tkinter
import random
wi=300
step=15
canvas=tkinter.Canvas(width=wi,height=300,bg='white')
canvas.pack()

# nakresli ciaru podla poslaneho pola s y
def line(y_list):
    canvas.delete('all')
    x=0
    for i in range (len(y_list)-1):
        canvas.create_line(x,y_list[i],x+step,y_list[i+1],width=4,fill='blue')
        x+=step
    

# posunie hodnotz v y:liste o poziciu vedla
def shift_list(y_list):
    for i in range (len(y_list)-1,0,-1):
        y_list[i]=y_list[i-1]
    return y_list

#vygeneruje pole y
def generate_list():
    new_list=[]
    for i in range(int(wi/step)):
        new_list.append(generate_y())
    return new_list

#vygeneruj nahodny y
def generate_y():
    return random.randint(140,160)

#oosunie hodnoty vygneruje novvy prvok, vykresli ciaru
def shift_line(y_list):
    y_list=shift_list(y_list)
    y_list[0]=generate_y()
    line(y_list)
    canvas.after(500,lambda:shift_line(y_list))

y_list=generate_list()
line(y_list)

canvas.after(500,lambda:shift_line(y_list))

canvas.mainloop()
