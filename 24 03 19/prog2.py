from dataclasses import dataclass

@dataclass
class Auto:
    marka: str
    kolor: str
    rocznik: int
    cena: float

n = int(input("Ilość: "))
a = []
for x in range(n):
    m = input("Marka: ")
    k = input("Kolor: ")
    r = input("Rocznik: ")
    c = input("Cena: ")
    a.append(Auto(m,k,r,c))
r = int(input("Rocznik: "))
for x in a:
    if r <= x.rocznik:
        print(f"{x.marka} {x.kolor} {x.rocznik} {x.cena}")
sr = 0
for x in a:
    sr += x.cena
sr = sr / len(a)
for x in a:
    if x.cena > sr:
        print(f"{x.marka} {x.kolor} {x.rocznik} {x.cena}")