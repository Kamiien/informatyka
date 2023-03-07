import math

x2 = float(input("Podaj x^2: "))
x1 = float(input("Podaj x: "))
a = float(input("Podaj wyraz wolny: "))
p = float(input("Podaj p: "))
q = float(input("Podaj q: "))
e = float(input("Podaj E: "))
s = abs(p + q) / 2

def f(i):
  return (i**2)*x2 + i * x1 + a

while abs(f(s)) > e and f(p) != 0 and f(q) != 0:
  if f(p)*f(s) < 0:
    q = s
  else:
    p = s
  s = abs(p + q) / 2

if(f(p) == 0):
  print(p)
if(f(q) == 0):
  print(q)
print(s)