#include <iostream>
#include <cmath>
using namespace std;
//z systemu rzymskiego -> 10 

bool sprawdzenie(string wyraz)
{
	int d = wyraz.size();
	for(int i=0; i<d; i++)
		{   //wyraz[i] - to kolejna literka wyrazu
			if(wyraz[i]!='I' && wyraz[i]!='V' && wyraz[i]!='X' && wyraz[i]!='C' 
			&& wyraz[i]!='D' && wyraz[i]!='L' && wyraz[i]!='M') return false;
		}
return true;	
}

//funkcja kt�ra na podstawie znaku rzymskiego zwraca warto�c liczbow�
int wyznacz(string rz, int w[], char literka)
{
	for(int i=0; i<rz.size();i++)
		{
			if(rz[i]==literka) return w[i];
		}

return -1;		
}


main()
{
string rzymska;
cout<<"rzymska=";
cin>>rzymska;
if(sprawdzenie(rzymska)==true) cout<<"liczba rzymska ok"<<endl;
else cout<<"liczba nie jest rzymska"<<endl;
int dziesietna= 0;
string rz="MDCLXVI";
int w[7]={1000,500,100,50,10,5,1};

//np. rzymska MCCXCIX
for(int i=0; i<rzymska.size(); i++)
	{
		//czy jest nastepnik rzymska[i]
		//kolejna literka wyrazu rzymski  
		if(i<=rzymska.size()-2)
		{
		//czy nastepna wi�ksza[i+1] ? od poprzedniej
		//czy rzymska[i] <rzymska
		int wartosc= wyznacz(rz,w,rzymska[i]);
		int nastepna = wyznacz(rz,w,rzymska[i+1] );
		if(nastepna>wartosc) dziesietna -=wartosc;
		else dziesietna +=wartosc;		
		}
		if(i==rzymska.size()-1)
		{
		int wartosc= wyznacz(rz,w,rzymska[i]);	
		dziesietna +=wartosc;
		}	
	}
cout<<dziesietna<<endl;	
}
//Kamil Stok�osa
