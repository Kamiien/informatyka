#include <iostream>
using namespace std;

main()
{
  int l;
  string nazwisko;
  cout << "Podaj nazwisko: ";
  cin >> nazwisko;
  l = nazwisko.size();
  for(int i = 0; i < l; i++)
  {
    cout << nazwisko[i] << " ";
  }
  cout << endl;
  for(int i = l; i >= 0; i--)
  {
    cout << nazwisko[i];
  }
  cout << endl;
}