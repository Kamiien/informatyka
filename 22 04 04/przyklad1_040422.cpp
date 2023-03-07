#include <iostream>
using namespace std;

bool sprawdzenie(string liczba)
{
  int d = liczba.size();
  for(int i = 0; i < d; i++)
    if(liczba[i] != '0' && liczba[i] != '1') return false;
  return true;
}

main()
#include <iostream>
using namespace std;
//dodawanie binarne
bool sprawdzenie(string liczba)
{
	int d= liczba.size();   
	for(int i=0; i<d; i++)
	    if(!(liczba[i]=='0' || liczba[i]=='1')) return false;
	    
return true;	    
}

main()
{
string w1, w2;
cout<<"liczba binarna 1 =";
cin>>w1;
cout<<"liczba binarna 2 =";
cin>>w2;

if(sprawdzenie(w1)==true && sprawdzenie(w2)==true)
{
	int d1 = w1.size();
	int d2 = w2.size();
	int n;     //wiêksza d³ugosc
	if(d1>d2) n=d1;
	else n=d2;
	int t1[n]={0};
	int t2[n]={0};
	
	int j=n-1;
	for(int i=d1-1; i>=0; i--,j--) //jedziemy od koñca pierwszego wyrazu
	    if(w1[i]=='1') t1[j]=1;
	    else t1[j]=0;
	j=n-1;    
	for(int i=d2-1; i>=0; i--,j--)
	    if(w2[i]=='1') t2[j]=1;
		else t2[j]=0;    
	//mamy przekonwertowane string do tablic wartoœci
	int pamiec=0;
	int wynik[n+1]; 
	//dodawanie realizujemy od koñca
	for(int i=n-1; i>=0; i--)
	{
		wynik[i+1]=(pamiec + t1[i]+t2[i])%2;
		pamiec = (t1[i]+t2[i])/2;
	}
	wynik[0]=pamiec;
	
	for(int i=0; i<n; i++) cout<<t1[i];
	cout<<endl;
	for(int i=0; i<n; i++) cout<<t2[i];
	cout<<endl;
	for(int i=0; i<n; i++) cout<<"-";
	cout<<endl;
	for(int i=0; i<n+1; i++) cout<<wynik[i];
	cout<<endl;
		
}
else cout<<"nie wprowadzono liczb w zapisie binarnym";


}