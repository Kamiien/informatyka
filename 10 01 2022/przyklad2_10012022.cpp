#include <iostream>
using namespace std;

int nwd(int a, int b)
{
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
  cout << a << " / " << b << "  /  " << c << " / " << d << " = ";
  int l = a * d;
  int m = b * c;
  cout << l / nwd(l,m) << " / " << m/ nwd(l,m);
}