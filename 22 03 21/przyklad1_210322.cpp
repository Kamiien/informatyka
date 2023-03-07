#include <iostream>
using namespace std;

main()
{
  int n;
  cout << "n = ";
  cin >> n;
  int t[15] = {0};
  int i = 0;
  while(n>0)
  {
    t[i] = n%2;
    i++;
    n = n/2;
  }
  for(int j = 15; j >= 0; j--)
  {
    cout << t[j];
  }
}
