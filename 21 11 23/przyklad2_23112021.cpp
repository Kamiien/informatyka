#include <iostream>
using namespace std;
//jednoczesne szukanie minimalnego i maksymalnego elementu w zbiorze

main()
{
  int i,min,max;
  cout << "rozmiar tablicy: ";
  cin >> i;
  int t[i];
  for(int x = 0; x < i; x++)
  {
    cout << "t[" << x << "]= ";
    cin >> t[x]; 
  }
  if(t[0] > t[1])
  {
    min = t[1];
    max = t[0];
  }
  else
  {
    max = t[1];
    min = t[0];
  }
  for(int x = 2; x < i; x++)
  {
    if(t[x] > max) max = t[x];
    if(t[x] < min) min = t[x];
  }
  cout << min << endl << max << endl;
}