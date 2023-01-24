#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
// str 132 tabelka
int main()
{
  srand(time(NULL));
  int t[9];
  int l = 0;
  for(int i = 0; i < 9; i++)
  {
    t[i] = rand() % 28 + 4 + 1;
    cout << t[i] << endl;
    if(t[i] >= 9) l++;
  }
  if(l == 9) cout << "Wszystkie liczby sa nie mniejsze niz 9" << endl;
  return 0;
}
