#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
  srand(time(nullptr));
  int n;
  int l = 0;
  cout << "n = ";
  cin >> n;
  int t[n];
  for(int i = 0; i < n; i++)
  {
    t[i] = rand() % 119 - 2 + 1;
  }
  int max = t[0];
  for(int i = 1; i < n; i++)
  {
    if(t[i] > max) max = t[i];
  }
  for(int i = 0; i < n; i++)
  {
    if(t[i] == max) l++;
  }
  cout << "Najwieksza: " << max << endl;
  cout << "Liczba wystapien: " << l << endl;
}
