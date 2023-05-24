#include<iostream>
#include<math.h>
main()
{

    int x1,y1,x2,y2;
    float dx,dy,x_old,x_new,x_inc,y_old,y_new,y_inc,step;
    printf("\nEnter initial point (x1,y1) : ");
    scanf("%d%d",&x1,&y1);

    printf("\nEnter final point (x2,y2) : ");
    scanf("%d%d",&x2,&y2);

    dx=x2-x1;
    dy=y2-y1;

    if(abs(dx)>abs(dy))
    {
         step = abs(dx);
    }
    else
    {
         step = abs(dy);
    }
    
   
    x_old=float(x1),y_old=float(y1);
    x_inc= abs(dx)/step;
    y_inc= abs(dy)/step;
    printf("\n \t\tX_old\tY_old\tX_inc\tY_inc\tX_new\tY_new\tround(X_new)\tround(Y_new)");
    for(int i=1;i<=step;i++)
    {
        x_new=x_old+x_inc;
        y_new=y_old+y_inc;
        printf("\n\t\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t\t%1.1f",x_old,y_old,x_inc,y_inc,x_new,y_new,round(x_new),round(y_new));
        x_old=x_new;
        y_old=y_new;
    }

    return 0;
}