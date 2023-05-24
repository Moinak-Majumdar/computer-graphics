import matplotlib.pyplot as plt
def drawBres(x1,y1,x2,y2):
    x, y = x1, y1
    x_values = [x]
    y_values = [y]
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = (2*dy) - dx
    while (x<=x2):
        print("x = ",x, "y = ",y)
        x_values.append(x)
        y_values.append(y)
        if(p<0):
            p = p + (2*dy)
            x+=1
            y=y
        else:
            p = p + ((2*dy) - (2*dx))
            x+=1
            y+=1
    plt.plot(x_values, y_values, marker='o', color='b')
    plt.grid()
    plt.show()

drawBres(3,2,15,5)
