#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
  int n = 15;
  bool f = false;
  double t[n];
  for(int i = 0; i < n; i++)
  {
    cout << "t[" << i << "] = ";
    cin >> t[i];
    if(t[i] <= 11) f = true; 
  }
  if(f) cout << "Prawda";
  else  cout << "Fałsz";
}
