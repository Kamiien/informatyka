from decimal import *

pierwiastek = int(input("Podaj liczbę do spierwiastkowania: "))
getcontext().prec = 5 #int(input("Podaj liczby po przecinku: "))
a = pierwiastek
b = 1

while Decimal(a) != Decimal(b):
    a = (a + b) / 2
    b = pierwiastek / a
    print(a)
    print(b)
    print(Decimal(a))
    print(Decimal(b))
