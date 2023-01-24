#include <iostream>
#include <cmath>
using namespace std;

bool isBin(string wyraz)
{
  int d = wyraz.size();
  for(int i = 0; i < d; i++)
  {
    if(wyraz[i] != 0 && wyraz[i] != 1)
      return false;
  }
  return true;
}

main()
{
  string binarna;
  cout << "Liczba binarna: ";
  cin >> binarna;
  //if(isBin(binarna)) cout << "Liczba jest binarna" << endl;
  //else
  //{
  //  cout << "Liczba nie jest binarna" << endl;
  //  return 1;
  //}
  int dziesietna = 0;
  int potega = 0;
  for(int i = binarna.size() - 1; i>=0; i++)
  {
    if(binarna[i]=='1')
    {
      dziesietna += pow(2,potega);
    }
    potega++;
  }
  cout << dziesietna;
}
