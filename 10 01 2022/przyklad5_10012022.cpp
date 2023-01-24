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

int nww(int a, int b)
{
  return a * b / nwd(a,b);
}

main()
{
  int a,b;
  cout << "a = ";
  cin >> a;
  cout << "b = ";
  cin >> b;
  cout << "nwd(a,b) = " << nwd(a,b) << endl;
  cout << "nww(a,b) = " << nww(a,b);
}