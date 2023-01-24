#include <iostream>
using namespace std;
//Wyznaczanie wartości wielomianu w(x) w punkcie metodą Hornera
//w(x) = 3x^3 + 2x^2 - 3x + 5
//w(x) = a0x^3 + a1x^2 + a2x + a3



int main()
{
  int a[4] = {3,2,-3,5};
  int x;
  cout << "x = ";
  cin >> x;
  int wynik = a[0];
  for(int i = 1; i <= 3; i++)
  {
    wynik = wynik * x + a[i];
  }
  cout << wynik << endl;
}
