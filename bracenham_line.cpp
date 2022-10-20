#include<stdio.h>
#include<graphics.h>
#include<math.h>
//Function for finding absolute value
int abs (int n)
{
	return ( (n>0) ? n : ( n * (-1)));
}

void BCN(int X0,int Y0, int X1, int Y1) {
	
	// calculate dx & dy
	int dx = X1 - X0;
	int dy = Y1 - Y0;
	
	int dec = 2*dy - dx;
	
	int x = X0;
	int y = Y0;

	putpixel(x, y, WHITE);
	
	while (x <= X1) {
		if(dec >= 0) {
			y = y+1;
			dec = dec + 2*(dy - dx);
		} else {
			dec = dec + 2*dy;
		}
		putpixel(x, y, WHITE);
		x = x+1;
		delay(10);
	}
}

int main() {
	
	int gd = DETECT, gm;
	// Initialize graphics function
	initgraph (&gd, &gm, "c:\\tc\bgi");

	int X0 = 100, Y0 = 100, X1 = 200, Y1 = 200;
	BCN(X0, Y0, X1, Y1);
	getch();
	return 0;
}
