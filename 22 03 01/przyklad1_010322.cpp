#include <iostream>
#include <cmath>
using namespace std;

void sito(int t[], int n)
{
  for(int i = 2; i <= n; i++) t[i] = 1;
  int i = 2;
  int m;
  while(i <= n)
  {
    m=2*i;
    while(m<=n)
    {
      t[m]=0;
      m += i;
    }
    i++;
  }
}

main()
{
  int n;
  cout << "n:";
  cin >> n;
  int t[n+1];
  sito(t, n);
  int p,q;
  int l = 0;
  for(int i = n; i > 2; i--)
  {
    if(l == 2) break;
    if(t[i] == 1 && l == 1)
    {
      q = i;
      l++;
    }
    if(t[i] == 1 && l == 0)
    {
      p = i;
      l++;
    }
  }
  cout << endl << p << " " << q;
}