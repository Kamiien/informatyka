#include <iostream>
using namespace std;

int main()
{
  int t[10] = {4,6,2,15,3,5,12,6,7,9};
  int l = 0;

  for(int i = 0; i < 10; i++)
  {
    for(int j = i+1; j < 10; i++)
    {
      if(t[i] <= t[j] && t[j] % t[i] == 0)
      {
        cout << t[i] << " " << t[j] << endl;
        l++;
      }
    }
  }
}
