#include <iostream>
using namespace std;

main()
{
  int j;
  for(int i = 1,j = 10; i <= 10; i++)
  {
    cout << i << " ";
    if(i % 2 == 0)
    {
      i++;
    }
  }
  cout << endl << j;
}