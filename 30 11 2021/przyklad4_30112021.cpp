//wprowadzić z klawiatury wyraz i sprawdzić czy pierwsza litea jest taka sama jak ostatnia
//jeżeli tak to napisz "tak" a jak nie to napisz "nie"
#include <iostream>
using namespace std;

main()
{
  string s;
  cout << "s = ";
  getline(cin, s);
  if(s[0] == s[s.size()-1]) cout << "tak";
  else cout << "nie";
}