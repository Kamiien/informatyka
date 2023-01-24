#include <iostream>
using namespace std;

int main()
{
  int trawa;
  int dzien;
  for(int b = 50; b < 100; b++)
  {
    trawa = 20000 * 0.9;
    int dzien = 1;
    for(int i = 0; i < 365; i++)
    {
      if(dzien % 7 != 0) trawa -= b * 2;
      trawa += 90;
      dzien++;
    }
    cout << "Bizon: " << b << endl;
    cout << "Trawa: " << trawa << endl;
  }
}