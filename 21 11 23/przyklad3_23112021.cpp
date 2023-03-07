#include <iostream>
using namespace std;
//wyznaczenie maksymalnej wartości w tablicy dwuwymiarowej 5x5

main()
{
  int min,max;
  int t[5][5];
  for(int x = 0; x < 5; x++)
  {
    for(int y = 0; y < 5; y++)
    {
      cout << "t[" << x << "][" << y << "] = ";
      cin >> t[x][y]; 
    }
  }
  min = t[0][0];
  max = t[0][0];
  for(int x = 0; x < 5; x++)
  {
    for(int y = 2; y < 5; y++)
    {
      if(t[x][y] > max) max = t[x][y];
      if(t[x][y] < min) min = t[x][y];
    }
  }
  cout << min << endl << max << endl;
}
