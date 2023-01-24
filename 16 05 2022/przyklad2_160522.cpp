#include <iostream>
using namespace std;
//Wyznaczanie wartości wielomianu w(x) w punkcie metodą Hornera
//w(x) = -x^4 + 2x^3 - 3x^2 + 2x + 1

int main()
{
  int a[5] = {-1,2,-3,2,1};
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
