#include <iostream>
using namespace std;

int l = 0;

int fib(int n)
{
  l++;
  if(n == 1 || n == 2) return 1;
  return fib(n-1) + fib(n-2);
}

main()
{
  int i;
  cin >> i;
  int f[i];
  for(int x = 0; x < i; x++)
  {
    l++;
    if(x == 0 || x == 1) f[x] = 1;
    else f[x] = f[x-1] + f[x-2];
  }
  cout << f[i-1] << " : ";
  cout << l;
}