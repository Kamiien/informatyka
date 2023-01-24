//dane: liczba ca³kowita dodatnia n
//wynik: liczba jest x cyfrowa
#include <iostream>
using namespace std;

int policz(int n)
{
  int x = 1;
  int i = 10;
  while(n >= i)
  {
    i *= 10;
    x++;
  }
  return x;
}

main()
{
  int n;
  cout << "n = ";
  cin >> n;
  int x = policz(n);
  cout << "Liczba ma " << x << " cyfr";
}
