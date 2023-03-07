import math

t = []
p = []
n = int(input('n: liczba elementów tablicy T (więcej niż zero): '))
if n <= 0:
  exit()
k = int(input('k: liczba elementów tablicy P (więcej niż zero i n): '))
if k >= n:
  exit()
for i in range(0,n):
  x = int(input('Element ' + str(i) + ' tablicy T: '))
  t.append(x)
for i in range(0,k):
  x = int(input('Element ' + str(i) + ' tablicy P: '))
  p.append(x)
d = math.floor(len(t) / 4)
for i in range(0,d):
  t.remove(min(t))
  t.remove(max(t))
sig = (min(t) + max(t)) / 2
for i in p:
  if(i > sig):
    print(i, end=' ')