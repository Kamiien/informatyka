#include <iostream>
using namespace std;

int main()
{
  int t[10];
  bool rosnaca = true;
  for(int i = 0; i < 10; i++)
  {
    cout << "t[" << i << "] = ";
    cin >> t[i];
    if(i > 0 && t[i] <= t[i-1])
    {
      rosnaca = false;
    }
  }
  if(rosnaca) cout << "tak";
  else cout << "nie";
  return 0;
}
