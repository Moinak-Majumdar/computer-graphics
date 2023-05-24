from tkinter import *
win=Tk()
win.geometry("450x450")
canvas=Canvas(win, width=450, height=450)
canvas.pack()

INSIDE = 0 # 0000
LEFT = 1 # 0001
RIGHT = 2 # 0010
BOTTOM = 4 # 0100
TOP = 8 # 1000

xMax = 350.0
yMax = 350.0
xMin = 50.0
yMin = 50.0
canvas.create_rectangle(xMin,yMin, xMax, yMax, outline='#000000')


def regionCode(x, y):
	code = INSIDE
	if x < xMin: # to the left of rectangle
		code |= LEFT
	elif x > xMax: # to the right of rectangle
		code |= RIGHT
	if y < yMin: # below the rectangle
		code |= BOTTOM
	elif y > yMax: # above the rectangle
		code |= TOP
	return code

def cohenSutherland(x1, y1, x2, y2):

	xi=x1
	yi=y1
	code1 = regionCode(x1, y1)
	code2 = regionCode(x2, y2)
	accept = False

	while True:

		# If both endpoints lie within rectangle
		if code1 == 0 and code2 == 0:
			accept = True
			break

		# If both endpoints are outside rectangle
		elif (code1 & code2) != 0:
			break
		# partially inside / outside
		else:

			x = 1.0
			y = 1.0
			if code1 != 0:
				code_out = code1
			else:
				code_out = code2
				
			if code_out & TOP:
				
				x = x1 + (x2 - x1) * (yMax - y1) / (y2 - y1)
				y = yMax
			elif code_out & BOTTOM:
				
				x = x1 + (x2 - x1) * (yMin - y1) / (y2 - y1)
				y = yMin
			elif code_out & RIGHT:
				
				y = y1 + (y2 - y1) * (xMax - x1) / (x2 - x1)
				x = xMax
			elif code_out & LEFT:
				
				y = y1 + (y2 - y1) * (xMin - x1) / (x2 - x1)
				x = xMin

		
			if code_out == code1:
				x1 = x
				y1 = y
				code1 = regionCode(x1, y1)
			else:
				x2 = x
				y2 = y
				code2 = regionCode(x2, y2)

	if accept:
		win.title('Line Accepted')
		# clipped portion
		canvas.create_line(x1,y1,x2,y2, fill="green", width=2)
		# outside window
		canvas.create_line(xi,yi,x1,y1, fill='red', width=2)

	else:
		win.title("Line rejected")

cohenSutherland(25, 295, 200, 180)

win.mainloop()