#include <iostream>

using namespace std;

float angle_calc(int h,int m,float angle);

int main()
{
    int minute;
    int hour;
    int n;
    float angle;
    while(cin>>hour&&cin>>minute)
    {
        if(hour<0||minute<0)
        {
            break;
        }
        angle = angle_calc(hour,minute,0);
        cout<<angle<<endl;
    }
    return 0;
}

float angle_calc(int h,int m,float angle)
{
    angle = 30*h + m/60.0*30 - 6*m;
    if(angle>180)
    {
        angle = 360-angle;
    }
    if(angle<0)
    {
        angle = -angle;
    }
    return angle;
}
