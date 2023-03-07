//program który liczy ile w wyrazie jest liter 'a'
#include <iostream>
using namespace std;

main()
{
  int l;
  l = 0;
  string s;
  cout << "s = ";
  cin >> s;
  for(int i = 0; i < s.size(); i++) if(s[i] == 'a' || s[i] == 'A') l++;
  cout << l;
}