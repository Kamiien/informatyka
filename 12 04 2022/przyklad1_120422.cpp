#include <iostream>
using namespace std;
/*
 * Konwertowanie liczby z systemu binarnego na dziesiętny metodą Hornera
 * 
 * Specyfikacja:
 *    Dane:
 *      - Liczba podana w systemie dwójkowym jako string
 *    Wynik:
 *      - Liczba przekonwertowana na liczbę dziesiętną
*/

int main()
{
  string binarna;
  cout << "Podaj liczbe binarna: ";
  cin >> binarna;
  int d = binarna.size();
  int a[d];
  for(int i = 0; i < d; i++)
  {
    if(binarna[i] == '1') a[i] = 1;
    else a[i] = 0;
  }
  int w = a[0];
  for(int i = 1; i < d; i++)
  {
    w = w * 2 + a[i];
  }
  cout << "Liczba dziesietna: " << w << endl;
}
