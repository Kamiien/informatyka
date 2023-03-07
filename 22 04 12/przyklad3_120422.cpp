#include <iostream>
using namespace std;

int main()
{
  string oct;
  cout << "Podaj liczbe osemkowa: ";
  cin >> oct;
  int d = oct.size();
  int a[d];
  for(int i = 0; i < d; i++)
  {
    switch(oct[i])
    {
      case '0': a[i] = 0; break;
      case '1': a[i] = 1; break;
      case '2': a[i] = 2; break;
      case '3': a[i] = 3; break;
      case '4': a[i] = 4; break;
      case '5': a[i] = 5; break;
      case '6': a[i] = 6; break;
      case '7': a[i] = 7; break;
    }
  }
  int w = a[0];
  for(int i = 1; i < d; i++)
  {
    w = w * 8 + a[i];
  }
  cout << "w = " << w << endl;
}
