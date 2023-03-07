//metoda dziel i zwyciężaj polega na dzieleniu problemu na mniejsze problemy
//w nich znelezienie rozwiązania i na podstawie częściowych rozwiązań znalezienie rozwiązania głównego problemu.
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void wypisz(int t[], int size)
{
  for(int x = 0; x < size; x++)
  {
    cout << t[x] << ", ";
  }
  cout << endl;
}

int main(int argc, char *argv[])
{
  if(argc < 3)
  {
    cout << "Za malo argumentow" << endl;
    return 0;
  }
  srand(time(NULL));
  int n,d;
  long long int min,max;
  n = atoi(argv[1]);
  min = 0;
  max = 0;
  int t[n];
  for(int x = 0; x < n; x++)
  {
    t[x] = rand() % atoi(argv[2]) + 1;
  }
  wypisz(t, n);
  if(t[0] > t[1])
  {
    min = t[1];
    max = t[0];
  }
  else
  {
    max = t[1];
    min = t[0];
  }
  if(n % 2 == 1) d = n - 2;
  else d = n - 1;
  for(int i = 2; i < d; i++)
  {
    if(t[i] < t[i+1])
    {
      if(t[i] < min) min = t[i];
      if(t[i+1] > max) max = t[i+1];
    }
    else
    {
      if(t[i+1] < min) min = t[i+1];
      if(t[i] > max) max = t[i];
    }
  }
  if(n % 2 == 1)
  {
    if(t[n-1] > max) max = t[n-1];
    if(t[n-1] < min) min = t[n-1];
  }
  cout << min << endl << max << endl;
}
