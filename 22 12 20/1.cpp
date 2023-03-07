#include <iostream>
using namespace std;

int main()
{
  int bizony = 50;
  int trawa = 20000 * 0.9;
  int dzien = 1;
  while(true)
  {
    trawa -= bizony * 2;
    trawa += 90;
    if(trawa <= 0) break;
    dzien++;
  }
  cout << "Dzien: " << dzien << endl;
}