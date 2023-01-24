#include <iostream>
#include <cmath>
using namespace std;

int lustrzana(int n)
{
  int nowa = 0;
  while(n > 0)
  {
    nowa = 10 * nowa + n % 10;
    n = n/10;
  }
  return nowa;
}

bool test(int n)
{
  for(int i = 2; i <= sqrt(n); i++)
    if(n % i == 0) return false;
    else return true;
}

main()
{
  int n;
  cout << "n = ";
  cin >> n;
  int x = lustrzana(n);
  cout << x << endl;
  if(test(n) == true && test(x) == true) cout << "Liczba i liczba do niej lustrzana sa pierwsze";
  else cout << "Liczba i liczba do niej lustrzana nie sa pierwsze";
}
