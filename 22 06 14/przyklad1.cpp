#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
  srand(time(nullptr));
  int cel = rand() % 100 + 1;
  cout << "cel = " << cel << endl;
  while(true)
  {
    int losowa = rand() % 100 + 1;
    if(losowa != cel)
    {
      cout << "pudlo: " << losowa << endl;
      continue;
    }
    else
    {
      cout << "trafiony: " << endl;
      break;
    }
  }
  return 0;
}
