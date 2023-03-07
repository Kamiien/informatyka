#include <iostream>
using namespace std;
// dane: liczby całkowite w tablicy t - 10 elementów
// wunik: czy tablica zawiera liczbę 2 i na jakiej pozycji


int szukaj(int t[], int n)
{
  for(int i = 0; i < n; i++)
  {
    if(t[i] == 2) return i;
  }
  return -1;
}

int main()
{
  int t[10] = {3,4,6,5,9,3,4,7,3,2};
  int p = szukaj(t,10);
  if(p == -1) cout << "brak 2" << endl;
  else cout << "jest na pozycji: " << p << endl;
}
