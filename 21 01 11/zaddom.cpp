#include <iostream>
#include <cmath>
using namespace std;

int nwd(int a, int b)
{
  a = abs(a);
  b = abs(b);
  while(a!=b)
  {
    if(a > b) a -= b;
    else b -= a;
  }
  return a;
}

main()
{
  int a,b,c,d;
  cout << "a = ";
  cin >> a;
  cout << "b = ";
  cin >> b;
  cout << "c = ";
  cin >> c;
  cout << "d = ";
  cin >> d;
  cout << a << " / " << b << "  +  " << c << " / " << d << " = ";
  int l = d*a+b*c;
  int m = b * d;
  cout << l / m;
  if(l / nwd(l,m) - l / m * m / nwd(l,m) > 0)
  {
    cout << " " << l / nwd(l,m) - l / m * m / nwd(l,m)<< " / " << m / nwd(l,m) << endl;
  }
}