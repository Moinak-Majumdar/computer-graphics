#include<iostream>
#include<conio.h>
#include<graphics.h>
#include<math.h>
main()
{
    int x1,y1,x2,y2,dx,dy;
    float a,b,d,x,y;
    // int gd = DETECT, gm, color;

    printf("\nEnter initial point (x1,y1) : ");
    scanf("%d%d",&x1,&y1);

    printf("\nEnter final point (x2,y2) : ");
    scanf("%d%d",&x2,&y2);

    dx=abs(x1-x2);
    dy=abs(y1-y2);

    a=dy;
    b=-dx;
    d=a+(b/2);

    x=x1;
    y=y1;

    float x_old=x1,y_old=y1,d_old=d;
    printf("\n\t\tX_old\tY_old\tD_old\tX_new\tY_new\tD_new");
    printf("\n\t\t---------------------------------------------");
    for(int i=1;i<=dx;i++)
    {
        x++;
        if(d<=0)
        {
            d=d+a;
            printf("\n\t\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f",x_old,y_old,d_old,x,y,d);
        }
        else
        {
            y++;
            d=d+a+b;
            printf("\n\t\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f",x_old,y_old,d_old,x,y,d);
        }
        x_old=x;
        y_old=y; 
        d_old=d;
        printf("\n\t\t---------------------------------------------");    
    }
}