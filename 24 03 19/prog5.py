from dataclasses import dataclass

@dataclass
class Lot:
    numer: str
    trasa: str
    godzina_o: str
    godzina_p: str
    miejsca: list[str]
    nazwisko: list[str]
    cena: list[int]

lot = Lot('777', 'Poznań - Luton', '7:00', '13:00', ['A007', 'A008'], ['Nowak', 'Kowalska'], [1000, 1000])