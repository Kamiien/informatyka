#include <iostream>
using namespace std;

int main()
{
  int n;
  cout << "n = ";
  cin >> n;
  int t[n];
  bool f = true;
  for(int i = 0; i < n; i++)
  {
    cout << "t[" << i << "] = ";
    cin >> t[i];
    if(i > 0 && t[i] >= t[i-1])
    {
      f = false;
    }
  }
  if(f) cout << "tak";
  else cout << "nie";
  return 0;
}
