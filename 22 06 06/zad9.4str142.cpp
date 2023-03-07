#include <iostream>
using namespace std;

int main()
{
  int n, x, max;
  int i = 0;
  while(x != 0)
  {
    cout << "x = ";
    cin >> x;
    if(i == 0 || x > max)
    {
      max = x;
      cout << "Nowy max: " << max << endl;
    }
    i++;
  }
  return 0;
}
