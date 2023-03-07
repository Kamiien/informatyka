#include <iostream>
using namespace std;
//lider to taki element zbioru, który występuje więcej razy niż połowa wszystkich elementów

main()
{
  int i,k,l;
  cout << "rozmiar tablicy: ";
  cin >> i;
  int t[i];
  for(int x = 0; x < i; x++)
  {
    cout << "t[" << x << "]= ";
    cin >> t[x]; 
  }
  for(int x = 0; x < i; x++)
  {
    k = t[x];
    l = 0;
    for(int y = 0; y < i; y++)
    {
      if(k == t[y]) l++;
    }
    if(l > i / 2)
    {
      cout << "Lider: " << k << endl;
      break;
    }
  }
}
