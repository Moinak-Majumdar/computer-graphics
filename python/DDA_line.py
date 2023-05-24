import tkinter as tk
win=tk.Tk()
win.geometry("450x450")
canvas=tk.Canvas(win, width=450, height=450)
canvas.pack()

x1=100
y1=100
x2=300
y2=350

dx = abs(x2-x1)
dy = abs(y2-y1)
steps = dx if dx>dy else dy

x=x1
y=y1

canvas.create_line(x,y,x+1,y+1,fill="red")

xInc = dx/steps
yInc = dy/steps

for i in range(1, steps) :
    x = x+xInc
    y = y+yInc
    canvas.create_line(x,y,x+1,y+1,fill="red")

canvas.create_rectangle(50,50,400,400, outline='black')
win.title("DDA_line")
win.mainloop()