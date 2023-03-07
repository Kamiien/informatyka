//wprowadzanie tekstu ze spacjami
#include <iostream>
using namespace std;

main()
{
  int l;
  l = 0;
  string s;
  cout << "s = ";
  getline(cin, s);
  for(int i = 0; i < s.size(); i++) if(s[i] == ' ') l++;
  cout << l;
}