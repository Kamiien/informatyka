#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
  srand(time(nullptr));
  int n = 11;
  bool f = true;
  int t[n];
  for(int i = 0; i < n; i++)
  {
    t[i] = rand() % 33 + 1;
    cout << "t[" << i << "] = " << t[i] << endl;
    if(t[i] % 4 == 0) f = false; 
  }
  if(f) cout << "Prawda";
  else  cout << "Falsz";
}
