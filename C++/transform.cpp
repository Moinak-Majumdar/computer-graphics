#include <graphics.h>
#include <iostream>
#include <math.h>
#define PI 3.14

using namespace std;

float result[3][3];
float temp[3][3];

void draw (float tri[2][3]) {
	int gdriver = DETECT,gmode;  
    initgraph(&gdriver, &gmode, "c:\\tc\bgi");
    
	line(tri[0][0],tri[1][0], tri[0][1],tri[1][1]);
	line(tri[0][0],tri[1][0], tri[0][2],tri[1][2]);
	line(tri[0][1],tri[1][1], tri[0][2],tri[1][2]);
}

void multiplyMatrix(float a[3][3], float b[3][3])
{
	for(int i=0;i<3;i++)    
	{    
		for(int j=0;j<3;j++)    
		{    
			result[i][j]=0;    
			for(int k=0;k<3;k++)    
			{    
				result[i][j]+=a[i][k]*b[k][j];    
			}    
		}    
	}    
}

void store(float m[3][3])
{
	for(int i=0; i<3; i++)
	{
		for(int j=0; j<3; j++)
		{
			temp[i][j] = m[i][j];
		}
	}
}	

int main() {
	float initialTriangel[][3] = {{100.0,500.0,300.0}, {100.0,100.0,300.0}, {1.0,1.0,1.0}};
	draw(initialTriangel);
	float translateX, translateY;
	float theta;
	float scaleX, scaleY;

	cout<<endl<<"Enter translation parameters (X,Y) :";
	cin>>translateX>>translateY;
	cout<<endl<<"Enter degree of anti clock wise rotation (theta) :";
	cin>>theta;
	cout<<endl<<"Enter scaleing parameters (sX,sY) :";
	cin>>scaleX>>scaleY;
	
	float t1[][3] = {{1,0,translateX}, {0,1,translateY}, {0,0,1}};
	float radian = theta * (PI/180);
	float sinValue = sin(radian);
   	float cosValue = cos(radian);
	float t2[][3] = {{cosValue, -sinValue, 0}, {sinValue, cosValue, 0}, {0,0,1}};
	float t3[][3] = {{scaleX,0,0}, {0,scaleY,0}, {0,0,1}};
	
	multiplyMatrix(t3,t2);
	store(result);

	multiplyMatrix(temp,t1);
	store(result);

	multiplyMatrix(temp, initialTriangel);
	store(result);

	draw(temp);
	
	getch();
	
}
