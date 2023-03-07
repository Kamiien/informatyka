#include <iostream>
using namespace std;

int main()
{
  int n;
  cout << "Podaj stopien wielomianu: ";
  cin >> n;
  double a[n+1];
  cout << "Podaj wspolczynniki" << endl;
  for(int i = 0; i <= n; i++)
  {
    cout << "a[" << i << "] = ";
    cin >> a[i];
  }
  double x;
  cout << "Podaj x: ";
  cin >> x;
  double w = a[0];
  for(int i = 0; i <= n; i++)
  {
    w = w * x + a[i];
  }
  cout << w;
  return 0;
}
