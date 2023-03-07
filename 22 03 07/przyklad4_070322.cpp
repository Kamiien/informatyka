#include <iostream>
using namespace std;

void rozklad(int n)
{
  int dzielnik = 2;
  while(dzielnik <= n)
  {
    while(n % dzielnik == 0)
    {
      cout << dzielnik << " * ";
      n /= dzielnik;
    }
    dzielnik += 1;
  }
}

main()
{
  int n;
  cout << "n = ";
  cin >> n;
  rozklad(n);
}
