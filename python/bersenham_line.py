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

roh = 2*dy - dx

x=0
y=0
end=0
if(x1 > x2) :
    x=x2
    y=y2
    end = x1
else :
    x=x1
    y=y1
    end = x2


canvas.create_line(x,y,x+1,y+1, fill="red")

while(x < end) :
    x=x+1
    if(roh >= 0) :
        y=y+1
        roh += 2*dy - 2*dx
    else :
        roh += 2*dy

    canvas.create_line(x,y,x+1,y+1, fill="red")


win.title('Bresenham Line drawing ')
win.mainloop()