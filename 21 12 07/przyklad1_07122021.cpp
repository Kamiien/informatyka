#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main(int argc, char *argv[])
{
  if(argc <= 1)
  {
    cout << "pierwszy argument: wiersze\ndrugi argument: kolumny\ntrzeci argument: maksymalna liczba";
    return 1;
  }
  srand(time(NULL));
  int p,q,min,max,maxrand;
  p = atoi(argv[1]);
  q = atoi(argv[2]);
  maxrand = atoi(argv[3]);

  int t[p][q];
  for(int x=0; x < p; x++) //losowanie zmiennych do tablicy
    for(int y=0; y < q; y++)
      t[x][y] = rand() % maxrand + 1;

  for(int x=0; x < p; x++)
  {
    for(int y=0; y < q; y++)
      cout << t[x][y] << "\t";
    cout << endl;
  }

  cout << endl;

  max = t[0][0]; //największa wartość
  for(int x=0; x < p; x++)
    for(int y=0; y < q; y++)
      if(t[x][y] > max) max = t[x][y];
  cout << "max = " << max << endl;

  cout << endl;

  for(int x=0; x < p; x++) // największa wartość w każdym wierszu
  {
    max = t[x][0];
    for(int y=0; y < q; y++)
      if(t[x][y] > max) max = t[x][y];
    cout << "max w wierszu " << x+1 << " = " << max << endl;
  }

  cout << endl;

  for(int y=0; y < q; y++) // największa wartość w każdej kolumnie
  {
    max = t[0][y];
    for(int x=0; x < p; x++)
      if(t[x][y] > max) max = t[x][y];
    cout << "max w kolumnie " << y+1 << " = " << max << endl;
  }

  cout << endl;
}
