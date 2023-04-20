import math

file = open("liczby.txt", "r")
liczby = []
for line in file:
  liczby.append(int(line))

nwd = 0
for p,c in zip(liczby, liczby[1:]):
  if math.gcd(p,c) > nwd:
    nwd = math.gcd(p,c)
print(nwd)