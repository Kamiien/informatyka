#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

double max(double t[], int n)
{
  double max = t[0];
  for(int i = 1; i < n; i++) if(t[i] > max) max = t[i];
  return max;
}

main()
{
  srand(time(NULL));
  double t[7] = {1.0,1.1,1.2,1.5,2.2,2.4,2.7};
  cout << max(t, 7);
  double r[100];
  for(int i = 0; i < 100; i++)
  {
    r[100] = rand() % 101;
  }
}
