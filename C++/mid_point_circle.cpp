#include <graphics.h>  
#include <math.h>  
#include <stdio.h>  

void circle_point (int x, int y) {
	//defining a constant to translate points by somw pixels
	const int cons=200;
   	putpixel(cons+x,cons+y,WHITE);
    putpixel(cons+y,cons+x,WHITE);
    putpixel(cons+y,cons-x,WHITE);
    putpixel(cons+x,cons-y,WHITE);
    putpixel(cons-x,cons-y,WHITE);
    putpixel(cons-y,cons-x,WHITE);
    putpixel(cons-y,cons+x,WHITE);
    putpixel(cons-x,cons+y,WHITE);
}
   
void cal (int r)  
{  
    int gdriver = DETECT,gmode;  
    initgraph(&gdriver, &gmode, "c:\\tc\bgi");  
   
    float x=0,p;  
    float y=r;  
	circle_point(x,y);
    p=1-r;  
    while (x!=y)  
    {  
    	x++;
        if (p>=0)  {
        	y = y-1;
        	p= p + 2*(x-y) + 5;
		}  
        else  
        {  
            p = p + 2*x + 3;
        }  
       circle_point(x,y);
       delay(10);
    }  
}  
int main ()  {  
	cal(100.5);  
   	getch();
}  
