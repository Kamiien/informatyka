#include <iostream>
using namespace std;

int main()
{
  string hex;
  cout << "Podaj liczbe w systemie szesnastkowym: ";
  cin >> hex;
  int d = hex.size();
  int a[d];
  for(int i = 0; i < d; i++)
  {
    switch(hex[i])
    {
      case '0': a[i] = 0; break;
      case '1': a[i] = 1; break;
      case '2': a[i] = 2; break;
      case '3': a[i] = 3; break;
      case '4': a[i] = 4; break;
      case '5': a[i] = 5; break;      
      case '6': a[i] = 6; break;
      case '7': a[i] = 7; break;
      case '8': a[i] = 8; break;
      case '9': a[i] = 9; break;
      case 'A': a[i] = 10; break;
      case 'B': a[i] = 11; break;
      case 'C': a[i] = 12; break;
      case 'D': a[i] = 13; break;
      case 'E': a[i] = 14; break;
      case 'F': a[i] = 15; break;
    }
  }
  int w = a[0];
  for(int i = 1; i < d; i++)
  {
    w = w * 16 + a[i];
  }
  cout << w;
}
