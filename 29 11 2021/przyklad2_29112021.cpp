/*
do tablicy 10 elementowej wylosować liczby z zakresy 0-40
- wypisz je
- policz ile jest liczb parzystych
- jaka jest maksymalna wartość
*/
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

main()
{
  srand(time(NULL));
  int l,max;
  int t[10];
  for(int x = 0; x < 10; x++) t[x] = rand() % 41;
  for(int x = 0; x < 10; x++) cout << t[x] << ", ";
  cout << endl;
  for(int x = 0; x < 10; x++) if(x % 2 == 0) l++;
  if(t[0] > t[1]) max = t[0];
  else max = t[1];
  for(int x = 2; x < 10; x++) if(t[x] > max) max = t[x];
  cout << max << endl;
}