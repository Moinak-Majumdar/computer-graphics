# import matplotlib.pyplot as plt
# def drawDDA(x1,y1,x2,y2):
#     x,y = float(x1),float(y1)
#     length = int(abs((x2-x1) if abs(x2-x1) > abs(y2-y1) else (y2-y1)))
#     dx = float((x2-x1)/float(length))
#     dy = float((y2-y1)/float(length))
#     print ("x = ",round(x),"y = ",round(y))
#     x_values=[round(x)]
#     y_values=[round(y)]
#     for i in range(length):
#         x += dx
#         y += dy
#         print("x = ",x, "y = ",y)
#         x_values.append(x)
#         y_values.append(y)
#     plt.plot(x_values, y_values,marker='o', color='b')
#     plt.grid()
#     plt.show()
#
# drawDDA(2,3,12,8)

import matplotlib.pyplot as plt
def ROUND(a):
    return abs(a)

def drawDDA(x1,y1,x2,y2):
    x,y = x1,y1
    length = abs((x2-x1) if abs(x2-x1) > abs(y2-y1) else (y2-y1))
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    print("x = ", ROUND(x), "y = ", ROUND(y))
    x_values = [ROUND(x)]
    y_values=[ROUND(y)]
    for i in range(length):
        x += dx
        y += dy
        print("x = ", ROUND(x), "y = ", ROUND(y))
        x_values.append(ROUND(x))
        y_values.append(ROUND(y))
    plt.plot(x_values, y_values, marker='o', color='b')
    plt.grid()
    plt.show()

drawDDA(100,100,300,350)