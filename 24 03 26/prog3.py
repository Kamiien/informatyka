class Samochod:
    def __init__(self, marka, model, rocznik, przebieg):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.przebieg = przebieg
    def wczytaj(self, marka, model, rocznik, przebieg):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.przebieg = przebieg
    def wypisz(self):
        print(f'{self.marka} {self.model} {self.rocznik} {self.przebieg}')