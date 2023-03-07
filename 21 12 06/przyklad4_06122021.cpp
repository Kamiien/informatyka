#include <iostream>
#include "random.h"
using namespace std;

int szukaj(int t[3][3])
{
  int l = 0;
  for(int x = 0; x < 3; x++)
  {
    for(int y = 0; y < 3; y++)
    {
      if(t[x][y] == 0) l++;
    }
  }
  return l;
}

main()
{
  int t[3][3];
  for(int x = 0; x < 3; x++)
  {
    for(int y = 0; y < 3; y++)
    {
      t[x][y] = randr(0, 4);
    }
  }
  for(int x = 0; x < 3; x++)
  {
    for(int y = 0; y < 3; y++)
    {
      cout << t[x][y] << "\t";
    }
    cout << endl;
  }
  cout << szukaj(t);
}