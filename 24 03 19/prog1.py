from dataclasses import dataclass

@dataclass
class Auto:
    marka: str
    kolor: str
    rocznik: int
    cena: float

auto = Auto("Porsche", "zielony", 2022, 700000)
print(auto.marka)
print(auto.kolor)
print(auto.rocznik)
print(auto.cena)