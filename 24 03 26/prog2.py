class Uczen:
    def __init__(self, imie, nazwisko, klasa, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
        self.plec = plec

u = Uczen('Piotr', 'Kowalski', '3E', 'M')
print(u.imie)
u = Uczen('Anna', 'Nowak', '3E', 'K')