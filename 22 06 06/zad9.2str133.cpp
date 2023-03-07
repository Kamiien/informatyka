#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

bool test(int x, int t[])
{
  for(int i = 0; i < sizeof(t)/sizeof(int); i++)
  {
    if(t[i] == x) return true;
  }
  return false;
}

int main()
{
  srand(time(nullptr));
  int l[6] = {};
  int x = 0;
  while(x < 6)
  {
    int r = rand() % 49 + 1;
    if(!test(r, l))
    {
      l[x] = r;
      x++;
      cout << r << endl;
    }
  }
  return 0;
}
