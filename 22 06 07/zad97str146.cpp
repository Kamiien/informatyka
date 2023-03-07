#include <iostream>
using namespace std;

int main()
{
  int n;
  cout << "n = ";
  cin >> n;
  int t[n];
  bool mono[5] = { 1,1,1,1,1 };
  for(int i = 0; i < n; i++)
  {
    cout << "t[" << i << "] = ";
    cin >> t[i];
    if(i > 0 && t[i] <= t[i-1])
    {
      mono[0] = false;
    }
    if(i > 0 && t[i] >= t[i-1])
    {
      mono[1] = false;
    }
    if(i > 0 && t[i] > t[i-1])
    {
      mono[2] = false;
    }
    if(i > 0 && t[i] < t[i-1])
    {
      mono[3] = false;
    }
  }
  for(int i = 0; i < 10; i++)
  {
    if(i > 0 && t[i] == t[i-1] || mono[0] || mono[1])
    {
      mono[4] = false;
    }
  }
  if(mono[0]) cout << "Rosnaca ";
  if(mono[1]) cout << "Malejaca ";
  if(mono[2]) cout << "Nierosnaca ";
  if(mono[3]) cout << "Niemalejaca ";
  if(mono[4]) cout << "Niemonotoniczna ";
  return 0;
}