"""
Algorytm wydawania reszty w najmniejszej ilości nominałów
"""
zaplacone = float(input("Wprowadź zapłaconą wartość: "))
produkt = float(input("Wprowadź wartość produktów: "))
if zaplacone < produkt:
    print("Nie starczy pieniędzy")
    exit(-1)
if zaplacone == produkt:
    print("Brak reszty")
    exit(0)
reszta = zaplacone - produkt
nominaly = [50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.01]
wyplata = []
while reszta != 0:
    for x in nominaly:
        if x <= reszta:
            wyplata.append(x)
            reszta = reszta - x
            break
print(wyplata)
