import tkinter as tk
win=tk.Tk()
win.geometry("450x450")
canvas=tk.Canvas(win, width=450, height=450)
canvas.pack()
canvas.create_rectangle(50,50,400,400,outline='black')
x1=100
y1=100
x2=300
y2=350

dx = abs(x1-x2)
dy = abs(y1-y2)

a=dy
b=dx
d = a + b/2
x=x1
y=y1

canvas.create_line(x,y,x+1,y+1,fill="red")

for _ in range(1, dx) :
    x = x+1
    if(d<=0) :
        d += a
    else :
        y +=1
        d = d+a+b
    canvas.create_line(x,y,x+1,y+1,fill="red")

win.title("Mid point line")
win.mainloop()